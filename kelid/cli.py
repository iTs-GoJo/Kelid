import argparse
from .core import encode, run
from .utils import read_file, write_file, is_python_file

def main():
    parser = argparse.ArgumentParser(description="Kelid - Python Code Locker 🔐")
    parser.add_argument("command", choices=["encode", "run"], help="Command to run")
    parser.add_argument("input", help="Input file (for encode) or base64 string (for run)")
    parser.add_argument("-o", "--output", help="Output file for encoded result")

    args = parser.parse_args()

    if args.command == "encode":
        if not is_python_file(args.input):
            print("❌ Invalid Python file.")
            return

        code = read_file(args.input)
        encoded = encode(code)

        if args.output:
            write_file(args.output, encoded)
            print(f"✅ Encoded output written to: {args.output}")
        else:
            print("🔐 Encoded base64 string:\n")
            print(encoded)

    elif args.command == "run":
        try:
            run(args.input)
        except Exception as e:
            print(f"❌ Error running encoded code: {e}")

if __name__ == "__main__":
    main()
