from argparse import ArgumentParser
from collections import Counter
from csv import writer as CsvWriter
from json import dumps as to_json
from pathlib import Path
from sys import stdout

from .modgraph import modgraph


def main() -> int:
    parser = ArgumentParser(prog="modgraph")

    # fmt: off
    parser.add_argument(
        "files", help="module files to analyze",
        type=Path, nargs="+")
    parser.add_argument(
        "-f", "--format", help="output format",
        choices=["csv", "d2"], default="csv")
    parser.add_argument(
        "-r", "--rank", help="min number of repeats for sample to be included",
        type=int, default=1)
    # fmt: on

    args = parser.parse_args()

    entries = modgraph(args.files)

    sample_hash_counts = Counter(e.sample_hash for e in entries)
    entries = list(e for e in entries if sample_hash_counts[e.sample_hash] >= args.rank)

    if args.format == "csv":
        writer = CsvWriter(stdout, escapechar="\\")
        writer.writerow(("mod_path", "sample_name", "sample_hash"))
        for e in entries:
            writer.writerow((e.mod_path, e.sample_name, e.sample_hash))

    elif args.format == "d2":
        escape = lambda x: to_json(str(x), ensure_ascii=False)

        print(f"direction: right")

        for e in entries:
            sample_id = f"sample.{escape(e.sample_hash)}"
            module_id = f"module.{escape(e.mod_path)}"
            sample_name = escape(e.sample_name)

            print(f"{sample_id} -> {module_id}.{sample_name}")

    return 0
