from django.shortcuts import render
import requests
from homepage.forms import SearchForm
from decouple import config
# Create your views here.


API_KEY = config('API_KEY')


def home(req):
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

                all_results.append(item)
            return render(req, "homepage.html", {"form": form, "all_results": all_results})

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
