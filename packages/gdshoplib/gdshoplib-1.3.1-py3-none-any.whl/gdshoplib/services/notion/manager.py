import functools
import logging

import requests as r

from gdshoplib.packages.cache import BaseCache
from gdshoplib.services.notion.settings import Settings

logger = logging.getLogger(__name__)


class Manager:
    SETTINGS = Settings
    BASE_URL = "https://api.notion.com/v1/"

    def __init__(self, caching=False) -> None:
        self.settings = self.SETTINGS()
        self.caching = caching
        if self.settings.CACHE:
            self.CACHE = BaseCache.get_class(self.settings.CACHE_CLASS)(
                dsn=self.settings.CACHE_DSN + str(self.settings.CACHE_DB),
                cache_period=self.settings.CACHE_PERIOD,
            )

    def get_cache_key(self, path, **kwargs):
        return f"{path}"

    def check_cacheble(self, *args, **kwargs):
        return kwargs.get("method").upper() == "GET" or "query" in args[0]

    def get_headers(self):
        return {
            **self.auth_headers(),
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
            "Accept": "application/json",
        }

    def auth_headers(self):
        return {"Authorization": "Bearer " + self.settings.NOTION_SECRET_TOKEN}

    def cache_response(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            if self.settings.CACHE and not kwargs.get("cached") is False:
                cached = self.CACHE.get(self.get_cache_key(*args, **kwargs))

                if cached and not self.caching:
                    return cached

            data = func(self, *args, **kwargs)

            if self.check_cacheble(*args, **kwargs):
                self.CACHE[self.get_cache_key(*args, **kwargs)] = data

            return data

        return wrap

    @cache_response
    def make_request(self, path, *, method, params=None, cached=True):
        _path = f"{self.BASE_URL}{path}"
        _params = (
            dict(params=params) or {}
            if method.upper() == "GET"
            else dict(json=params) or {}
        )

        _r = r.request(
            method,
            _path,
            headers=self.get_headers(),
            **_params,
        )
        if not _r.ok:
            logger.warning(_r.json())
            assert (
                False
            ), f"Запрос {method.upper()} {_path} прошел с ошибкой {_r.status_code}/n"

        return _r.json()

    def pagination(self, url, *, params=None, **kwargs):
        _params = params or {}
        response = None
        while True:
            response = self.make_request(url, params=_params, **kwargs)
            next_cursor = self.pagination_next(response)

            if next_cursor is None or next_cursor is False:
                return response
            else:
                return self.pagination(
                    url, params={**_params, **dict(start_cursor=next_cursor)}, **kwargs
                )

    def pagination_next(self, response):
        """Выдаем данные для следующего"""
        if not response:
            return None

        if not response.get("has_more"):
            return False

        return response["next_cursor"]
