#!/usr/bin/env bash

cd "$(dirname "$0")" || exit
CONTAINER_RUNTIME=${CONTAINER_RUNTIME:-docker}

CONTAINER_NAME=openapi-converter

OPENAPI_GENERATOR_CLI="openapitools/openapi-generator-cli:v6.6.0"

HOST_SHARED_DIR="$(pwd)/../data"
OPEN_API_MOUNT="/local"

${CONTAINER_RUNTIME} run --rm -v "${HOST_SHARED_DIR}:${OPEN_API_MOUNT}" \
    --name ${CONTAINER_NAME} ${OPENAPI_GENERATOR_CLI} \
    generate -i "${OPEN_API_MOUNT}/swagger.json" \
    -g openapi-yaml \
    -o "${OPEN_API_MOUNT}" \
    --skip-validate-spec
# the script will stop and remove the container after it's done due to the --rm flag

# move the generated OpenAPI file to your data directory and remove the generated directory
mv "${HOST_SHARED_DIR}/openapi/openapi.yaml" "${HOST_SHARED_DIR}/openapi.yml"
rm -rf "${HOST_SHARED_DIR}/openapi"
rm -rf "${HOST_SHARED_DIR}/.openapi-generator"
