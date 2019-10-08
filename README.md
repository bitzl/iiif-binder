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

The application takes two arguments: The base path to the top level directory where the hierarchical image identifiers are resolved to relatively, and an optional base url for your image API endpoint for the manifest (defaults to http://127.0.0.1).

```
$ uvicorn main:app /base/path/image/folders [http://image/api/basepath]
```