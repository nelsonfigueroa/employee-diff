# employee-diff

Get a diff of employees from a BambooHR directory. See who comes and goes whether leadership stays silent about it or not 👀

## Running:

**At this time, this only works with Firefox**

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

Run this periodically, then compare results with `diff` or a similar tool. For example:

```shell
diff employees-2026-01-20.txt employees-2026-01-27.txt
```
