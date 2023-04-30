"""
Demonstrate Lines functionality
File: src/client.py
Initial authors: Joshua LaBelle
Individual contributor: Joshua LaBelle
Date: 29 April 2023
"""
from nhl_lines import Lines


def offensive_lines_method():
    """
    Demonstrate `most_effective_offensive_lines()` instance method in Lines.
    """
    lines_obj = Lines("../data/NHL_Line_Data.csv", "../data/data_out.txt")
    lines_obj.organize_by_line()
    most_effective_lines = lines_obj.most_effective_offensive_lines()
    for rank, offensive_line in most_effective_lines.items():
        print("Rank:", rank, ' ', "Line:", offensive_line)


def defensive_pair_method():
    """
    Demonstrate `most_physical_defensive_pair()` instance method in Lines.
    """
    lines_obj = Lines("../data/NHL_Line_Data.csv", "../data/data_out.txt")
    lines_obj.organize_by_line()
    most_physical_pair = lines_obj.most_physical_defensive_pair()
    for team, defensive_pair in most_physical_pair.items():
        pair, hits = defensive_pair
        print("Team:", team, ' ', "Pair:", pair, ' ', "Number of hits:", hits)


def write_output():
    """
    Demonstrate `write_to_file()` method in Lines.
    """
    lines_obj = Lines("../data/NHL_Line_Data.csv", "../data/data_out.txt")
    lines_obj.organize_by_line()
    lines_obj.most_effective_offensive_lines()
    lines_obj.most_physical_defensive_pair()
    lines_obj.write_to_file()


def main():
    """
    Use Lines Methods.
    """
    choice = 0
    while choice != "Q":
        choice = input("Which method would you like to try? \n "
                       "'A' for offensive lines"
                       ", 'B' for defensive pairs, or 'Q' to quit: ")
        choice = choice.upper()
        if choice == "A":
            offensive_lines_method()
        elif choice == "B":
            defensive_pair_method()
        elif choice not in ("A", "B", "Q"):
            print("please enter a valid choice\n")
            continue

    choice2 = input("Would you like to test the write method?\n Enter Y if"
                    " yes or N if no: ")
    choice2 = choice2.upper()
    if choice2 == "Y":
        write_output()
        print("Check the data_out.txt file in data!\n")
    print("Thank you for trying my program!")


if __name__ == '__main__':
    main()
