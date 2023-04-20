## The NHL Lines and Pairings of the 2022-2023 Regular Season

**Contributors**: Joshua LaBelle

**Date**: 13 April 2023

### Data Source
_MoneyPuck_: NHL Dataset website who collected their data from sources including the National Hockey League
(NHL) and ESPN.

Website URL: https://www.moneypuck.com/data.htm

### Motivation
As an avid hockey player and lifelong Boston Bruins fan, diving into this dataset is exciting for
me. The 2022-2023 season has been a special one, as the Bruins have set a new record for most wins 
in an NHL regular season, and can be considered one of the best teams of all time.

The Goal of this project will be to investigate and identify the most effective lines and defensive pairings for
the 2022-2023 NHL season.

### Data Documentation

#### Basics: Contact Distribution and Access
Dataset Name: 2022-2023  NHL Lines/Pairings

Date last updated: 14 April 2023 0602hrs

Can be accessed by anyone via the _MoneyPuck_ website

#### Dataset Contents
Includes statistical data for every single offensive line and defensive pairing during throughout the 2022-2023
NHL regular season.

* Each item is a single line or defensive pair 
* Number of dataset (row) items:  2947
* There are 108 different stats (column items), examples include:
  * Line/Pair name
  * Games played
  * Total ice time (minutes)
  * Goals percentage
  * Goals against
  * Face-offs won
* The dataset covers all games to date in the 2022-2023 regular season for the NHL

#### Intended Use of Dataset
The intended purpose for the dataset is to track NHL statistics and analyze how teams/lines/players have performed over
time. It can also be used to help make future predications on team performance.

#### Data Collection Procedures
The data was collected and compiled from publicly available statistical data provided by the National Hockey League and 
ESPN.

The data was collected and compiled by the owners and moderators of https://www.moneypuck.com/. 

MoneyPuck has stated that their data collections are free to use as long as they are clearly credited. This is
explicitly stated on their site on this page: https://www.moneypuck.com/data.htm.

#### Representativeness
This data represents all 2022-2023 regular season data for EVERY SINGLE NHL line that played, even if that line only
played one game. No group or team was omitted. 

#### Data Quality
The number of statistics tracked in the dataset is impressive, and nothing significant has been omitted.

There are some statistics and formulas in the data set that are more complex or unclear in exactly what they represent.
In those cases, I will choose not to use those statistics.

There are no data validity issues, as the data is updated daily and pulled directly from the source (NHL/ESPN). Updates
to the dataset can be found here: https://www.moneypuck.com/data.htm.

#### Privacy
All data is publicly available and not considered sensitive.

### Investigative Questions

1. What were the most effective lines in the NHL for the 2022 - 2023 Season?
   * Data fields used to determine this: Minutes played (set a minimum filter), Goals For, Goals Against, Name
   * Results produced will be the top-five lines in the NHL based on the weighted average of _Goals for_ divided by 
     _Goals Against_ (GF/GA).
   * Minutes Played will be used to filter lines so that only those that have 200 total minutes or more played will be
     factored in.
   * The results will be presented by a dictionary with the top level key being the rank (one through five) and value
     being a string of the specific line _name_  and  the weighted average of GF/GA.

2. What was the most physical defensive pair for each team in the NHL in the 2022-2023 season?
    * Data fields used: Hits for, Team, Name
    * Results will be the defensive pair for each team in the NHL with the highest _Hits for_ statistic
    * The result will be presented as a dictionary with each _Team_ as the key and value as the _name_ of the 
      pair