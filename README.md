# employee-diff

Get a diff of employees from a BambooHR directory. See who comes and goes whether leadership stays silent about it or not 👀

## Running:

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

Install firefox via Playwright:
```
playwright install firefox
```

Run the script, passing in your company's BambooHR subdomain:
```
python3 main.py -s mycompany
```

The script will output a textfile with results in the format `employees-YYYY-MM-DD.txt`.

Run this periodically, then compare results with `diff` or a similar tool. For example:

```shell
diff employees-2026-01-20.txt employees-2026-01-27.txt
```
