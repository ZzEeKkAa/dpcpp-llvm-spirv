import json
import os.path
import sys


def get_pkg_version(index_json_fn: str) -> str:
    """Extract version field from info/index.json.

    Arg:
       index_json_fn: path to info/index.json

    Return:
       version as a string
    """
    if not os.path.exists(index_json_fn):
        raise FileNotFoundError(f"File {index_json_fn} could not be found")

    with open(index_json_fn, "r") as fh:
        data = json.load(fh)

    if "version" not in data:
        raise RuntimeError("JSON data does not contain 'version' key.")

    return data["version"]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    else:
        fn = os.path.join("compiler", "info", "index.json")

    print(get_pkg_version(fn))
