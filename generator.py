import random
import os
import argparse
import sys

def load_names(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def generate_name(first_names_file, last_names_file):
    first_names = load_names(first_names_file)
    last_names = load_names(last_names_file)

    if not first_names or not last_names:
        raise ValueError("One of the provided files is empty.")

    first = random.choice(first_names).rstrip(",")
    last = random.choice(last_names).rstrip(",")
    return f"{first} {last}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a random name from text files.") # Initializes argument parser

    parser.add_argument(
        "-f", "--first", 
        type=str, 
        default="lists/first_names.txt", 
        help="Path to the first names text file"
    )
    parser.add_argument(
        "-l", "--last", 
        type=str, 
        default="lists/surnames.txt", 
        help="Path to the surnames text file"
    )
    args = parser.parse_args()
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        print(generate_name(args.first, args.last))
    except FileNotFoundError as e:
        print(f"Error: The file '{e.filename}' was not found, make sure your file path is correct.")
    except Exception as e:
        print(f"An error occurred: {e}")
