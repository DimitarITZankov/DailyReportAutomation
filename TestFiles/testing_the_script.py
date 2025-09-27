import pytest
from scripts.UpgradedVersionOfDailyReportScript import *
def test_open_csv_not_found(path):
    fake_path = path / "not_existing_file.csv"
    with pytest.raises(FileNotFoundError):
        open_csv(fake_path)
