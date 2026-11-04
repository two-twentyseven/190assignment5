import os, sys
import json


def main() -> None:
    unused = 42
    try:
        print(does_not_exist)
    except:
        pass
    print(os.getcwd())
    print(sys.version)
