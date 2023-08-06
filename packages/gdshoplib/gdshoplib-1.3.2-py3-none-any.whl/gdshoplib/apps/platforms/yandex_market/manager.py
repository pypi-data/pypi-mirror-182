from gdshoplib.apps.platforms.base import BasePlatformManager
from gdshoplib.packages.feed import Feed

from .settings import Settings


class YandexMarketManager(BasePlatformManager, Feed):
    KEY = "YM"
    SETTINGS = Settings
