from pydantic import BaseSettings


class S3Settings(BaseSettings):
    ENDPOINT_URL: str = "https://storage.yandexcloud.net"
    BUCKET_NAME: str = "gdshop"
    ACCESS_KEY: str
    SECRET_KEY: str
