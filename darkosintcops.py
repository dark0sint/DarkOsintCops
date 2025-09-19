import argparse
from darkosintcops.core import DarkOsintCopsCore

def main():
    parser = argparse.ArgumentParser(description="DarkOsintCops: Search .onion URLs on multiple search engines")
    parser.add_argument("search", help="The search string or phrase")
    parser.add_argument("--proxy", default="127.0.0.1:9050", help="Set Tor proxy (default: 127.0.0.1:9050)")
    parser.add_argument("--output", default=None, help="Output file name")
    parser.add_argument("--continuous_write", type=bool, default=False, help="Write progressively to output file")
    parser.add_argument("--limit", type=int, default=None, help="Max number of pages per engine to load")
    parser.add_argument("--engines", nargs="*", default=None, help="Engines to request")
    parser.add_argument("--exclude", nargs="*", default=None, help="Engines to exclude")
    parser.add_argument("--fields", nargs="*", default=["engine", "name", "link"], help="Fields to output")
    parser.add_argument("--field_delimiter", default=",", help="Delimiter for CSV fields")
    parser.add_argument("--mp_units", type=int, default=None, help="Number of processing units")

    args = parser.parse_args()

    core = DarkOsintCopsCore(
        proxy=args.proxy,
        output=args.output,
        continuous_write=args.continuous_write,
        limit=args.limit,
        engines=args.engines,
        exclude=args.exclude,
        fields=args.fields,
        field_delimiter=args.field_delimiter,
        mp_units=args.mp_units
    )

    core.search(args.search)

if __name__ == "__main__":
    main()
