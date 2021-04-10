import json
import os
import requests
from pprint import pprint
# Add your Bing Search V7 subscription key and endpoint to your environment variables.
subscription_key = os.environ['efd7ad03f1ea41cb90b409558e2f33a6']
endpoint = os.environ['https://api.bing.microsoft.com'] + "/bing/v7.0/search"

# Query term(s) to search for.
query = "Microsoft Cognitive Services"

# Construct a request
mkt = 'en-US'
params = {'q': query, 'mkt': mkt}
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

# Call the API
print('calling the API')
try:
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()

    print("\nHeaders:\n")
    print(response.headers)

    print("\nJSON Response:\n")
    pprint(response.json())
except Exception as ex:
    raise ex
