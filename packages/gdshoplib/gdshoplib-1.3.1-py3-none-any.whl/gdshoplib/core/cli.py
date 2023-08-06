import typer
from rich import print

# from gdshoplib import Description, Media, NotionManager
from gdshoplib import Platform, Product
from gdshoplib.packages.cache import KeyDBCache
from gdshoplib.services.notion.settings import Settings as NotionSettings

app = typer.Typer()


# @app.command()
# def update_descriptions(sku=None):
#     description = Description()
#     if not sku:
#         for product in description.notion_manager.get_products(as_generator=True):
#             description.update(product["sku"])
#             print(f"Обновлен продукт {product['sku']}")
#         return

#     description.update(sku)
#     print(f"Обновлен продукт {sku}")


# @app.command()
# def update_media(sku=None):
#     media = Media()
#     if sku:
#         media.product_update(sku)
#         print(f"Медия {sku} обновлены")

#     for product in NotionManager().get_products(format="model", as_generator=True):
#         media.save(product)
#         print(f"Медия {product.dict()['sku']} обновлены")


# @app.command()
# def update_sku():
#     NotionManager().set_sku()


# @app.command()
# def warm_cache():
#     for product in Product(notion_manager={"caching": True}):
#         print(product.sku)


# @app.command()
# def warm_media():
#     for product in Product():
#         for media in product.media:
#             media.fetch()

#         print(product.sku)


@app.command()
def warm_feed(platform_key=None):
    settings = NotionSettings()
    cache = KeyDBCache(
        dsn=f"{settings.CACHE_DSN}/{settings.CACHE_DB}", cache_period=7 * 24 * 60 * 60
    )
    if platform_key:
        cache[f"feed/{platform_key}"] = Platform.get_platform(key=platform_key).feed()
        return

    for platform in Platform():
        cache[f"feed/{platform_key}"] = platform.feed()
        print(platform.manager.KEY)


if __name__ == "__main__":
    app()
