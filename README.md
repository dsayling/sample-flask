# Sample Python App - Flask Server

TODO: links in this document will need updating after migration to another github organization

[![CircleCI Build Status](https://circleci.com/gh/dsayling/sample-flask.svg?style=shield)](https://circleci.com/gh/dsayling/sample-flask) [![Software License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/CircleCI-Public/cimg-python/master/LICENSE)

## Description

The sample app here is designed to demonstrate a simple python CircleCI workflows.

In this application we're simply installing dev python packages, with the [CircleCI python orb](https://circleci.com/developer/orbs/orb/circleci/python) and then running tests with pytest.

## Getting Started

You can see the CI pipeline for this application running [live on CircleCI](https://app.circleci.com/pipelines/github/dsayling/sample-flask?branch=main)

Here you can find the CircleCI configuration file, aka [config.yml](https://github.com/dsayling/sample-flask/blob/main/.circleci/config.yml). These links may need to be full URLs if this is indexed outside of github.

## Adapting to your workflow

The [config.yml](https://github.com/dsayling/sample-flask/blob/main/.circleci/config.yml) is well commented with the following tips and pointers:

* Find the definition of the executor and ensure the correct version of python is used for your application via the convenience image tag on the [CircleCI Developer Hub](https://circleci.com/developer/images/image/cimg/python).
* Find the `install-packages` command in the configuration file, here you can define an alternative `requirements.txt` file if necessary.
* Find the `Run Tests` step and include any additional runtime arguments necessary for `pytest` or update it to the testing tool you're using, e.g. `nosetests`

## Build and Test Locally

If you would like to try this application out locally, you can find runtime instructions below.

### Requirements

Python 3.5.2+ OR Docker

### Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t sample-flask .

# starting up a container
docker run -p 8080:8080 sample-flask
```

### Usage

If not using docker, to run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m openapi_server
```

### Tests

To launch the integration tests, use pytest:

```
pip3 install -r test-requirements.txt
pytest
```

## Additional Resources

[CircleCI Docs](https://circleci.com/docs/) - The official CircleCI Documentation website.
[CircleCI Configuration Reference](https://circleci.com/docs/2.0/configuration-reference/#section=configuration) - From CircleCI Docs, the configuration reference page is one of the most useful pages we have.


## License

This repository is licensed under the MIT license.
The license can be found [here](./LICENSE).

