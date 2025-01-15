import requests
from pathlib import Path

SESSION_COOKIE = (
    "53616c7465645f5fcc1be70354bceaa995118049e8ef8c80adabee5fcda9f971ac3c463508895852fa8bbb433a656ace413820cbd4047df00ff5e690fce93bd5"
)
INPUT_CACHE_DIR = "/Users/sarcar/PycharmProjects/Aoc24/InputData"

def fetch_aoc_input(day, year, session_cookie=SESSION_COOKIE, raw_string=False, force_remote_pull = False):
    """
    Fetches the Advent of Code input for the specified day and year.

    Args:
        day (int): The day of the Advent of Code challenge (e.g., 1 for Day 1).
        year (int): The year of the Advent of Code challenge (e.g., 2024).
        session_cookie (str): The session cookie obtained from your Advent of Code account.

    Returns:
        str: The content of the input file.
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "Cookie": f"session={session_cookie}",
        "User-Agent": "Python Fetcher for Advent of Code (your_email@example.com)",
        # Replace with your email for politeness
    }

    filename = f"{INPUT_CACHE_DIR}/aoc{year}_{day}.txt"
    filepath = Path(filename)
    cached = True # assume the file exists
    if not filepath.is_file() or force_remote_pull:
        cached = False

    if not cached:
        # Download from the AoC website and store in a  file
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(filename,"w") as f:
                f.write(response.text)
        else:
            raise Exception(f"Failed to fetch input: {response.status_code} {response.reason}")

    #Always return data from the file
    with open(filename,"r") as f:
        buffer = f.read()
        if raw_string:
            return response.text
        else:
            input_lines = buffer.strip().split("\n")
            return input_lines

