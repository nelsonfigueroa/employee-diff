import argparse
import fetch
import diff

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--subdomain", required=True, help="Specify company subdomain")
args = parser.parse_args()

bamboo_subdomain = args.subdomain

fetch.fetch_employees(bamboo_subdomain)
diff.diff_employees()
