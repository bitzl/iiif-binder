from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Please call /<path/to/folder>/manifest.json"}


@app.get("/{folder_path:path}/manifest.json")
async def manifest(folder_path: str):
    parts = folder_path.split("/")
    return {"path": folder_path, "parts": parts}
