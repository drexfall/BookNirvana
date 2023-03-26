from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, hashers
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from avatar_generator import Avatar
import requests
from .wiki_urls import urls
from .wikipedia import Extractor
from .models import Book, User, Shelf, Review
from .forms import UserRegisterForm, ReviewForm, ProfileForm
import time
import re
import random
import string
import json
import datetime
# Create your views here.

# Method to generate random ID
def generate_id(model, length=3):
    # Input model to check if ID exists in database

    id = ""

    key = string.ascii_lowercase+string.digits

    for letter in range(length):
        id += random.choice(key)

    if model.objects.filter(id=id):
        id = generate_id()

    return id


def index(request):
    context = {}

    return render(request, "home.html",context)


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

        data.update({"result": result, "empty": not len(result)})
    context =  {"data": data}
    return render(request, "search.html",context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.profile_picture = "static/def_user.png"

            user.shelves = {}
            user.book_info={}
            user.social_links={}
            user._change_reason = "User registered"
            user.save()

            return redirect('login')
    else:
        form = UserRegisterForm()
    for field in form.fields:
        form.fields[field].widget.attrs.update({"placeholder": ""})
    context = {'form': form, 'type': 'register'}
    return render(request, 'registration/index.html', context)


def login_(request):
    context = {'type': 'login'}
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
        else:
            context.update({"error": True})
    else:
        form = AuthenticationForm()

    for field in form.fields:
        form.fields[field].widget.attrs.update({"placeholder": ""})
    context.update({"form": form})
    return render(request, 'registration/index.html', context)


@login_required
def profile(request):
    user_obj = User.objects.get(username=request.user.username)
    # add 3 shelves automatically after registration
    if (not len(user_obj.shelves)):
        for shelf_name in ["Currently Reading", "Want to Read", "Already Read"]:
            add_shelf(request, shelf_name)

    NUMBER_OF_SUGGESTIONS = 7
    book_list = [book.id for book in Book.objects.all()]
    suggested_book_ids = random.choices(book_list, k=NUMBER_OF_SUGGESTIONS)
    suggested = [Book.objects.get(id=id) for id in suggested_book_ids]

    context = {"data": {"shelves": user_obj.get_shelf_detail()},
               "user": user_obj, "suggested": suggested}

    return render(request, "profile.html", context)


def info(request, id):
    obj = Book.objects.get(id=id)
    data = obj.__dict__

    del data["_state"]
    c = 1
    for x in Book.objects.all():
        c += 1

    data.update({"shelves": {}})

    # reviews
    for review in obj.reviews:
        obj.reviews[review] = Review.objects.get(id=review)

    if request.user.is_authenticated:
        user_obj = User.objects.get(username=request.user.username)
        if str(user_obj.id) in obj.like_status:
            data.update({"liked": obj.like_status[str(user_obj.id)]})

        data["shelves"].update(user_obj.get_shelf_detail())
    context =  {"data": data}
    return render(request, "info.html", context)



@login_required()
def add_shelf(request, name=None):
    user_obj = User.objects.get(username=request.user.username)
    id = generate_id(Shelf)
    if (name is None):
        name = "Shelf_"+id

    shelf = Shelf(id=id, name=name, user_id=user_obj)
    shelf._change_reason = "Shelf Added"
    shelf.save()

    user_obj.shelves.update({id: []})
    user_obj._change_reason = "Shelf object added in User history"
    user_obj.save()

    if request.session.get("redirect"):
        return redirect(request.session["redirect"], request.session["args"][0], id)

    return redirect("profile")

@login_required
def delete_shelf(request, shelf_id):
    Shelf.objects.get(id=shelf_id).delete()
    user = User.objects.get(username=request.user.username)
    del user.shelves[shelf_id]
    user._change_reason = "Shelf deleted"
    user.save()
    return redirect("profile")

@login_required
def add_to_shelf(request, book_id):

    user_obj = User.objects.get(username=request.user.username)
    shelf_id = request.POST["shelf_list"]
    print(user_obj.shelves[shelf_id])
    if book_id not in user_obj.shelves[shelf_id]:
        user_obj.shelves[shelf_id].append(book_id)
        user_obj._change_reason = "Book added to shelf"
        user_obj.save()

    return redirect('info', book_id)


@login_required
def like_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user_obj = User.objects.get(username=request.user.username)
    like_status = book.like_status
    key = str(user_obj.id)

    if key in like_status:
        status = not book.like_status[key]
        book.like_status.update({key: status})
        book._change_reason = "Liked Book" if status else "Unliked Book"
    else:
        book.like_status.update({key: True})
        book._change_reason = "Liked Book"
        
    
    book.save()
    return redirect('info', book_id)


@login_required()
def add_review(request, book_id):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)

            user_obj = User.objects.get(username=request.user.username)

            obj.reviewer = user_obj
            obj._change_reason = "Review added by the user"
            obj.save()

            book = Book.objects.get(id=book_id)
            book.reviews.update({obj.id: user_obj.id})
            book._change_reason = "Review added to book"
            book.save()

            return redirect("info", book_id)
    return render(request, "reviewForm.html", {"form": form})

def settings(request):
    form = SettingsForm()
    if request.method == "POST":
        form = SettingsForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit = False)
            if Settings.objects.filter(id=request.user.id):
                set_obj = Settings.objects.get(user_id=request.user.id)
                set_obj.background = obj.background
                set_obj._change_reason = "Setting changed"
                set_obj.save()
            else:
                obj.user_id = User.objects.get(id=request.user.id)
                obj._change_reason = "Setting changed"
                obj.save()
            return redirect("profile")
    return render(request, "settings.html", {"form":form})

def edit(request):
    user = User.objects.get(username=request.user.username)
    form = ProfileForm(initial={"bio":user.bio,"profile_photo":user.profile_photo,"first_name":user.first_name,"last_name":user.last_name})

    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            user.first_name = obj.first_name
            user.last_name = obj.last_name
            user.bio = obj.bio
            user.profile_photo = obj.profile_photo
            links = user.social_links
            for website in request.POST:
                if website not in  ("csrfmiddlewaretoken","first_name","last_name","profile_photo","bio"):
                    links.update({website:request.POST[website]})
            user.social_links = links
            user._change_reason = "Profile edited"
            user.save()

            return redirect("profile")

    return render(request, "profile_edit.html", {"form":form})

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

def save_images(request):
    books = Book.objects.all()
    for book in books:
        pass