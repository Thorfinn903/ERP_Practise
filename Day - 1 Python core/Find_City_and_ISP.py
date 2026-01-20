import requests

url = "http://ip-api.com/json"

try:
    response = requests.get(url)
    data = response.json()

    print(data)

    city_name = data['city']
    provider = data['org']

    print(f"Main abhi {city_name} mein baitha hoon.")
    print(f"Mera internet {provider} chala raha hai.")

except Exception as e:
    print(f"Error aa gaya: {e}")