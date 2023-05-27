from functools import singledispatchmethod
import re

import deepmerge
from inflection import camelize
import yaml


# Class to clean OpenAPI specs by applying specific rules
# NB: must be run within docker context to resolve file paths
class OpenAPICleaner:
    # Regex pattern to match old-style '#/definitions' schema references
    FIX_REF_RE = re.compile(r"#/definitions")

    # Replace null descriptions with empty strings
    @singledispatchmethod
    def no_null_descriptions(self, value):
        return value

    # If the value is a dictionary, traverse each key-value pair
    @no_null_descriptions.register
    def _(self, value: dict):
        for child in value.values():
            self.no_null_descriptions(child)

        # If the key "description" exists and its value is None, replace it with an empty string
        if "description" in value and value["description"] is None:
            value["description"] = ""

    # If the value is a list, traverse each item
    @no_null_descriptions.register
    def _(self, value: list):
        for item in value:
            self.no_null_descriptions(item)

    # Make sure all externalDocs have a url
    @singledispatchmethod
    def no_missing_external_doc_urls(self, value):
        return value

    # If the value is a dictionary, traverse each key-value pair
    @no_missing_external_doc_urls.register
    def _(self, value: dict):
        for child in value.values():
            self.no_missing_external_doc_urls(child)

        # If the key "externalDocs" exists and it doesn't have a "url", add a placeholder url
        if "externalDocs" in value and "url" not in value["externalDocs"]:
            value["externalDocs"]["url"] = "https://example.com/replace/me"

    # If the value is a list, traverse each item
    @no_missing_external_doc_urls.register
    def _(self, value: list):
        for item in value:
            self.no_missing_external_doc_urls(item)

    # Replace old-style '#/definitions' schema references with '#/components/schemas'
    @singledispatchmethod
    def fix_refs(self, value):
        return value

    # If the value is a dictionary, traverse each key-value pair
    @fix_refs.register
    def _(self, value: dict):
        for child in value.values():
            self.fix_refs(child)

        # If the key "$ref" exists, replace the old reference style with the new one
        if "$ref" in value:
            value["$ref"] = self.FIX_REF_RE.sub("#/components/schemas", value["$ref"])

    # If the value is a list, traverse each item
    @fix_refs.register
    def _(self, value: list):
        for item in value:
            self.fix_refs(item)

    # Replace "*/*" content type with "application/json"
    @singledispatchmethod
    def fix_content_types(self, value):
        return value

    # If the value is a dictionary, traverse each key-value pair
    @fix_content_types.register
    def _(self, value: dict):
        for child in value.values():
            self.fix_content_types(child)

        # If the key "*/*" exists, replace it with "application/json"
        if "*/*" in value:
            value["application/json"] = value["*/*"]
            del value["*/*"]

    # If the value is a list, traverse each item
    @fix_content_types.register
    def _(self, value: list):
        for item in value:
            self.fix_content_types(item)

    # Apply all cleaning methods
    def clean(self, value):
        self.no_null_descriptions(value)
        self.no_missing_external_doc_urls(value)
        self.fix_refs(value)
        self.fix_content_types(value)


# Function to merge OpenAPI specs with operation ID map
def merge_operation_ids():
    with open("/app/openapi.yml") as openapi_file, open(
        "/app/operation-id-map.yml"
    ) as ops_file:
        openapi = yaml.load(openapi_file, Loader=yaml.FullLoader)
        ops = yaml.load(ops_file, Loader=yaml.FullLoader)

    return deepmerge.always_merger.merge(openapi, ops)


if __name__ == "__main__":
    # Merge the OpenAPI specs with the operation ID map
    result = merge_operation_ids()

    OpenAPICleaner().clean(result)
    # Write the cleaned result back to the OpenAPI file
    with open("/app/openapi.yml", "w") as openapi_file:
        yaml.dump(result, openapi_file, sort_keys=False)
