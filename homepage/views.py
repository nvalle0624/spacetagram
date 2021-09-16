from django.shortcuts import render
import requests
from homepage.forms import SearchForm, LikeForm
from homepage.models import Favorites

from decouple import config
# Create your views here.


API_KEY = config('API_KEY')


def home(req):
    all_favorites = Favorites.objects.all()
    favorites_urls = []
    for u in all_favorites:
        favorites_urls.append(u.image_url)
    print("favs:")
    print(favorites_urls)

    def handleLike():
        print("test passed")
    if req.method == "POST":
        form = SearchForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            search_query = data["search_query"]
            search_query = str(search_query)
            res = requests.get(
                f'https://images-api.nasa.gov/search?q={search_query}&media_type=image')
            all_results = []
            res = res.json()["collection"]['items']
            for item in res:
                href = item['links'][0]['href']
                isFavorite = ''
                if(href in favorites_urls):
                    print(href)
                    print("match!")
                    isFavorite = ' favorite'

                all_results.append([item, isFavorite])
            likeForm = LikeForm()
            return render(req, "homepage.html", {"form": form, "all_results": all_results, 'likeForm': likeForm})

    form = SearchForm()
    return render(req, "homepage.html", {"form": form})


# def search(req, search_query=None):
#     if search_query:
#         if req.method == "POST":
#             form = SearchForm(req.GET)
#             if form.is_valid():
#                 data = form.cleaned_data
#                 search_query = data['search_query']
#                 response = request.urlopen(
#                     f'https://images-api.nasa.gov/search?q={search_query}api_key={API_KEY}')
#                 all_results = []
#                 for item in response:
#                     all_results.append(item)
#                 print(response)
#                 return render(req, "homepage.html", {"all_results": all_results, "response": response}, args=[search_query])
#     else:
#         form = SearchForm()
#         return render(req, "homepage.html", )


def favorites(request):
    return render(request, "favorites.html")
