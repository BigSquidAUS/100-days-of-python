# COULD NOT COMPLETE EXERCISE: BILLBOARD.COM NOW HAS PAYWALL FOR ARCHIVED CHARTS :(

import requests
chart_date = input("What year do you want to travel to?\n(Format: YYYY-MM-DD)\n")

url = f"https://www.billboard.com/charts/hot-100/{chart_date}/"
print(url)

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0'}
r = requests.get(url, headers=headers)

