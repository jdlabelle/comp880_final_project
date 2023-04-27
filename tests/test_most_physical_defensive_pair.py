"""
File: tests/test_most_physical_defensive_pair.py
Author and Individual Contributor: Joshua LaBelle
Date: 23 April 2023
"""
import os
import pytest
# pylint: disable=import-error
from src.nhl_lines import Lines
# pylint: enable=import-error

# pytest looks for files in the directory in which it is run,
# not in the directory where the test file exists.
# Thus, we need to include the path to the current file:
FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
)


def test_most_physical_defensive_pair():
    """
    Test happy path of most_physical_defensive_pair() method in Lines. Return a
    dictionary with key `team` and value `name` with the highest hits statistic
    for that team. Will only return defensive pairs; offensive lines are
    filtered out.
    """
    test_file_in = f'{FIXTURE_DIR}/data_10.txt'
    test_file_out = f'{FIXTURE_DIR}/data_10.txt'
    lines_obj = Lines(test_file_in, test_file_out)

    expected_result = {
        "OTT": "Chabot-Brannstrom", "DET": "Chiarot-Seider",
        "PIT": "Dumoulin-Letang", "COL": "Girard-Makar"
    }

    actual_result = lines_obj.most_physical_defensive_pair()

    assert actual_result == expected_result


if __name__ == '__main__':
    pytest.run()
