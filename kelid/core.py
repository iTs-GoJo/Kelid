import marshal
import base64

def encode(code: str) -> str:
    """
    کد پایتون (رشته) رو می‌گیره و base64 رمزگذاری شده برمی‌گردونه
    """
    compiled = compile(code, "<kelid>", "exec")
    marshaled = marshal.dumps(compiled)
    encoded = base64.b64encode(marshaled).decode()
    return encoded

def run(encoded_code: str):
    """
    رشته base64 رمز شده رو می‌گیره، اجرا می‌کنه
    """
    marshaled = base64.b64decode(encoded_code)
    code = marshal.loads(marshaled)
    exec(code)
