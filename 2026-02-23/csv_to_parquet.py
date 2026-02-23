#!/usr/bin/env python3
import argparse
from pathlib import Path

import pandas as pd


def convert_csv_to_parquet(csv_path: Path, parquet_path: Path) -> None:
    df = pd.read_csv(csv_path)
    parquet_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(parquet_path, index=False, engine="pyarrow")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a CSV file to Parquet format."
    )
    parser.add_argument("csv_path", type=Path, help="Path to input CSV file")
    parser.add_argument("parquet_path", type=Path, help="Path to output Parquet file")
    args = parser.parse_args()

    convert_csv_to_parquet(args.csv_path, args.parquet_path)
    print(f"Converted '{args.csv_path}' -> '{args.parquet_path}'")


if __name__ == "__main__":
    main()
