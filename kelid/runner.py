import sys
from kelid.core import run
from kelid.utils import read_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python runner.py <encoded_file.kl>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        encoded_code = read_file(input_file)
        run(encoded_code)
    except Exception as e:
        print(f"❌ خطا در اجرای فایل: {e}")

if __name__ == "__main__":
    main()
