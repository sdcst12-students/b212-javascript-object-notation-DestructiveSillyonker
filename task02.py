#!python3
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests


req = requests.get('http://sdcaf.hungrybeagle.com/menu.php')

if req.status_code == 200:
    try:
        data = req.json()

        if 'menu' in data:
            weekly_menu = data['menu']
            for day_data in weekly_menu:
                print("=" * 30)
                print(f"Menu for {day_data['dayname']}")
                print("-" * 30)
                print(f"Soup: {day_data['soup']}")
                print(f"Short Order: {day_data['shortorder']}")
                print(f"Entree: {day_data['entree']}")
                print(f"Notes: {day_data['notes']}")
                print("=" * 30)
        else:
            print("No menu data found.")
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
else:
    print(f"Failed to retrieve data. HTTP Status Code: {req.status_code}")


# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains
