import sqlite3
import os

username = os.getlogin()

# this needs to be dynamic
cookies_filepath = f'/Users/{username}/Library/Application Support/Firefox/Profiles/ok2znsrl.default-release/cookies.sqlite'

rows = None

try:
    conn = sqlite3.connect(cookies_filepath)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM moz_cookies WHERE host LIKE '%bamboohr%'")
    rows = cursor.fetchall()
except sqlite3.OperationalError as e:
    if "database is locked" in str(e):
        print("Database locked. Close Firefox then try again.")
        exit(1)


if rows is None:
    print("No cookies for bamboohr found. Are you sure you're logged signed in?")
    exit(1)

# proceed with rest of processing
bamboohr_directory_url = ""
