# CSV to Parquet Converter

Simple Python script to convert a `.csv` file into `.parquet` format.

## Requirements

- Python 3.8+
- `pandas`
- `pyarrow`

## Install

```bash
pip install pandas pyarrow
```

## Usage

```bash
python csv_to_parquet.py input.csv output.parquet
```

## Example

```bash
python csv_to_parquet.py data/sales.csv data/sales.parquet
```

After running, the output Parquet file will be created at the path you provided.
