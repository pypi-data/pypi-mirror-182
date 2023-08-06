from lxml import objectify

from gdshoplib.apps.platforms.base import BasePlatformManager
from gdshoplib.apps.platforms.ula.settings import Settings
from gdshoplib.core.settings import settings
from gdshoplib.packages.feed import Feed


class UlaManager(BasePlatformManager, Feed):
    DESCRIPTION_TEMPLATE = "ula.txt"
    KEY = "ULA"
    SETTINGS = Settings

    def get_shop(self):
        shop = objectify.Element("shop")
        objectify.deannotate(shop, cleanup_namespaces=True, xsi_nil=True)

        return shop

    def get_offer(self, product):
        offer = super(UlaManager, self).get_offer(product)
        offer.youlaCategoryId = self.settings.CATEGORY_ID
        offer.youlaSubcategoryId = self.settings.SUBCATEGORY_ID
        offer.tovary_vid_zhivotnogo = 10463
        offer.managerName = settings.MANAGER_NAME
        offer.address = settings.ADDRESS
        offer.phone = settings.PHONE
        objectify.deannotate(offer, cleanup_namespaces=True, xsi_nil=True)
        return offer
