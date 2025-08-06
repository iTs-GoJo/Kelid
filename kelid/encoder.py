import sys
from kelid.core import encode
from kelid.utils import read_file, write_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python encoder.py <input_file.py> [output_file.kl]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.rsplit('.',1)[0] + ".kl"

    code = read_file(input_file)
    encoded_code = encode(code)
    write_file(output_file, encoded_code)

    print(f"✅ فایل رمزگذاری شده ذخیره شد: {output_file}")

if __name__ == "__main__":
    main()
