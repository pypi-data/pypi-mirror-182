from requests.auth import HTTPBasicAuth


class Config:
    __url = "https://api.pagar.me/core/v5"

    @classmethod
    def set_auth(cls, headers):
        cls.__header = headers

    @classmethod
    def get_header(cls):
        return cls.__header

    @classmethod
    def get_url(cls):
        return cls.__url
