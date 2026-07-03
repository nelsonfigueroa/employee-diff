import json
import os
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def fetch_employees(bamboo_subdomain):
    full_url = f'https://{bamboo_subdomain}.bamboohr.com/api/v1_1/employees/directory?page=1&limit=10000'

    print(f'Getting employees from {full_url}')

    # set up Firefox profile for session/cookie persistence
    profile_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "firefox_session")
    os.makedirs(profile_path, exist_ok=True)

    options = webdriver.FirefoxOptions()
    options.add_argument("-profile")
    options.add_argument(profile_path)
    options.set_preference("devtools.jsonview.enabled", False)  # disable pretty JSON viewer to get raw JSON

    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )

    try:
        driver.get(full_url)

        # prompt user log in via Google SSO in the browser that pops up
        # then press enter
        input("Log in through the browser that popped up, then press enter after you've logged in.")

        # get page data
        driver.get(full_url)
        content = driver.page_source

    finally:
        driver.quit()

    # there's some HTML we need to get rid of. The JSON is in between these HTML tags.
    soup = BeautifulSoup(content, "html.parser")
    data = soup.get_text()  # get only JSON text within HTML tags
    data = json.loads(data)

    # parse the data and get employees
    employees_list = []

    for employee in data['employees']:
        full_name = f'{employee["displayFirstName"]} {employee["lastName"]}'
        employees_list.append(full_name)

    employees_list.sort()

    # write each employee to a textfile with the format employees-YYYY-MM-DD.txt
    today = datetime.today().strftime('%Y-%m-%d')
    output_file = f'snapshots/employees-{today}.txt'
    with open(output_file, "w") as f:
        for employee in employees_list:
            f.write(employee)
            f.write("\n")

    print(f'{len(employees_list)} employees written to {output_file}')
