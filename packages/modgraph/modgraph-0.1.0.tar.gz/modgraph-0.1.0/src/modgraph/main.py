from argparse import ArgumentParser
from csv import writer as CsvWriter
from dataclasses import dataclass
from hashlib import md5
from pathlib import Path
from sys import stdout
from typing import Any, Protocol, TypedDict
from trackrip import tracker


class Sample(TypedDict):
    name: str
    data: bytes


class Module(Protocol):
    samples: list[Sample]


@dataclass(frozen=True)
class EntryKey:
    mod_path: Path
    sample_hash: str


@dataclass
class Entry:
    mod_path: Path
    sample_name: str
    sample_hash: str
    count: int


def main() -> int:
    parser = ArgumentParser(prog="modgraph")
    parser.add_argument("files", type=Path, nargs="+", help="module files to analyze")
    args = parser.parse_args()

    entries: dict[EntryKey, Entry] = {}

    for mod_path in args.files:
        with open(mod_path, "rb") as mod_file:
            # why is it annotated as -> str? it returns a module object
            mod: Module = tracker.identify_module(mod_file)  # type: ignore

            for sample in mod.samples:
                if "data" not in sample:
                    continue

                sample_name = sample["name"]
                sample_hash = md5(sample["data"]).hexdigest()

                key = EntryKey(mod_path, sample_hash)

                e = entries.get(key)
                if e is None:
                    entries[key] = Entry(mod_path, sample_name, sample_hash, 1)
                else:
                    e.count += 1

    writer = CsvWriter(stdout, escapechar="\\")
    writer.writerow(("mod_path", "sample_name", "sample_hash", "count"))
    for e in entries.values():
        writer.writerow((e.mod_path, e.sample_name, e.sample_hash, e.count))

    return 0
