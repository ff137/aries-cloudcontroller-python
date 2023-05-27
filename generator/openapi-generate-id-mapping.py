from collections import OrderedDict

import yaml


methods = ["get", "post", "put", "delete", "options", "head", "patch", "trace"]


def camel_to_snake(name):
    return "".join(["_" + i.lower() if i.isupper() else i for i in name]).lstrip("_")


# Function to load yaml file while preserving order of keys
def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    # Subclass of the yaml Loader
    class OrderedLoader(Loader):
        pass

    # Method to construct a mapping
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    # Add a constructor to the OrderedLoader
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
    )

    # Return loaded yaml content
    return yaml.load(stream, OrderedLoader)


# Function to dump yaml file while preserving order of keys
def ordered_dump(data, stream=None, Dumper=yaml.Dumper, **kwds):
    # Subclass of the yaml Dumper
    class OrderedDumper(Dumper):
        pass

    # Method to represent a dictionary
    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items()
        )

    # Add a representer to the OrderedDumper
    OrderedDumper.add_representer(OrderedDict, _dict_representer)

    # Return dumped yaml content
    return yaml.dump(data, stream, OrderedDumper, **kwds)


# Function to generate the operation ID map
def generate_operation_id_map():
    # Load the OpenAPI specification
    with open("/app/openapi.yml", "r") as f:
        openapi_data = ordered_load(f)

    # Initialize an empty dictionary to store the operation ID map
    operation_id_map = {}

    # Try to load existing operation ID map, if exists
    try:
        with open("/app/operation-id-map.yml", "r") as f:
            operation_id_map = ordered_load(f)
    except FileNotFoundError:
        pass

    # Make a copy of the operation ID map
    id_map = operation_id_map.copy()

    # If paths are not in the ID map, add them
    if "paths" not in id_map:
        id_map["paths"] = OrderedDict()

    # Get all the paths from the OpenAPI spec
    openapi_paths = openapi_data.get("paths", {})

    # Remove any paths in the ID map that do not exist in the OpenAPI spec
    for path in list(id_map["paths"]):  # iterating over a copy of the keys
        if path not in openapi_paths:
            del id_map["paths"][path]

    # Go through each path in the OpenAPI spec
    for path, path_item in openapi_paths.items():
        # If path is not in the ID map, add it
        if path not in id_map["paths"]:
            id_map["paths"][path] = OrderedDict()

        # If path is in the existing operation ID map
        if path in operation_id_map["paths"]:
            # Go through each method in the path
            for method in operation_id_map["paths"][path]:
                # If method is in the path item
                if method in path_item:
                    # Keep the existing operation ID
                    id_map["paths"][path][method] = {
                        "operationId": operation_id_map["paths"][path][method][
                            "operationId"
                        ]
                    }
        # Go through each method
        for method in methods:
            # If method is in the path item and not in the ID map
            if method in path_item and method not in id_map["paths"][path]:
                # Generate a new operation ID
                operation_id = camel_to_snake(path_item[method].get("summary", ""))
                # Add the new operation ID to the ID map
                id_map["paths"][path][method] = {"operationId": operation_id}

    # Sort the paths dictionary by keys (i.e., the paths)
    id_map["paths"] = OrderedDict(sorted(id_map["paths"].items()))

    # Save the ID map to a yaml file
    with open("/app/operation-id-map.yml", "w") as f:
        ordered_dump(id_map, f, default_flow_style=False)


if __name__ == "__main__":
    generate_operation_id_map()
