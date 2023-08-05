import sys
import os

if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.dirname(
        os.path.realpath(__file__))), "src")
    sys.path.append(path)

    from powerml.utils.config import get_config
    print(get_config())
    print(get_config({"powerml": {"key": "test"}}))
