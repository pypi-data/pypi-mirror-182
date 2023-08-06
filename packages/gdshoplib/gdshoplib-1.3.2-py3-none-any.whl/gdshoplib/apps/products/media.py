import re
from enum import Enum
from typing import Optional

import magic
import requests
from pydantic import BaseModel

from gdshoplib.packages.s3 import S3
from gdshoplib.services.notion.notion import Notion


class ProductMedia:
    def __init__(self, block, notion=None):
        self.notion = Notion() if not notion else notion
        self.block = block

        url = self.block[self.block["type"]]["file"]["url"]

        self.data = ProductMediaModel(
            key=self.notion.get_capture(self.block) or f"{self.block['type']}_general",
            type=self.block["type"],
            url=url,
            block_id=self.block["id"],
        )
        self.s3 = S3(self)

    def __getattr__(self, name: str):
        if name not in ("data", "block"):
            if name in self.data.dict().keys():
                try:
                    return self.data.__getattribute__(name)
                except MediaContentException:
                    self.refresh()
                    return self.data.__getattribute__(name)

        return super().__getattribute__(name)

    def fetch(self):
        if not self.check_access():
            self.refresh()

        if not self.s3.get():
            self.s3.put()
        return self.s3.get()

    def get_url(self):
        return f"{self.s3.settings.ENDPOINT_URL}/{self.s3.settings.BUCKET_NAME}/{self.s3.file_key}"

    def check_access(self):
        return requests.get(self.data.url).ok

    def refresh(self):
        self.block = self.notion.get_block(self.block["id"], cached=False)
        url = self.block[self.block["type"]]["file"]["url"]
        self.data = ProductMediaModel(
            key=self.notion.get_capture(self.block) or f"{self.block['type']}_general",
            type=self.block["type"],
            url=url,
            block_id=self.block["id"],
        )


class MediaEnum(str, Enum):
    video = "video"
    image = "image"


class ProductMediaModel(BaseModel):
    parsed: bool = False
    block_id: str
    key: str
    url: str
    type: MediaEnum

    name: Optional[str]
    format: Optional[str]
    content: Optional[bytes]
    hash: Optional[str]
    mime: Optional[str]

    def __parse(self):
        if self.parsed:
            return

        response = requests.get(self.url)
        if not response.ok:
            raise MediaContentException

        self.name = ProductMediaModel.parse_name(self.url)
        self.format = ProductMediaModel.parse_format(self.url)
        self.content = response.content
        self.hash = response.headers.get("x-amz-version-id")
        self.mime = response.headers.get("content-type")

        self.parsed = True

        if not all([self.name, self.format, self.content, self.hash, self.mime]):
            raise MediaParseException

    @staticmethod
    def parse_format(url):
        pattern = re.compile(r"\/.*\.(\w+)(\?|$)")
        r = re.findall(pattern, url)
        return r[0][0] if r else None

    @staticmethod
    def parse_name(url):
        pattern1 = re.compile(r".*\/(?P<name>.*)")
        r = re.findall(pattern1, url)
        if not r or not r[0]:
            return None
        return r[0].split("?")[0]

    def get_mime(self):
        return magic.from_buffer(self.get_content(), mime=True)

    def __getattribute__(self, name):
        exceptions = {*super(ProductMediaModel, self).__dict__.keys()} - {
            "key",
            "type",
            "url",
            "block_id",
            "parsed",
            "dict",
        }
        if name in exceptions:
            self.__parse()
        return super(ProductMediaModel, self).__getattribute__(name)


class MediaContentException(Exception):
    ...


class MediaParseException(Exception):
    ...
