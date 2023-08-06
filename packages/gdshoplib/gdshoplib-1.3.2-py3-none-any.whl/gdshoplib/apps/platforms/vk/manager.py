from gdshoplib.apps.platforms.base import BasePlatformManager
from gdshoplib.apps.platforms.vk.settings import Settings
from gdshoplib.packages.feed import Feed


class VkManager(BasePlatformManager, Feed):
    DESCRIPTION_TEMPLATE = "vk.txt"
    KEY = "VK"
    SETTINGS = Settings
