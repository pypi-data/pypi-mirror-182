from dataclasses import dataclass
from hashlib import md5
from pathlib import Path
from trackrip import tracker

from typing import (
    Callable,
    Generic,
    Hashable,
    Iterable,
    Optional,
    Protocol,
    TypeVar,
    TypedDict,
)


TDigest = TypeVar("TDigest", bound=Hashable)


class Sample(TypedDict):
    name: str
    data: bytes


class Module(Protocol):
    samples: list[Sample]


@dataclass(frozen=True)
class Entry(Generic[TDigest]):
    mod_path: Path
    sample_name: str
    sample_hash: TDigest


def modgraph(
    mod_paths: Iterable[Path | str],
    *,
    replace_null_char: Optional[str] = " ",
    ignore_empty_samples: bool = True,
    sample_digest: Callable[[bytes], TDigest] = lambda x: md5(x).hexdigest(),
) -> list[Entry[TDigest]]:
    entries: list[Entry] = []

    for mod_path in mod_paths:
        mod_path = Path(mod_path)

        with open(mod_path, "rb") as mod_file:
            # why is it annotated as -> str? it returns a module object
            mod: Module = tracker.identify_module(mod_file)  # type: ignore

            for sample in mod.samples:
                if "data" not in sample and ignore_empty_samples:
                    continue

                sample_name = sample["name"]
                if replace_null_char is not None:
                    sample_name = sample_name.replace("\u0000", replace_null_char)

                sample_hash = sample_digest(sample.get("data", bytes()))

                entries.append(Entry(mod_path, sample_name, sample_hash))

    return entries
