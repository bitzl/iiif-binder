from pydantic import BaseModel


class Config(BaseModel):
    base_url: str
    url_identifier: str
    metadata: Metadata


class Metadata(BaseModel):
    title: str = None
    description: str = None
    navdate: str = None


class Image(BaseModel):
    url_id: str
    url_path: str
    width: int
    height: int
    media_type: str
