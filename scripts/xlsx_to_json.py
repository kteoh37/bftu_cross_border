"""
Convert each xlsx in excel_files/ into a compact columnar JSON in data/json/.

Output shape per dataset (columnar + categorical encoding to keep size small):
{
  "name": "BFTU_iBoPS",
  "id_columns":        ["country", "year", "region", "income_group", ...],
  "indicators":        ["total", "total_in", ...],
  "categorical":       ["country", "region", "income_group", "income_subgroup",
                        "code_wdi", "code_ifs", "code_weo"],
  "categories": {
    "country":      ["Albania", "Algeria", ...],
    "region":       ["Africa", ...],
    ...
  },
  "columns": {
    "country":      [12, 12, 12, 0, 0, ...],   # int indices into categories.country
    "year":         [1995, 1996, ...],         # numeric column kept inline
    "total":        [0.31, 0.32, ...],
    ...
  },
  "meta": {
    "n_rows":   5655,
    "year_min": 1995,
    "year_max": 2023
  }
}

This format is roughly 5-10x smaller than long-format JSON because:
  - column names appear once, not per-row
  - categorical strings are deduplicated into a lookup table

Run from the repo root:
    python scripts/xlsx_to_json.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]
XLSX_DIR = REPO_ROOT / "excel_files"
OUT_DIR = REPO_ROOT / "data" / "json"

ID_COLS = [
    "country", "year", "code_wdi", "code_ifs",
    "region", "income_group", "income_subgroup", "code_weo",
]

CATEGORICAL_COLS = [
    "country", "region", "income_group", "income_subgroup",
    "code_wdi", "code_ifs", "code_weo",
]

DATASETS = [
    "BFTU_iBoPS.xlsx",
    "BFTU_iBoPC.xlsx",
    "BFTU_iBoPC_Intensity.xlsx",
    "BTFU_iBoPC_Subcategories.xlsx",
    "FKRSU_LLM.xlsx",
]


def _to_jsonable(v):
    if v is None:
        return None
    if isinstance(v, float):
        if math.isnan(v):
            return None
        # Round to 6 sig figs to shrink size; tweak if more precision needed.
        return round(v, 6)
    return v


def _round_floats(arr):
    out = []
    for v in arr:
        if v is None or (isinstance(v, float) and math.isnan(v)):
            out.append(None)
        elif isinstance(v, float):
            out.append(round(v, 6))
        else:
            out.append(v)
    return out


def convert(xlsx_path: Path) -> dict:
    df = pd.read_excel(xlsx_path)
    df.columns = [c.lstrip("﻿").strip() for c in df.columns]

    id_cols = [c for c in ID_COLS if c in df.columns]
    indicator_cols = [c for c in df.columns if c not in id_cols]

    categories: dict[str, list] = {}
    columns: dict[str, list] = {}

    for col in df.columns:
        series = df[col]
        if col in CATEGORICAL_COLS:
            cat = series.astype("category")
            categories[col] = [str(x) for x in cat.cat.categories.tolist()]
            # -1 sentinel for NaN -> we map back to None on read
            codes = cat.cat.codes.tolist()
            columns[col] = [None if c == -1 else int(c) for c in codes]
        elif col == "year":
            columns[col] = [int(v) if not (isinstance(v, float) and math.isnan(v)) else None
                            for v in series.tolist()]
        else:
            columns[col] = _round_floats(series.tolist())

    meta = {
        "n_rows": int(len(df)),
        "year_min": int(df["year"].min()) if "year" in df else None,
        "year_max": int(df["year"].max()) if "year" in df else None,
    }

    return {
        "name": xlsx_path.stem,
        "id_columns": id_cols,
        "indicators": indicator_cols,
        "categorical": [c for c in CATEGORICAL_COLS if c in df.columns],
        "categories": categories,
        "columns": columns,
        "meta": meta,
    }


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    index = []

    for fname in DATASETS:
        src = XLSX_DIR / fname
        if not src.exists():
            print(f"skip (missing): {src}")
            continue

        print(f"converting {fname} ...")
        payload = convert(src)
        out = OUT_DIR / f"{payload['name']}.json"
        out.write_text(json.dumps(payload, separators=(",", ":")))
        size_mb = out.stat().st_size / 1e6
        print(f"  -> {out.name}  ({size_mb:.2f} MB, {payload['meta']['n_rows']:,} rows)")
        index.append({
            "name": payload["name"],
            "file": f"data/json/{payload['name']}.json",
            "indicators": payload["indicators"],
            "id_columns": payload["id_columns"],
            "meta": payload["meta"],
        })

    (OUT_DIR / "index.json").write_text(json.dumps(index, indent=2))
    print(f"\nwrote {OUT_DIR / 'index.json'}")


if __name__ == "__main__":
    main()
