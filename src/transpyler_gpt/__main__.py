import argparse
import json

from ._core import transpile


def main() -> None:
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description="Transpile Python code to an older version of Python."
    )
    parser.add_argument(
        "filename",
        help="The Python code file to transpile.",
    )
    parser.add_argument(
        "--target",
        dest="target_version",
        required=True,
        help="The target version of Python to transpile to.",
    )
    parser.add_argument(
        "--from",
        dest="from_version",
        help="The version of Python the code is written in. If not specified, the latest version of Python is assumed.",
    )
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument(
        "-o",
        "--output",
        help="The path to write the transpiled code to, by default it outputs to the stdout.",
    )
    output_group.add_argument(
        "-i",
        "--inplace",
        action="store_true",
        help="Overwrite the input file with the transpiled code.",
    )
    parser.add_argument(
        "--api-key",
        help="The API key to use for the OpenAI API. If not specified, the OPENAI_API_KEY environment variable is used.",
    )
    parser.add_argument(
        "--config",
        help="The path to the configuration file to call the completion API.",
    )
    args = parser.parse_args()

    if args.config:
        with open(args.config) as f:
            options_override = json.load(f)
    else:
        options_override = None
    with open(args.filename, encoding="utf-8") as f:
        code = f.read()
    transpiled_code = transpile(
        code,
        args.target_version,
        from_version=args.from_version,
        api_key=args.api_key,
        options_override=options_override,
    )
    if args.inplace:
        with open(args.filename, "w", encoding="utf-8") as f:
            f.write(transpiled_code)
    elif args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(transpiled_code)
    else:
        print(transpiled_code, flush=True)


if __name__ == "__main__":
    main()
