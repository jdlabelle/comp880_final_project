"""
File: tests/test_most_effective_offensive_lines.py
Author and Individual Contributor: Joshua LaBelle
Date: 23 April 2023
"""
import os
import pytest
# pylint: disable=import-error
from src.lines import Lines
# pylint: enable=import-error

# pytest looks for files in the directory in which it is run,
# not in the directory where the test file exists.
# Thus, we need to include the path to the current file:
FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
)


def test_most_effective_offensive_lines():
    """
    Test happy path of most_effective_offensive_lines() method in Lines. Returns dictionary with key `rank` and value
    tuple with `name` and `weighted_average`.
    """
    test_file_in = f'{FIXTURE_DIR}/data_5.txt'
    test_file_out = f'{FIXTURE_DIR}/data_5.txt'
    lines_obj = Lines(test_file_in, test_file_out)

    expected_result = {1: ("Connor-Dubois-Scheifele", 2.67), 2: ("Cogliano-Compher-O'Connor", 2.67),
                       3: ("Comtois-Strome-Zegras", 1.2), 4: (), 5: ()}

    actual_result = lines_obj.most_effective_offensive_lines()
    assert actual_result == expected_result


if __name__ == '__main__':
    pytest.run()
