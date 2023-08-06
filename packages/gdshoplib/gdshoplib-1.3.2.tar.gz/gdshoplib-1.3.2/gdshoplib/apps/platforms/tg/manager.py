from gdshoplib.apps.platforms.base import BasePlatformManager
from gdshoplib.apps.platforms.tg.settings import Settings
from gdshoplib.packages.feed import Feed


class TgManager(BasePlatformManager, Feed):
    KEY = "TG"
    SETTINGS = Settings
