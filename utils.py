# utils.py

import pandas as pd
from io import BytesIO

def to_excel(df: pd.DataFrame):
    """Konvertiert ein DataFrame in eine Excel-Datei im Speicher."""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="IFC_Data")
    return output.getvalue()
