import boto3
from botocore.exceptions import ClientError

from gdshoplib.packages.settings import S3Settings


class S3:
    def __init__(self, data):
        self.data = data
        self.content = None
        self.settings = S3Settings()
        self.__session = None
        self.__client = None

    @property
    def session(self):
        if not self.__session:
            self.__session = boto3.session.Session()

        return self.__session

    @property
    def s3(self):
        if not self.__client:
            self.__client = self.session.client(
                service_name="s3",
                endpoint_url=self.settings.ENDPOINT_URL,
                aws_access_key_id=self.settings.ACCESS_KEY,
                aws_secret_access_key=self.settings.SECRET_KEY,
            )
        return self.__client

    def put(self):
        return self.s3.put_object(
            Bucket=self.settings.BUCKET_NAME,
            Key=self.file_key,
            Body=self.data.content,
            ACL="public-read",
            StorageClass="COLD",
            ContentType=self.data.mime,
        )

    @property
    def file_key(self):
        return f"{self.data.hash}.{self.data.format}"

    def get(self):
        try:
            return self.s3.get_object(
                Bucket=self.settings.BUCKET_NAME, Key=self.file_key
            )
        except ClientError as ex:
            if ex.response["Error"]["Code"] == "NoSuchKey":
                return None
            raise ex

    def delete(self):
        return self.s3.delete_object(
            Bucket=self.settings.BUCKET_NAME, Key=self.file_key
        )
