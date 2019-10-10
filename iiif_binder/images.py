from PIL import Image
from pathlib import Path
from typing import List
from urllib.parse import quote

import iiif_binder


def load_images(path: Path, base: Path) -> List[iiif_binder.Image]:
    images = []
    for image_path in path.glob("*.png"):
        img = Image.open(image_path)
        width, height = img.size
        url_path = image_path.relative_to(base)
        images.append(
            iiif_binder.Image(
                url_id=quote(str(url_path)),
                url_path=str(url_path),
                width=width,
                height=height,
                label=url_path.name,
                media_type="image/png",
            )
        )
    return images
