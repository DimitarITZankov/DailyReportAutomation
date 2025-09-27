import pytest
import os
import pandas as pd
from scripts.UpgradedVersionOfDailyReportScript import open_csv,generate_daily_reports

def test_open_csv_file_not_found(tmp_path):
    fake_path = tmp_path / "not_existing_file.csv"
    with pytest.raises(FileNotFoundError):
        open_csv(fake_path)

def test_generate_daily_reports():
    df = pd.DataFrame({"Kg":[100,200,300],
                       "Date" : ['25/10/2025','25/10/2025','25/10/2025'],
                       "Price" : [100.0,200.0,300.0],})
    result_df, _ = generate_daily_reports(df)
    assert result_df["Kg"].sum() == 600