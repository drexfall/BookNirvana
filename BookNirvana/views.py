from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
import requests
from .wiki_urls import urls
from .wikipedia import Extractor
from .models import Book,Shelf,User
import time
import re
import random
import string
# Create your views here.


def index(request):

    return render(request, "home.html")


def search(request):
    data = {}
    if request.method == "POST":
        result = []
        search_query = request.POST["search"]
        for x in Book.objects.all():
            temp = {}
            if search_query.lower() in (x.title+x.series+x.author).lower():

                temp = {"img": x.img,
                        "title": x.title,
                        "author": x.author,
                        "id": x.id}

                result.append(temp)

        data.update({"result": result})

    return render(request, "search.html", {"data": data})


def info(request, id):
    obj = Book.objects.get(id=id)
    data = obj.__dict__

    del data["_state"]
    c = 1
    for x in Book.objects.all():
        c += 1

    return render(request, "info.html", {"data": data})

@login_required
def add_to_list(request,book_id):
    return redirect('info',book_id)

@login_required
def like_book(request,book_id):
    return redirect('info',book_id)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            # return redirect('login')
    else:
        form = UserCreationForm()
    print(form.get_context())
    return render(request, 'registration/index.html', {'form': form, 'type': 'register'})


def login_(request):
    context =  {'type': 'login'}
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
        else:
            context.update({"error":True})
    else:
        form = AuthenticationForm()

    context.update({"form":form})
    print(form.get_context())
    return render(request, 'registration/index.html', context)

@login_required
def profile(request):
    print(User.objects.all())
    return render(request, "profile.html", {"user": request.user})


def save(request):
    for index, url in enumerate(urls):
        temp = {}
        r = requests.get(url)

        soup = BeautifulSoup(r.content, features="html.parser")
        row = soup.find(attrs={"class": "infobox vcard"})
        if row:
            rows = row.tbody.find_all("tr", recursive=False)

            for row in rows:
                temp.update({"title": row.td.text})
                if (row.th and row.td):
                    key = row.th.text.replace("\u00a0", " ")
                    value = row.td.text.replace("\u00a0", " ")
                    if key == "Preceded by":
                        url = wikify(row.td.a["href"])
                        temp |= {"preceded_url": url}
                    if key == "Followed by":
                        url = wikify(row.td.a["href"])
                        temp |= {"followed_url": url}
                    if key == "Publication date":
                        value = "2002-02-11"
                    temp |= {key.lower().replace(" ", "_"): value}

        film = soup.find(id="Film_adaptation")
        if not film:
            film = soup.find(id="Film_adaptation")

        if film:
            film = film.parent
            temp.update({
                "film": film.a['title'].replace(" (film)", ""),
                "film_url": wikify(film.a['href'])
            })

        b = Book(**temp)
        b.save()


def add_book(request):
    for index, url in enumerate(urls):
        wiki_extractor = Extractor(url, attributes=['img',
                                                    'title',
                                                    'author',
                                                    'illustrator',
                                                    'country',
                                                    'language',
                                                    'series',
                                                    'release_number',
                                                    'genre',
                                                    'set_in',
                                                    'publisher',
                                                    'publication_date',
                                                    'pages',
                                                    'isbn',
                                                    'preceded_by',
                                                    'preceded_url',
                                                    'followed_by',
                                                    'followed_url',
                                                    'film',
                                                    'film_url'])
        regEx = r'(?:\d{1,2}[-/th|st|nd|rd\s]*)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?[a-z\s,.]*(?:\d{1,2}[-/th|st|nd|rd)\s,]*)+(?:\d{2,4})+'

        if wiki_extractor.data.get("publication_date"):
            date = re.match(regEx, wiki_extractor.data.get("publication_date"))
            if date:

                wiki_extractor.data["publication_date"] = date[0]
        try:
            if not Book.objects.filter(title=wiki_extractor.data["title"]).exists():
                b = Book(**wiki_extractor.data)
                b.save()
        except:
            print(wiki_extractor.data.get("title"))
        # print(wiki_extractor.data["title"],index)
