n enumerate(urls):
        wiki_extractor = Extractor(url,attributes = ['img',
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
                                                         'pages', 'isbn', 'preceded_by', 'preceded_url', 'followed_by', 'followed_url', 'film', 'film_url'])
        regEx = r'(?:\d{1,2}[-/th|st|nd|rd\s]*)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?[a-z\s,.]*(?:\d{1,2}[-/th|st|nd|rd)\s,]*)+(?:\d{2,4})+'

        
        if wiki_extractor.data.get("publication_date"):
            date = re.match(regEx, wiki_extractor.data.get("publication_date"))
            if date:
                
                wiki_extractor.data["publication_date"] = date[0]
        b = Book(**wiki_extractor.data)
        try:
            b.save()
        except:
            print(wiki_extractor.data.