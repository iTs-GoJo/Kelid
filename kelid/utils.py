import os

def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path: str, data: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)

def is_python_file(path: str) -> bool:
    return path.endswith(".py") and os.path.isfile(path)
