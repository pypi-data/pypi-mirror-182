from gdshoplib.apps.platforms.base import BasePlatformManager
from gdshoplib.apps.platforms.ok.settings import Settings
from gdshoplib.packages.feed import Feed


class OkManager(BasePlatformManager, Feed):
    KEY = "OK"
    SETTINGS = Settings
