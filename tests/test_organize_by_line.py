"""
File: tests/test_organize_by_line.py
Initial authors: Joshua LaBelle
Individual contributor: Joshua LaBelle
Date: 24 April 2023
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


def test_organize_by_lines():
    """
    Tests happy path for helper function organize_by_lines(). Returns a list of dictionaries representing each line/pair
    statistics with keys `name` of each required statistic and values the actual data representation of that statistic.
    Additionally, calculates `weighted_average` for each line by dividing `goalsFor` by `goalsAgainst` for inclusion in
    the dictionary.
    """
    test_file_in = f'{FIXTURE_DIR}/data_1.txt'
    test_file_out = f'{FIXTURE_DIR}/data_1.txt'
    lines_obj = Lines(test_file_in, test_file_out)

    expected_result = [{"name": "Aho-Pulock", "team": "NYI", "position": "pairing", "games_played": 60, "goalsFor": 8,
                        "goalsAgainst": 8, "hitsFor": 65, "weighted_average": 1.0}]

    actual_result = lines_obj.organize_by_lines()

    assert actual_result == expected_result


if __name__ == '__main__':
    pytest.run()
