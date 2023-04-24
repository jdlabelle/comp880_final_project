"""
File: src/nhl_lines.py
Initial authors: Joshua LaBelle
Individual contributor: Joshua LaBelle
Date: 24 April 2023
"""


class Lines:
    """
    Represent a dataset with NHL Offensive Line and Defensive Pair statistics.
    Instance Variables:
        self.fin_name, self.fout_name: strings, names of input and output files
        self.list_of_line_dicts: list of dictionaries for each line/pair. See organize_by_line().
    """

    def __init__(self, filename_in, filename_out):
        """
        Create Lines object.
        :param filename_in: string, name of text file from which data is read
        :param filename_out: string, name of text file to which data is written
        :raise ValueError: if either arguments is either empty string or None
        """
        self.fin_name = filename_in
        self.fout_name = filename_out
        self.list_of_line_dicts = []

    def organize_by_line(self):
        """
        Helper function to read from file with name `self.fin_name` and initialize `self.list_of_line_dicts`, which is a
        list of dictionaries representing each line/pair statistics with keys name of each required statistic and values
        the actual data representation of that statistic. Calculates `weighted_average` for each line by dividing
        `goalsFor` by `goalsAgainst`.
        :return: List of Dictionaries
            keys: the name of each require statistic. "name", "position", "games_played", "team", "goalsFor",
            "goalsAgainst", "hitsFor", "weighted_average".
            values: Dataset representation of each statistic associated with each line/pair. "position" and "team" will
            be a string, "weighted_average" will be a float, and the rest are integers.
        """

    def most_effective_offensive_lines(self):
        """
        Identify the top 5 most effective offensive lines in the NHL for the 2022-2023 regular season. Take the data
        from `self.list_of_line_dicts` and return a dictionary of rank and offensive line.
        :return: Dictionary with five keys.
            keys: (Integer) representing `rank` (1 through 5)
            values: tuple with `name` and `weighted_average`.
        """

    def most_physical_defensive_pair(self):
        """
        Identify the defensive pair with the highest number of hits for each team. Take the data from
        `self.list_of_line_dicts` and return a dictionary with teams and defensive pairs.
        :return: Dictionary
            keys: string representing `team` (3 letter city abbreviation: BOS, DET, OTT, etc)
            values: string representing `name` (defensive pair names)
        """
