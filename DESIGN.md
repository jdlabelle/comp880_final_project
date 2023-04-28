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
  * initialize an empty dictionary `self.effective_lines`
    * holds the contents returned from `most_effective_offensive_lines()`
  * initialize an empty dictionary `self.physical_pairs`
    * holds the contents returned from `most_physical_defensive_pair()`

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
  * initialize the dictionary `line_dict` and build it as follows:
    * assign keys to this dictionary with `line_lst[0]` items (which are the headers, or stat names).
    * assign values to each key for the parallel item in each `line`.
      * these will be idx 2 for `name`, idx 3 for `team`, idx 4 for `position`, idx 6 for `games_played`, idx 26 for 
        `goalsFor`, idx 38 for `hitsFor`, idx 74 for `goalsAgainst`.
        * use type casting in order to transform the needed values to type int or float.
  * Use conditional _if elif else_ statements to handle the various scenarios for the `weighted_average` calculation and
    avoid a _divide by zero_ scenario.
    * for the happy path, add the key `weighted_average` and associated value as the calculation of `goalsFor` divided by `goalsAgainst` to
      each dictionary in `self.list_of_line_dicts`.
      * use the `round()` function here to round `weighted_average` to 2 decimal places.
    * else if `goalsAgainst` is equal to zero, the value of `goalsFor` is the `weighted_average`.
    * else `weighted_average` is equal to zero.
  * append `line_dict` to `self.list_of_line_dicts`.
* return `self.list_of_line_dicts`.


## *write_to_file* Design
```
  def write_to_file(self):
    """
    Write to the text file `self.fout_name` the data in
    `self.effective_lines` or `self.physical_pairs`.
    """
```
* use the _with_ statement to open self.fout_name for writing
  * assign to variable `file_out`
* ask for input if the user would like to write the contents of `self.effective_lines` or `self.physical_pairs` to
  the output file `data_out.txt`
  * assign the input to `choice`
* use an _if_ statement to write the `choice` to the output file.


## *most_effective_offensive_lines* Design
```
  def most_effective_offensive_lines(self):
    """
    Identify the top 5 most effective offensive lines in the NHL for the 2022-2023 regular season. Take the data
    from `self.list_of_line_dicts` and return a dictionary of rank and offensive line. Filters so that only lines
    with 30+ games played are considered.
    :return: Dictionary with five keys.
      keys: (Integer) representing `rank` (1 through 5)
      values: tuple with `name` (type string) and `weighted_average` (type float).
    """
```
#### Part 1:
* Use list comprehension to filter `self.list_of_line_dicts` and create a new list of dictionaries
  `filtered_list_of_line_dicts` that only include the dictionaries that have the key/value pair `position`: `line` and
  `games_played`: 30 or greater.
  * This new list will only contain dictionaries that represent offensive lines with 20+ games played, since this method
    is solely focused on offensive lines.
  * the comprehension will consist of a for loop with iterator `line_dict` and iterable `self.list_of_line_dicts`
  * it will also have an _if_ statement to only include the dictionaries where the value associated with the key
    `position` is equal to "line" _and_ `games_played` is greater than or equal to 30.

##### Part 2:
* Use the _sorted_ function to organize the dictionaries in `filtered_list_of_line_dicts` in descending order based on 
  the value associated with the key `weighted_average`. Assign this to `sorted_list_of_line_dicts`.
  * use indexing to only grab the first five dictionaries.
  * arguments for sorted function would be `filtered_list_of_line_dicts`, a _lambda_ function that will instruct the
    function to sort based on value associated with the key `weighted_average`, and `reverse=True` in order to specify
    descending order.
* construct the dictionary `most_effective_offensive_lines` using the values from `sorted_list_of_line_dicts`.
  * initialize the empty dictionary `self.effective_lines`
  * use a _for loop_ with iterator `i` and iterable `range(min(len(sorted_list_of_line_dicts), 5))`
    * this will allow us to create the dictionary using `i` as the common index, and the iterable is structured so that 
      if `sorted_list_of_line_dicts` has less than 5 entries, it will add to the dictionary the minimum number of dictionaries
      between the length of `sorted_list_of_line_dicts` and the integer 5. 
      * This will avoid an _index out of range error_ if `len(sorted_list_of_line_dicts)` is less than five
    * within the for loop, each key of `self.effective_lines` will start with the integer 1, and we can index
      `i`+1 to represent this (since `i` will start at 0).
    * assign the value to the tuple of index `i` of `sorted_list_of_line_dicts` key `name`, and index `i` of
      `sorted_list_of_line_dicts` key `weighted_average`.
* return `self.effective_lines`.


## *most_physical_defensive_pair* Design
```
  def most_physical_defensive_pair(self):
    """
    Identify the defensive pair with the highest number of hits for each team. Take the data from
    `self.list_of_line_dicts` and return a dictionary with teams and defensive pairs.
    :return: Dictionary
      keys: string representing `team` (3 letter city abbreviation: BOS, DET, OTT, etc)
      values: tuple with `name` and `hitsFor`
    """
```
* Initiate an empty dictionary `self.physical_pairs` to be the accumulator
* Use a _for loop_ to iterate through each dictionary in `self.list_of_line_dicts`
  * iterator will be `pair_dict` and iterable `self.list_of_line_dicts` 
  * use the following conditional statements:
    * _if_ value associated with key `position` in `pair_dict` is equal to `pairing`
      * this will filter for only defensive pairs
    * assign variables to dictionary values of the keys `team`, `name`, and `hitsFor` to variables `team`, `name`, and
      `hits`.
    * use an _if_ statement to add the associated key and values to `self.physical_pairs` if a team is not
      already in the dictionary
      * key assigned to `team`
      * values assigned as a tuple of `name` and `hits`
    * _else_ if that team is in the dictionary
      * check with a conditional to see if the `hits` is greater than the `current_hits` of the value currently
        contained in the dictionary associated with that `team`.
      * if True, update the value in `self.physical_pairs` with the new tuple `name` and `hits`
* return `self.physical_pairs`
