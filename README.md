# OpenAPI generated server

## Overview
This server was generated by the [OpenAPI Generator](https://openapi-generator.tech) project. By using the
[OpenAPI-Spec](https://openapis.org) from a remote server, you can easily generate a server stub.  This
is an example of building a OpenAPI-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t openapi_server .

# starting up a container
docker run -p 8080:8080 openapi_server
```

## Usage
If not using docker, to run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m openapi_server
```

### Access Swagger UI

You can use this UI to test API calls to the server.

```
http://localhost:8080/ZoomFoodToo/1.0.0/ui/
```

### See openapi spec in JSON

```
http://localhost:8080/ZoomFoodToo/1.0.0/openapi.json
```

### Tests
To launch the integration tests, use tox:

```
sudo pip install tox
tox
```

## Swagger Editor

You can also start up the swagger editor with the local spec file.

When you're done editing the file though, you'll have to download it from the browser and replace the `zoomfood-openapi.yml` in the project directory.

```bash
docker run -p 8081:8080 -v $(pwd):/tmp -e SWAGGER_FILE=/tmp/zoomfood-openapi.yaml swaggerapi/swagger-editor
```
 ## Spec Generator

 The root specification `zoomfood-openapi.yaml` can be used to generate other code bases. Soon this spec file will have a source of truth where the generation should be done from - until then, you can generate other code bases using the OpenAPI spec prebuilt image.

 ```
 docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli list
 ```

 Shows you want you can generate and then feed into

 ```
 docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i /local/zoomfood-openapi.yaml \
    -g lang-to-generate \
    -o /local/dest-dir-for-generated-code
```
