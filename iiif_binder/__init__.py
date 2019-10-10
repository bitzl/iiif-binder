from pydantic import BaseModel

import json


class Config(BaseModel):
    base_url: str
    url_identifier: str
    viewing_hint: str = "individuals"


class Metadata(BaseModel):
    title: str = None
    description: str = None
    navdate: str = None
    viewing_hint: str = "individuals"


class Image(BaseModel):
    url_id: str
    url_path: str
    width: int
    height: int
    media_type: str


def load_config() -> Config:
    with open("config.json") as fp:
        data = json.load(fp)
    return Config(**data)
