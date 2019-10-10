# IIIF Dynamic Presentation

## Introduction

The goal is to create a manifest for a directory of images on the fly,

Projects that produce images either need backend services (e.g. a database), newly generated manifests for each new image, or often some howngrown software for this project. This IIIF presentation server takes an folder path, relative to the image root directory and generates a manifest containing all images that are present at that time.

Additional metadata (e.g. a title or description) can be define via file named `meta.json` in the same directory as the image files. Both the file and each entry are completely optional.

```json
{
    "title": "Samples for α = 1.17",
    "description": "Random samples based on a froobnicular model with α = 1.17.",
    "navDate": "2019-10-21",
}
```

## Usage

The application reads its configuration from a JSON file named `config.json` in the directory where the app is started.

App startup:

```
$ uvicorn main:app /base/path/image/folders [http://image/api/basepath]
```

Minimal `config.json`:

```json
{
    "base_url": "http://localhost:8000",
    "image_base_url": "http://localhost:1234",
    "base_path": "images"
}
```