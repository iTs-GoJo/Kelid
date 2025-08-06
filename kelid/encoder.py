import marshal, base64

def encode_file(input_file: str, output_file: str):
    with open(input_file, "r", encoding="utf-8") as f:
        source = f.read()

    code = compile(source, "<string>", "exec")
    marshaled = marshal.dumps(code)
    encoded = base64.b64encode(marshaled)

    with open(output_file, "wb") as f:
        f.write(encoded)

    print(f"[✓] فایل با موفقیت رمزنگاری شد: {output_file}")
