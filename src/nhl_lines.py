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
            values: Dataset representation of each statistic associated with each line/pair. "name", "position", and
                    "team" will be type string, "games_played" will be type int, and all others will be type float.
        """
        with open(self.fin_name, 'r') as f_in:
            self.list_of_line_dicts = []
            line_lst = []
            for row in f_in.readlines():
                row_lst = row.split(',')
                line_lst.append(row_lst)
            for line in line_lst[1:]:
                line_dict = {line_lst[0][2]: line[2], line_lst[0][3]: line[3], line_lst[0][4]: line[4],
                             line_lst[0][6]: int(line[6]), line_lst[0][26]: float(line[26]),
                             line_lst[0][74]: float(line[74]), line_lst[0][38]: float(line[38])}
                if line_dict["goalsFor"] > 0 and line_dict["goalsAgainst"] != 0:
                    line_dict["weighted_average"] = round(line_dict["goalsFor"] / line_dict["goalsAgainst"], 2)
                elif line_dict["goalsFor"] > 0 and line_dict["goalsAgainst"] == 0:
                    line_dict["weighted_average"] = line_dict["goalsFor"]
                else:
                    line_dict["weighted_average"] = 0
                self.list_of_line_dicts.append(line_dict)
            return self.list_of_line_dicts



    def most_effective_offensive_lines(self):
        """
        Identify the top 5 most effective offensive lines in the NHL for the 2022-2023 regular season. Take the data
        from `self.list_of_line_dicts` and return a dictionary of rank and offensive line. Filters so that only lines
        with 30+ games played are considered.
        :return: Dictionary with five keys.
            keys: (Integer) representing `rank` (1 through 5)
            values: tuple with `name` (type string) and `weighted_average` (type float).
        """
        # filter for only offensive lines and teams with 20+ games played
        filtered_list_of_line_dicts = [line_dict
                                       for line_dict in self.list_of_line_dicts
                                       if line_dict["position"] == "line" and line_dict["games_played"] >= 30]

        # sort the filtered list of lines from highest weighted average to lowest
        sorted_list_of_line_dicts = sorted(filtered_list_of_line_dicts, key=lambda x: x["weighted_average"],
                                           reverse=True)

        # construct the return dictionary
        most_effective_offensive_lines = {}
        for i in range(min(len(sorted_list_of_line_dicts), 5)):  # avoid an index out of range error
            most_effective_offensive_lines[i+1] = (sorted_list_of_line_dicts[i]['name'],
                                                   sorted_list_of_line_dicts[i]['weighted_average'])

        return most_effective_offensive_lines

    def most_physical_defensive_pair(self):
        """
        Identify the defensive pair with the highest number of hits for each team. Take the data from
        `self.list_of_line_dicts` and return a dictionary with teams and defensive pairs.
        :return: Dictionary
            keys: string representing `team` (3 letter city abbreviation: BOS, DET, OTT, etc)
            values: string representing `name` (defensive pair names)
        """


def main():
    lines_obj = Lines("../data/NHL_Line_Data.csv", "data_out.txt")
    lines_obj.organize_by_line()
    output = lines_obj.most_effective_offensive_lines()
    print(output)


main()


