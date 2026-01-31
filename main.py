import argparse
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
import json

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--subdomain", required=True, help="Specify company subdomain")
args = parser.parse_args()

bamboo_subdomain = args.subdomain
full_url = f'https://{bamboo_subdomain}.bamboohr.com/api/v1_1/employees/directory?page=1&limit=10000'

print(f'Getting employees from {full_url}')

with sync_playwright() as p:
    browser = p.firefox.launch_persistent_context(
        user_data_dir="./firefox_session",
        headless=False  # need to see the browser to be able to log in
    )
    page = browser.new_page()
    page.goto(full_url)

    # prompt user log in via Google SSO in the browser that pops up
    # then press enter
    input("Log in through the browser that popped up, then press enter after you've logged in.")

    # get page data
    page.goto(full_url)
    content = page.content()

    browser.close()

    # there's some HTML we need to get rid of. The JSON is in between these HTML tags.
    soup = BeautifulSoup(content, "html.parser")
    data = soup.get_text() # get only JSON text within HTML tags
    data = json.loads(data) # convert string to JSON

    # parse the data and get employees
    employees_list = []

    for employee in data['employees']:
        full_name = f'{employee["displayFirstName"]} {employee["lastName"]}'
        employees_list.append(full_name)

    employees_list.sort()

    # write each employee to a textfile with the format employees-YYYY-MM-DD.txt
    today = datetime.today().strftime('%Y-%m-%d')
    output_file = f'employees-{today}.txt'
    with open(output_file, "w") as f:
      for employee in employees_list:
          f.write(employee)
          f.write("\n")

    print(f'{len(employees_list)} employees written to {output_file}')
