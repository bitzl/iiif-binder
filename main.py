from os import path
from os.path import exists, isdir
from pathlib import Path

from fastapi import FastAPI, HTTPException

from iiif_binder import load_config, load_metadata
from iiif_binder.images import load_images
from iiif_binder.manifest import generate_manifest


config = load_config()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Please call /<path/to/folder>/manifest.json"}


@app.get("/{folder_path:path}/manifest")
async def manifest(folder_path: Path):
    target = (config.base_path / folder_path).absolute()
    if not str(target.absolute()).startswith(str(config.base_path)):
        raise HTTPException(
            status_code=403, detail="Identifier must lead into base folder."
        )

    if not target.exists() or not target.is_dir():
        raise HTTPException(status_code=404, detail=f"Directory {target} not found.")

    images = load_images(target, config.base_path)
    metadata = load_metadata(target)

    return generate_manifest(str(folder_path), config, metadata, images)
