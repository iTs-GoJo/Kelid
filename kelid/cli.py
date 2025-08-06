import argparse
from encoder import encode_file
from runner import run_file

def main():
    parser = argparse.ArgumentParser(description="Kelid - File Encoder")
    sub = parser.add_subparsers(dest="command")

    ef = sub.add_parser("encode-file", help="رمزنگاری یک فایل .py")
    ef.add_argument("input", help="مسیر فایل ورودی .py")
    ef.add_argument("-o", "--output", help="مسیر فایل خروجی", default="output.kelid")

    rf = sub.add_parser("run-file", help="اجرای فایل .kelid رمزنگاری شده")
    rf.add_argument("file", help="مسیر فایل رمز شده")

    args = parser.parse_args()

    if args.command == "encode-file":
        encode_file(args.input, args.output)
    elif args.command == "run-file":
        run_file(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
