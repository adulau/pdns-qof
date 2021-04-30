import sys
import json
import jsonschema
from jsonschema import validate


def get_schema(filename):
    """This function loads the given schema available"""
    with open(filename, 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(json_data, schema=None):
    """REF: https://json-schema.org/ """

    try:
        validate(instance=json_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message


if __name__ == "__main__":
    schema = get_schema("schema/schema.json")

    # Convert json to python object.
    with open(sys.argv[1], 'r') as ndjson_file:
        for line in ndjson_file:
            jsonData = json.loads(line)
            # validate it
            is_valid, msg = validate_json(jsonData, schema=schema)
            print(msg)
