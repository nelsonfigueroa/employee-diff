import browser_cookie3
import requests

cookiejar = browser_cookie3.firefox(domain_name='bamboohr')

bamboohr_directory_url = ""
resp = requests.get(bamboohr_directory_url, cookies=cookiejar)
print(resp.content)
