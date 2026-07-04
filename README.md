# employee-diff

Get a diff of employees from a BambooHR directory. See who comes and goes whether leadership stays silent about it or not 👀

## Running:

**At this time, this only works with Firefox**, so you'll need Firefox installed on your machine. 

Create a Python virtual environment:
```
python3 -m venv venv
```

Activate the virtual environment:
```
source venv/bin/activate
```

Install dependencies:
```
pip3 install -r requirements.txt
```

Run the script, passing in your company's BambooHR subdomain:
```
python3 main.py -s mycompany
```

A browser window will pop up, prompting you to log in. After logging in, press enter. Your session will be saved locally so you don't need to enter your credentials every time you want to run this script.

The script will output a textfile with results in the format `employees-YYYY-MM-DD.txt`.

If older snapshots (textfiles) exist, it will do a diff. For example:

```diff
2025-12-31 -> 2026-04-03
- John
+ David
2026-04-03 -> 2026-06-23
+ James
2026-06-23 -> 2026-07-02
- James
+ Suzy
2026-07-02 -> 2026-07-03
- Alice
- David
- Suzy
+ Brian
+ Stephanie
+ Oscar
+ Jen
```
