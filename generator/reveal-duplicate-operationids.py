from functools import singledispatchmethod
import deepmerge
import yaml


# Class for extracting operation IDs from an OpenAPI specification
class OpenAPIExtractor:
    def __init__(self):
        # Initialize operation IDs dictionary
        self.operation_ids = {}

    # Method to extract operation IDs, uses function overloading
    @singledispatchmethod
    def extract_operation_ids(self, value, path=""):
        # If the value is not a dictionary or list, just return the value
        return value

    # Function overload for dictionary values
    @extract_operation_ids.register
    def _(self, value: dict, path=""):
        # For each key, value pair in the dictionary
        for key, child in value.items():
            # Construct new path
            new_path = f"{path}/{key}" if path else key
            # Recursive call to handle nested structures
            self.extract_operation_ids(child, new_path)

        # If the current value is an operationId
        if "operationId" in value:
            # Get operationId
            operation_id = value["operationId"]
            # If operationId is not in the dictionary, initialize an empty list
            if operation_id not in self.operation_ids:
                self.operation_ids[operation_id] = []
            # Append current path to the list of paths for the current operationId
            self.operation_ids[operation_id].append(path)

    # Function overload for list values
    @extract_operation_ids.register
    def _(self, value: list, path=""):
        # For each item in the list
        for i, item in enumerate(value):
            # Construct new path
            new_path = f"{path}[{i}]"
            # Recursive call to handle nested structures
            self.extract_operation_ids(item, new_path)

    # Extracts operation ids and returns them
    def extract(self, value):
        self.extract_operation_ids(value)
        return self.operation_ids


# Function to extract operation IDs
def extract_operation_ids():
    # Open OpenAPI specification and operationId map
    with open("data/openapi.yml") as openapi_file, open(
        "data/operation-id-map.yml"
    ) as ops_file:
        # Load files
        openapi = yaml.load(openapi_file, Loader=yaml.FullLoader)
        ops = yaml.load(ops_file, Loader=yaml.FullLoader)

        # Combine OpenAPI and operationId map
        combined = deepmerge.always_merger.merge(openapi, ops)

        # Create extractor
        extractor = OpenAPIExtractor()
        # Extract operation ids
        operation_ids = extractor.extract(combined)

        # For each operationId, print it and the paths where it is found
        for operation_id, paths in operation_ids.items():
            if len(paths) > 1:
                print(
                    f"Operation ID '{operation_id}' is repeated {len(paths)} times. Paths:"
                )
                for path in paths:
                    print(path)


# Main function
if __name__ == "__main__":
    extract_operation_ids()
