import random
import os
import argparse
import sys

# Default file paths assume you've cloned the repo.
DEFAULT_FIRST_PATH = "first_names.txt" 
DEFAULT_LAST_PATH = "surnames.txt"

def load_names(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def generate_name(first_names_file=None, last_names_file=None):
    """
    Generates a name based on which file paths are provided.
    If a path is None, that part of the name is skipped.
    """
    name_parts = []

    if first_names_file:
        first_names = load_names(first_names_file)
        if not first_names:
            raise ValueError(f"File {first_names_file} is empty.")
        name_parts.append(random.choice(first_names).rstrip(","))

    if last_names_file:
        last_names = load_names(last_names_file)
        if not last_names:
            raise ValueError(f"File {last_names_file} is empty.")
        name_parts.append(random.choice(last_names).rstrip(","))

    if not name_parts:
        return "No name generated (no files provided)."

    return " ".join(name_parts)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a random name from text files.")

    parser.add_argument(
        "-f", "--first", 
        type=str, 
        default=None, 
        help="Path to the first names text file."
    )
    parser.add_argument(
        "-l", "--last","-s","--surname",
        type=str, 
        default=None, 
        help="Path to the last names (surnames) text file"
    )
    
    args = parser.parse_args()
    target_first = args.first
    target_last = args.last
    if target_first is None and target_last is None:
        target_first = DEFAULT_FIRST_PATH
        target_last = DEFAULT_LAST_PATH
    
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        result = generate_name(target_first, target_last)
        print(result)
    except FileNotFoundError as e:
        print(f"Error: The file '{e.filename}' was not found. Please check your path.")
    except Exception as e:
        print(f"An error occurred: {e}")
