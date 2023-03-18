from models import Book
from wiki_urls import wikify,urls

for index, url in enumerate(urls):
    temp = {}
    r = requests.get(url)

    soup = BeautifulSoup(r.content, features="html.parser")
    row = soup.find(attrs={"class": "infobox vcard"})
    if row:
        rows = row.tbody.find_all("tr", recursive=False)

        for row in rows:

            if (row.th and row.td):
                key = row.th.text.replace("\u00a0", " ")
                value = row.td.text.replace("\u00a0", " ")
                if key in ["Preceded by","Followed by"]:
                    url = wikify(row.td.a["href"])
                    value = {"title":value,"url":url}
                    
                temp |= {key: value}

    film = soup.find(id="Film_adaptation")
    if not film:
        film = soup.find(id="Film_adaptation")
    
    if film:
        film = film.parent
        temp.update({
            "Film": {
                "title": film.a['title'].replace(" (film)", ""),
                "url": wikify(film.a['href'])
            }
        })
    data.update({index: temp})
    print(data)
    break
# b = Book()