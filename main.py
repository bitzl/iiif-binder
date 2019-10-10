from fastapi import FastAPI
from iiif_binder import load_config

config = load_config()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Please call /<path/to/folder>/manifest.json"}


@app.get("/{folder_path:path}/manifest.json")
async def manifest(folder_path: str):
    parts = folder_path.split("/")
    return {"path": folder_path, "parts": parts}
