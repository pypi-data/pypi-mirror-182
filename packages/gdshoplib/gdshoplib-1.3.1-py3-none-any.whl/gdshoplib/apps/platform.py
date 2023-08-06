from gdshoplib.apps.platforms.base import BasePlatformManager
from gdshoplib.apps.product import Product


class Platform:
    def __init__(self, manager=None):
        self.manager = manager
        self.__iterator = None

    def feed(self):
        assert self.manager, "В платформе не определен менеджер"
        return self.manager.get_feed(Product())

    @classmethod
    def get_platform(cls, *args, key, **kwargs):
        return cls(manager=BasePlatformManager.get_platform_manager_class(key=key)())

    @classmethod
    def iterator(cls):
        for platform in cls.__subclasses__():
            yield platform

    def __iter__(self):
        self.__iterator = self.__class__.iterator()
        return self

    def __next__(self):
        _next = next(self.__iterator)
        platform = Platform.get_platform(key=_next)
        return platform
