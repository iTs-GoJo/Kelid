 main()
import argparse
from .core import encode, run
from .utils import read_file, write_file, is_python_file

def main():
    parser = argparse.ArgumentParser(description="Kelid - Python Code Locker 🔐")
    subparsers = parser.add_subparsers(dest="command")

    # encode command
    encode_parser = subparsers.add_parser("encode", help="رمزگذاری کد پایتون (رشته یا فایل)")
    encode_parser.add_argument("input", help="مسیر فایل .py یا کد به صورت رشته")
    encode_parser.add_argument("-o", "--output", help="مسیر فایل خروجی برای ذخیره نتیجه")

    # run command
    run_parser = subparsers.add_parser("run", help="اجرای کد رمزگذاری شده")
    run_parser.add_argument("input", help="کد base64 رمزگذاری شده یا مسیر فایل")

    # encode-file command
    encode_file_parser = subparsers.add_parser("encode-file", help="رمزگذاری فایل .py به .kl")
    encode_file_parser.add_argument("input", help="مسیر فایل .py ورودی")
    encode_file_parser.add_argument("-o", "--output", help="مسیر فایل خروجی .kl")

    # run-file command
    run_file_parser = subparsers.add_parser("run-file", help="اجرای فایل .kl رمزگذاری شده")
    run_file_parser.add_argument("input", help="مسیر فایل .kl")

    args = parser.parse_args()

    if args.command == "encode":
        if is_python_file(args.input):
            code = read_file(args.input)
        else:
            code = args.input
        encoded = encode(code)
        if args.output:
            write_file(args.output, encoded)
            print(f"✅ خروجی رمزگذاری شده در فایل {args.output} ذخیره شد.")
        else:
            print(encoded)

    elif args.command == "run":
        if is_python_file(args.input):
            code = read_file(args.input)
            encoded = encode(code)
            run(encoded)
        else:
            try:
                # فرض می‌کنیم ورودی رشته base64 است
                run(args.input)
            except Exception as e:
                # اگر ورودی مسیر فایل بود
                try:
                    code = read_file(args.input)
                    run(code)
                except Exception as e2:
                    print(f"❌ خطا در اجرا: {e}\n{e2}")

    elif args.command == "encode-file":
        if not is_python_file(args.input):
            print("❌ فایل ورودی باید .py باشد.")
            return
        code = read_file(args.input)
        encoded = encode(code)
        output_path = args.output if args.output else args.input.rsplit(".", 1)[0] + ".kl"
        write_file(output_path, encoded)
        print(f"✅ فایل رمزگذاری شده در {output_path} ذخیره شد.")

    elif args.command == "run-file":
        try:
            encoded = read_file(args.input)
            run(encoded)
        except Exception as e:
            print(f"❌ خطا در اجرای فایل: {e}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
