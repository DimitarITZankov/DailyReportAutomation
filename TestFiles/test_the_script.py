import pytest
import os
import pandas as pd
from scripts.UpgradedVersionOfDailyReportScript import open_csv

def test_open_csv_file_not_found(tmp_path):
    fake_path = tmp_path / "not_existing_file.csv"
    with pytest.raises(FileNotFoundError):
        open_csv(fake_path)
