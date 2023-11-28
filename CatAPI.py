import requests
import json

class CatFactsAPI:
    def __init__(self):
        # Cat Facts API endpoint
        self.api_url = "https://catfact.ninja/breeds"

    def get_nth_cat_breed(self, n):
        response = requests.get(self.api_url)
        data = response.json()
        if 1 <= n <= len(data['data']):
            nth_breed = data['data'][n - 1]['breed']
            return nth_breed
        else:
            # the f is for formatting th string that is being returned
            return f"Invalid value for n. It should be between 1 and {len(data['data'])}."

# Example usage:
cat_api = CatFactsAPI()
n = 3  # Replace with the desired value of n

nth_cat_breed = cat_api.get_nth_cat_breed(n)
print(f"The {n}th cat breed is: {nth_cat_breed}")
