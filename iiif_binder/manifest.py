from builtins import license
from os.path import basename
from typing import List

from pydantic import BaseModel

from iiif_binder import Config, Metadata, Image


def generate(config: Config, metadata: Metadata, images: List[Image]) -> dict:
    manifest = {
        "@context": "http://iiif.io/api/presentation/2/context.json",
        "@type": "sc:Manifest",
        "@id": f"{config.base_url}/{config.url_identifier}/manifest",
    }

    if metadata.title is not None:
        manifest["label"] = metadata.title
    else:
        manifest["label"] = config.url_identifier

    if metadata.navdate is not None:
        manifest["navdate"] = metadata.navdate

    if metadata.license is not None:
        manifest["license"] = metadata.license

    if metadata.attribution is not None:
        manifest["attribution"] = metadata.attribution

    manifest["sequences"] = [
        {
            "@id": "https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb00109488/sequences/normal",
            "@type": "sc:Sequence",
            "canvases": [
                canvas(index, config, image) for (index, image) in enumerate(images)
            ],
        }
    ]
    return manifest


def canvas(index: int, config: Config, image: Image):
    canvas_id = f"{config.base_url}/{image.url_path}/canvas/{index}"
    canvas = {
        "@id": canvas_id,
        "@type": "sc:Canvas",
        "label": image.url_path,
        "images": [
            {
                "@type": "oa:Annotation",
                "motivation": "sc:painting",
                "resource": {
                    "@id": f"{config.image_base_url}/{image.url_id}/full/full/0/default.jpg",
                    "@type": "dctypes:Image",
                    "service": {
                        "@context": "http://iiif.io/api/image/2/context.json",
                        "@id": f"https://api.digitale-sammlungen.de/iiif/image/v2/{image.url_id}",
                        "profile": "http://iiif.io/api/image/2/level2.json",
                        "protocol": "http://iiif.io/api/image",
                    },
                    "format": image.media_type,
                    "width": image.width,
                    "height": image.height,
                },
                "on": canvas_id,
            }
        ],
        "width": image.width,
        "height": image.height,
    }
    return canvas
