# Project Design Document

## *Class Lines* Design
```
  class Lines:
    """
    Represent a dataset with NHL Offensive Line and Defensive Pair statistics.
    Instance Variables:
      self.fin_name, self.fout_name: strings, names of input and output files
      self.list_of_line_dicts: list of dictionaries for each line/pair. See organize_by_line().
    """
```
* create the class `Lines`
  * This class will represent a dataset with NHL offensive line and defensive pair statistics.
* Initialize Instance Variables:
  * `self.fin_name`, `self.fout_name`: strings, names of input and output files
  * `self.list_of_line_dicts`: list of dictionaries for each line/pair. Updated by `organize_by_line` helper method.

##  *__init__* Design
```
  def __init__(self, filename_in, filename_out):
    """
    Create Lines object.
    :param filename_in: string, name of text file from which data is read
    :param filename_out: string, name of text file to which data is written
    :raise ValueError: if either arguments is either empty string or None
    """
```
* create the class constructor `__init__`
  * parameters:
    * `self`, `filename_in`, `filename_out`
  * assign `self.fin_name` to `filename_in`
  * assign `self.fout_name` to `filename_out`
  * initialize an empty list `self.list_of_line_dicts`
    * this will hold a list of dictionaries representing line/pair statistics.
    * create a helper method to compute and return this.

## *organize_by_line* Design
```
  def organize_by_line(self):
    """
    Helper function to read from file with name `self.fin_name` and initialize `self.list_of_line_dicts`, which is a
    list of dictionaries representing each line/pair statistics with keys name of each required statistic and values
    the actual data representation of that statistic. Calculates `weighted_average` for each line by dividing
    `goalsFor` by `goalsAgainst`.
    :return: List of Dictionaries
      keys: the name of each require statistic. "name", "position", "games_played", "team", "goalsFor",
      "goalsAgainst", "hitsFor", "weighted_average".
      values: Dataset representation of each statistic associated with each line/pair. "name", "position", and "team" will
      be type string, "games_played" will be type int, and all others will be type float.
    """
```
* Use the _with_ statement to open `filename_in` and assign it to the variable `f_in`.
* initialize an empty list, `self.list_of_line_dicts` to be the final return value accumulator.
* initialize an empty list, `line_lst`, to be an interim accumulator.
* use a _for loop_ with iterator `row` and iterable `f_in.readlines()`.
  * use the _split_ method on each `row` and assign to `row_lst`.
  * append each `row_lst` to `line_lst`.
  * this will give us a list of parallel lists from which we can construct `self.list_of_line_dicts`.
* Use a _for loop_ with iterator `line` and iterable `line_lst`. Index `line_lst` so that a dictionary is not created
  from the header, which is `line_lst[0]`
  * initialize an empty dictionary `line_dict`.
  * assign keys to this dictionary with `line_lst[0]` items (which are the headers, or stat names).
  * assign values to each key for the parallel item in each `line`.
    * these will be idx 2 for `name`, idx 3 for `team`, idx 4 for `position`, idx 6 for `games_played`, idx 26 for 
      `goalsFor`, idx 38 for `hitsFor`, idx 74 for `goalsAgainst`.
      * use type casting in order to transform the needed values to type int or float.
    * append `line_dict` to `self.list_of_line_dicts`.
  * add the key `weighted_average` and associated value as the calculation of `goalsFor` divided by `goalsAgainst` to
    each dictionary in `self.list_of_line_dicts`.
* return `self.list_of_line_dicts`.

## *most_effective_offensive_lines* Design
```
  def most_effective_offensive_lines(self):
    """
    Identify the top 5 most effective offensive lines in the NHL for the 2022-2023 regular season. Take the data
    from `self.list_of_line_dicts` and return a dictionary of rank and offensive line.
    :return: Dictionary with five keys.
      keys: (Integer) representing `rank` (1 through 5)
      values: tuple with `name` (type string) and `weighted_average` (type float).
    """
```
* Use the _sorted_ function to organize the dictionaries in `self.list_of_line_dicts` in descending order based on the
  value associated with the key `weighted_average`. Assign this to `sorted_top_five`.
  * use indexing to only grab the first five dictionaries.
  * arguments for sorted function would be `self.list_of_line_dicts`, a _lambda_ function that will instruct the
    function to sort based on value associated with the key `weighted_average`, and `reverse=True` in order to specify
    descending order.
* construct the dictionary `most_effective_offensive_lines` using the values from `sorted_top_five`.
  * cast the type _tuple_ with the tuple() function
* return `most_effective_offensive_lines`.


## *most_physical_defensive_pair* Design
* Description: take the data from `self.list_of_line_dicts` and filter for the defensive pair for each team with the 
  highest number of hits. Will only return defensive pairs; offensive lines will be filtered out.
* Return a dictionary with key `team` and value `pair_name` with the highest hits statistic for that team.