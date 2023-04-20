# Project Design Document

## *Class Lines* Design
* create the class `Lines`
  * This class will represent a dataset with NHL offensive line and defensive pair statistics.
* Instance Variables:
  * `self.fin_name`, `self.fout_name`: strings, names of input and output files

##  *__init__* Design
* create the class constructor `__init__`
  * parameters:
    * `self`, `filename_in`, `filename_out`
  * assign `self.fin_name` to `filename_in`
  * assign `self.fout_name` to `filename_out`
  * initialize an empty list `self.list_of_line_dicts`
    * this will hold a list of dictionaries representing line/pair statistics.
    * create a helper method to compute and return this.

## *most_effective_offensive_lines* Design
* Description: take the data from `self.list_of_line_dicts` and filter for the top 5 most effective lines in the NHL as
  determined by the weighted statistic Goals for divided by Goals against.
* Return a dictionary with keys `Rank` and values tuple of `line_name` and `weighted_average`.
* Calculate `weighted_average` by dividing `goals_for` by `goals_against`.

## *most_physical_defensive_pair_by_team* Design
* Description: take the data from `self.list_of_line_dicts` and filter for the defensive pair for each team with the 
  highest number of hits.
* Return a dictionary with key `team` and value `pair_name` with the highest hits statistic for that team.