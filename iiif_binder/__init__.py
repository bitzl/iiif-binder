import json
from os.path import exists

from pydantic import BaseModel, Path


class Config(BaseModel):
    base_url: str
    viewing_hint: str = "individuals"
    base_path: Path
    image_base_url: str
    thumbnail_size: int = 256


class Metadata(BaseModel):
    title: str = None
    description: str = None
    navdate: str = None
    viewing_hint: str = "individuals"
    license: str = None
    attribution: str = None


class Image(BaseModel):
    url_id: str
    url_path: str
    width: int
    height: int
    media_type: str
    label: str


def load_config() -> Config:
    with open("config.json") as fp:
        data = json.load(fp)
    config = Config(**data)
    config.base_path = config.base_path.absolute()
    return config


def load_metadata(target: Path) -> Metadata:
    metadata_file = target / "metadata.json"

    if not metadata_file.exists():
        return Metadata()

    with metadata_file.open("r") as fp:
        data = json.load(fp)
    return Metadata(**data)
