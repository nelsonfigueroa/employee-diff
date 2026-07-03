from datetime import date
import os

db = {}

files = os.listdir("snapshots/")
textfiles = [f for f in files if f.endswith(".txt")] # get only .txt files

# only do a chronological diff if there's more than 1 file (snapshot)
if len(textfiles) > 1:
    for file in textfiles:
        without_extension = file.split(".txt")[0]
        date_only = without_extension.split("employees-")[1]

        # convert date string to date object
        d = date.fromisoformat(date_only)

        with open(f'snapshots/{file}') as f:
            employees = f.read().splitlines() # list of employee names
            # add to dictionary. date -> employees list
            db[d] = employees


    # sort by chronological order
    db = {d: db[d] for d in sorted(db)}

    # to colorize text for the diff
    GREEN = "\033[32m"
    RED   = "\033[31m"
    RESET = "\033[0m"

    curr_date = None
    prev_date = None

    curr_snapshot = None
    prev_snapshot = None

    for snapshot_date in db:
        prev_date = curr_date
        curr_date = snapshot_date

        prev_snapshot = curr_snapshot
        curr_snapshot = db[snapshot_date]

        if prev_snapshot is None:
            continue

        # now do diff with sets
        removed = set(prev_snapshot) - set(curr_snapshot)
        added   = set(curr_snapshot) - set(prev_snapshot)

        print(f'{prev_date} -> {curr_date}')
        for employee in removed:
            print(f'{RED}- {employee}{RESET}')

        for employee in added:
            print(f'{GREEN}+ {employee}{RESET}')
