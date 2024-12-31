import requests

SESSION_COOKIE = "53616c7465645f5fcc1be70354bceaa995118049e8ef8c80adabee5fcda9f971ac3c463508895852fa8bbb433a656ace413820cbd4047df00ff5e690fce93bd5"


def fetch_aoc_input(day, year, session_cookie=SESSION_COOKIE, raw_string=False):
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

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        if raw_string:
            return response.text
        else:
            input_lines = response.text.strip().split("\n")
            return input_lines
    else:
        raise Exception(
            f"Failed to fetch input: {response.status_code} {response.reason}"
        )
