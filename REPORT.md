## Project Report

**Contributors**: Joshua LaBelle

**Date**: 30 April 2023

### 1. Purpose
The purpose of this program is to take the National Hockey League (NHL) dataset from the 2022-2023 regular season and
process it in order answer some very specific statistical on offensive line and defensive pair performance. The data 
set that is used for this project is the NHL Lines and Pairs dataset from https://moneypuck.com.

### 1.1 Motivation
I love the sport of hockey as a player myself and as a fan. This project gave me the opportunity to explore and answer 
some statistical questions based on the recently completed NHL season. I see alot of datasets that analyze NHL player
and team performance, but very rarely do I see a statistical focus on how offensive lines and defensive pairs have
performed and stacked up to each other. This led to my decision to focus this project around my this specific dataset
in order to investigate something unique.

### 1.2 Dataset
**Dataset Overview**
* **Basics: Contact Distribution and Access**
  * Dataset Name: 2022-2023  NHL Lines/Pairings
  * Dataset Owner/Manager: https://moneypuck.com
  * Date last updated: 30 April 2023 0530 hrs 
  * Can be accessed by anyone via the _MoneyPuck_ website
* **Dataset Contents**
  * Includes statistical data for every single offensive line and defensive pairing during throughout the 2022-2023
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
  * The dataset covers all line/pair statistics for games in the 2022-2023 regular season for the National Hockey 
    League.

* **Intended Use of Dataset**
  * The intended purpose for the dataset is to track NHL statistics and analyze how teams/lines/players have performed over
  time. It can also be used to help make future predications on team performance.

**Dataset Details**
* **Data Collection Procedures**
  * The data was collected and compiled from publicly available statistical data provided by the National Hockey League and 
  ESPN. 
  * The data was collected and compiled by the owners and moderators of https://www.moneypuck.com/. 
  * MoneyPuck has stated that their data collections are free to use as long as they are clearly credited. This is
    explicitly stated on their site on this page: https://www.moneypuck.com/data.htm.

* **Representativeness**
  * This data represents all 2022-2023 regular season data for EVERY SINGLE NHL line and pair that played in at least
    one regular season game. No group or team was omitted. 

* **Data Quality and Preprocessing**
  * The number of statistics tracked in the dataset is impressive, and nothing significant has been omitted. 
  * There are some statistics and formulas in the data set that are more complex or unclear in exactly what they 
    represent. In those cases, I will choose not to use those statistics. 
  * There are no data validity issues, as the data is updated daily and pulled directly from the source (NHL/ESPN). Updates
    to the dataset can be found here: https://www.moneypuck.com/data.htm.
  * Dataset does not need pre-processing or cleaning.

* **Privacy**
  * All data is publicly available and not considered sensitive.

### 1.3 Investigative Questions

1. What were the top 5 most effective offensive lines in the NHL for the 2022 - 2023 regular season?

2. What was the most physical defensive pair for each team in the NHL in the 2022-2023 season?

### 2. Approach
* In order to design solution to both questions, I needed to start by implementing a helper method to read and organize
  the data from the .csv file so that I could manipulate it further for the purpose of both primary methods. I did so by
  creating the `organize_by_lines()` method, which reads in the data and organizes it into list of dictionaries, with
  each dictionary representing a single line/pair and its associated statistics. Steps:
  * read in the data from the .csv
  * construct the list of dictionaries with only the statistics needed to answer the questions (primary methods)
  * calculate the weighted average of GF/GA and add to the dictionaries in the list
* Developer: Joshua LaBelle

#### Question #1
* Primary Developer: Joshua LaBelle
* The design process for this question was to take the now organized data created by `organize_by_lines()` and filter
  and sort the data, and finally return a dictionary with keys rank 1 through 5, and values as a tuple of line name and
  that lines weighted average of `goals for divided by goals against`. Here are the design steps:
  * filter for only offensive lines and 30+ games played
  * sort in descending order by weighted average
  * create the dictionary with the top 5 lines based on highest weighted average


#### Question #2
* Primary Developer: Joshua LaBelle
* The design process for this question was to take the organized list of dictionaries created by `organize_by_lines()`
  and filter the data, create the dictionary, and use the accumulator pattern to hold and update the dictionary with the 
  pair on each team with the most # of hits. Here are the design steps:
  * Filter for only defensive pairs
  * Add key value pairs to dictionary using a for loop, with key team and values tuple of pair name and # of hits.
  * Update the dictionary value of an entry for a team if # of hits is greater than the current value (within the for 
    loop)


### 3. Testing
I created three test cases, one to test the helper method and one for each primary method that answers the questions
above. Each test uses a different subset of the main data file with 1-entry, 5-entry, and 10-entry files. These ensure
that the data is processed correctly - with the correct output in the correct format. 

#### test_organize_by_line()
* Developer: Joshua LaBelle
* Tests the helper method that reads in the data and organizes it into a list of dictionaries.
* Input: data_1.csv
* Expected Results: List of dictionaries with one single dictionary. Only the specific statistics name, games played,
  team, position, hits for, goals for, and goals against.
* In order to get the results in a different way, Excel can be used to filter and parse the data to check each 
  statistic.
* Filename: test_organize_by_line.py

#### test_most_effective_offensive_lines()
* Developer: Joshua LaBelle
* Tests the primary method answering Question #1
* Input: data_5.csv
* Expected Results: a dictionary with two entries for rank 1 and 2. The pairs and lines with less than 30 games are
  filtered out. Key is rank (int) Value is a tuple of line name (str) and weighted average (float).
* In order to get the results in a different way, Excel can be used to filter and parse the data to check each 
  statistic.
* Filename: test_most_effective_offensive_lines.py

#### test_most_physical_defensive_pair
* Developer: Joshua LaBelle
* Tests the primary method answering Question #2
* Input: data_10.csv
* Expected results: a dictionary with 4 entries. Offensive lines are filtered out and only shows the pair for each team
  with the highest hitsFor statistic. Key is team name (str) and values tuple of pair name (str) and number of hits
  (float).
* In order to get the results in a different way, Excel can be used to filter and parse the data to check each 
  statistic.
* Filename: test_most_physical_defensive_pair.py


### 4. Results and Discussion
* The results show exactly what I need to answer both questions, and in a format that is easily digestible.
* The results have shown me which lines are the top five most effective (from a goals for vs goals against standpoint)
  in the NHL for the most recent season, and which defensive pair were the most physical (measured by highest # of hits)
  for each team.
  * For the first method, I was not surprised by any of these results, and was happy to see that one of the top lines 
    from the Boston Bruins (my favorite NHL team) is ranked #2 in most effective lines. 
  * For defensive pairs, I was surprised to see the hits of the New York Rangers (the Trouba pair) to have 591.0. 
    Compared to everyone else, this seems off the charts. I might question to what standard the hitsFor statistic is
    being measured by the stats-keepers at the NYR stadium.
    * It is interesting to see which teams have the heaviest hitters, and compare that to my knowledge of the team as
      either a big, powerful team or a more speed, finesse team. Most of my opinions lined up with these results.


### 5. Reflection
#### 5.1 Challenges
* The most challenging part of this project was figuring out how to return the ranking (top 5) lines in the first primary
  method and how to accrue and add to the dictionary the pair with the greatest hitsFor in the second primary method. By
  experimenting with some functions and methods that were covered in the class reading, I was gain some experience with
  new tools, which really helped me to grow as a developer and solve more complex problems. 
* Particularly, the _Sorted function_ and _tuple unpacking_ were very helpful in working through these challenges. 
  I also figured out how to use lambda functions with the sorted method to be able to sort by a specific statistic, which was really helpful in the
  first primary method.

#### 5.2 Successes
* Overall, the whole project went really well for me and I learned a lot by grinding through and figuring out how to make
  it all work as I wanted. I gained more familiarization using list comprehension in order to filter for only the 
  statistics that I needed. Even as a single person project, I made myself use branch techniques that would be used with
  collaborative development in order to get that experience, and in doing so, I figured out how to automate the project
  boards when you create a pull merge request from a branch (not main).

#### 5.3 Lessons Learned
* The number one thing here is that you need to challenge yourself, I already new this, so this is more of an affirmation.
  The reason I enjoyed and learned so much from this project was because I chose some challenging, specific questions to 
  solve. When I thought up these questions, I didn't know how I would answer them, but working through them was very
  rewarding. 

* Second is to simplify as much as possible. Take a problem and break it into segments and solve each piece one at a
  time. Test (locally) that each piece is producing the result you want using print statements, and then move to the
  next when you are satisfied. You can always refactor later.

* Lastly, in the future, I hope to learn more and gain some practice with Try/Except for exception and error handling.



