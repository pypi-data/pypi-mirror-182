from jinja2 import Environment, FileSystemLoader, select_autoescape

from gdshoplib.core.settings import settings


class ProductDescription:
    def __init__(self, product):
        self.product = product
        self.jinja2_env = self.jinja2_env()

    def __getattr__(self, name: str):
        if name not in ("__dict__", "__page"):
            key = f"_{name}"

            if key in self.__dict__.keys():
                return self.__dict__.get(key)

            return self.product.__getattr__(name)

    def split(self, source):
        for tag in source.split("/"):
            yield tag.strip()

    @property
    def tags(self):
        yield from self.split(self.product.tags)

    @property
    def specifications(self):
        yield from self.split(self.product.specifications)

    @property
    def notes(self):
        yield from self.split(self.product.notes)

    def generate(self, platform):
        return self.render(platform)

    def get_template(self, platform):
        return self.jinja2_env.get_template(platform.DESCRIPTION_TEMPLATE)

    def render(self, platform):
        return self.get_template(platform).render(product=self.product)

    @classmethod
    def jinja2_env(cls):
        return Environment(
            loader=FileSystemLoader(settings.TEMPLATES_PATH),
            autoescape=select_autoescape(),
        )
