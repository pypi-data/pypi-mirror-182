from gdshoplib.apps.platforms.base import BasePlatformManager
from gdshoplib.apps.platforms.vk.settings import Settings
from gdshoplib.packages.feed import Feed


class AvitoManager(BasePlatformManager, Feed):
    KEY = "AVITO"
    SETTINGS = Settings
