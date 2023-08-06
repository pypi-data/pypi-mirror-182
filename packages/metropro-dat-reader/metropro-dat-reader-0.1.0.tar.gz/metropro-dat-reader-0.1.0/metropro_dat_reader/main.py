#%%
import csv
from typing import Any, Dict, List, Literal, TypedDict
import struct
import argparse
from pathlib import Path


KeyType = Literal["IB", "S", "FB", "IL", "C", "NA"]


class KeyField(TypedDict):
    start: int
    end: int
    key: KeyType
    name: str
    value: Any


def parse_field(data: bytes, type: KeyType):
    lookup = {
        "IB": lambda x: int.from_bytes(x, byteorder="big"),
        "S": lambda x: x.decode("utf-8"),
        "FB": lambda x: struct.unpack(">f", x),
        "FL": lambda x: struct.unpack("<f", x),
        "IL": lambda x: int.from_bytes(x, byteorder="little"),
        "I": lambda x: int.from_bytes(x, byteorder="little"),
        "C": lambda x: x.decode("utf-8"),
        "NA": lambda x: x.decode("utf-8"),
    }
    return lookup[type](data)


def keys_from_file(file_name: str = "key.csv") -> List[KeyField]:
    field_listing = []
    with open(Path(__file__).parent / "key.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for i, row in enumerate(spamreader):

            if len(row) != 4:
                print(i, len(row))
                break

            if row[3] == "not_used":
                continue

            if i == 0:
                continue

            field_listing.append(
                {
                    "start": int(row[0]),
                    "end": int(row[1]),
                    "key": row[2],
                    "name": row[3],
                    # "value": "unknown",
                }
            )
    return field_listing


def get_raw_data(file_name: str = str(Path(__file__).parent / "sample.dat")) -> bytes:
    with open(file_name, "rb") as f:
        data = f.read()
    return data


def app():

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The file to parse")
    args = parser.parse_args()
    if (not Path(args.file).exists()):
        raise FileNotFoundError(f"{args.file} does not exist")
    print(Path(args.file))

    file_keys = keys_from_file()
    data = get_raw_data(args.file)

    for field in file_keys:
        try:
            print(
                f'{field["name"]}:',
                parse_field(
                    data[field["start"] - 1 : field["end"]],
                    field["key"],
                ),
            )
        except Exception as e:
            print(f"Error parsing {field=}")
            print(e,"\n")
            continue

if __name__ == "__main__":
    app()