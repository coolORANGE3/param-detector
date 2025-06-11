#!/usr/bin/env python3

import argparse
from urllib.parse import urlparse, parse_qs
import re

# ANSI color codes
ANSI_COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m"
}

def banner():
    print("🛠️ param-detector - Made by coolORANGE3\n")

def highlight_params(url, param_names, color):
    color_code = ANSI_COLORS.get(color.lower(), ANSI_COLORS["red"])
    reset_code = ANSI_COLORS["reset"]

    for param in param_names:
        pattern = re.compile(rf"(?<=\?|&){re.escape(param)}(?==)")
        url = pattern.sub(f"{color_code}{param}{reset_code}", url)

    return url

def detect_params(url, color):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if not query_params:
        print("No parameters found in the URL.")
        return

    param_names = list(query_params.keys())
    print(f"Found {len(param_names)} parameter(s):")
    for param in param_names:
        print(f"- {param}")

    print("\nHighlighted URL:")
    highlighted_url = highlight_params(url, param_names, color)
    print(highlighted_url)

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Detect and highlight parameters in a URL.\n"
            "🎨 Supported colors: black, red, green, yellow, blue, magenta, cyan, white"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-u", "--url", required=True, help="URL to inspect")
    parser.add_argument(
        "--color",
        default="red",
        help="Highlight color for parameters (default: red)"
    )
    args = parser.parse_args()

    banner()
    detect_params(args.url, args.color)

if __name__ == "__main__":
    main()
