import base64, marshal

def run_file(file_path: str):
    with open(file_path, "rb") as f:
        encoded = f.read()

    try:
        marshaled = base64.b64decode(encoded)
        code = marshal.loads(marshaled)
        exec(code)
    except Exception as e:
        print(f"[!] خطا در اجرای فایل: {e}")
