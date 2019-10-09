from pydantic import BaseModel


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
