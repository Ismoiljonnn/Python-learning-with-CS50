import sys
import requests

if len(sys.argv) < 2:
  sys.exit("Missing command-line argument")

try:
  amount = float(sys.argv[1])
except ValueError:
  sys.exit("Command-line argument is not a number")


API_KEY = "bd28508c89fb00dc86560996c08ba319e30a7562191208aa98e77b0487aca25d"

url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"


try:
  response = requests.get(url)
  data = response.json()

  price = float(data["data"]["priceUsd"])
except (requests.RequestException, KeyError, ValueError):
  sys.exit("API request failed")

total_cost = amount * price
print(f"${total_cost:,.4f}")