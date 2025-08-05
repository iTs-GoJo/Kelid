import base64
import marshal

def encode(code: str) -> str:
    compiled = compile(code, "<kelid>", "exec")
    dumped = marshal.dumps(compiled)
    encoded = base64.b64encode(dumped).decode()
    return encoded

def run(encoded_code: str):
    dumped = base64.b64decode(encoded_code.encode())
    code = marshal.loads(dumped)
    exec(code)
