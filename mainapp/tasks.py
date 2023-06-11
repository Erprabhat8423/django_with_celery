from celery import shared_task
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
from google_play_scraper import app
from .models import SpActivityLogs

@shared_task(bind=True)
def test_func(self):
    url = "https://play.google.com/store/games?hl=en&gl=US"
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the game titles using class name and tag name
    game_titles = soup.find_all('a', {'class': 'Si6A0c Gy4nib'})

    # Extract package names from game titles
    package_names = []
    for title in game_titles:
        package_name = title['href'].split('=')[1]
        package_names.append(package_name)

    # Print the package names
    game_list=[]
# sourcery skip: no-loop-in-tests
    for name in package_names:
        game_dict={}
        # Fetch the app details from Play Store using the package name
        result = app(name)
        game_dict['package_name']= name
        game_dict['app_name']= result['title']
        game_dict['developer']= result['developer']
        game_dict['Price']= result['price']
        game_dict['Rating']= result['ratings']
        game_dict['np_of_rating']= result['contentRating']
        game_dict['description']= result['description']
        game_dict['icon_url']= result['icon']
        game_dict['cover_image']= result['videoImage']
        game_list.append(game_dict)

    for game_lists in game_list:
        spactivitylogs = SpActivityLogs()
        spactivitylogs.package_name = game_lists['package_name']
        spactivitylogs.app_name = game_lists['app_name']
        spactivitylogs.developer = game_lists['developer']
        spactivitylogs.Price = game_lists['Price']
        spactivitylogs.Rating = game_lists['Rating']
        spactivitylogs.description = game_lists['description']
        spactivitylogs.icon_url = game_lists['icon_url']
        spactivitylogs.cover_image = game_lists['cover_image']
        spactivitylogs.save()
    return "Task Save"