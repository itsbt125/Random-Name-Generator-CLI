I've provided a decent list of names (first and last) in a folder within the repository.

Usage:
generator.py --> defaults to the provided name files in repo (lists/first_names.txt, lists/surnames.txt)
generator.py -f (--first) "user_provided_line_seperated_first_names.txt" --> only outputs a random first name from the file you specified
generator.py -l (--last,-s,--surname) "user_provided_line_seperated_last_names.txt" --> only outputs a random last name from the file you specified
generator.py -f -"user_provided_line_seperated_first_names.txt" -l "user_provided_line_seperated_last_names.txt" --> only outputs a random name in the format of {first, last} to your console from your custom line seperated file

Feel free to make an issue if the docs don't make sense to you.
