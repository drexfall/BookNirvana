def wikify(s):
    if s:
        return s.replace("./", "https://en.wikipedia.org/w/rest.php/v1/page/")


urls = [
    "https://en.wikipedia.org/w/rest.php/v1/page/Harry_Potter_and_the_Philosopher's_Stone/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Harry_Potter_and_the_Chamber_of_Secrets/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Harry_Potter_and_the_Prisoner_of_Azkaban/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Harry_Potter_and_the_Goblet_of_Fire/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Harry_Potter_and_the_Order_of_the_Phoenix/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Harry_Potter_and_the_Half-Blood_Prince/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Harry_Potter_and_the_Deathly_Hallows/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Twilight_(Meyer_novel)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/New_Moon_(novel)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Eclipse_(Meyer_novel)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Breaking_Dawn/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Life_and_Death:_Twilight_Reimagined/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Midnight_Sun_(Meyer_novel)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Hunger_Games_(novel)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Catching_Fire/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Mockingjay/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Ballad_of_Songbirds_and_Snakes/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Fifty_Shades_of_Grey/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Fifty_Shades_Darker/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Fifty_Shades_Freed/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Grey:_Fifty_Shades_of_Grey_as_Told_by_Christian/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Darker:_Fifty_Shades_Darker_as_Told_by_Christian/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Freed:_Fifty_Shades_Freed_as_Told_by_Christian/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Pretty_Little_Liars/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Flawless/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Perfect/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Unbelievable/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Wicked/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Killer/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Heartless/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Wanted/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Twisted/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Ruthless/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Stunning/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Burned/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Crushed/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Deadly/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Toxic/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Vicious/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Pretty_Little_Secrets/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pretty_Little_Liars_(book_series)#Ali's_Pretty_Little_Lies/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries_(novel)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_II:_Princess_in_the_Spotlight/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_III:_Princess_in_Love/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_IV:_Princess_in_Waiting/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_IV_and_1/2:_Project_Princess/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_V:_Princess_in_Pink/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_VI:_Princess_in_Training/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_VI_and_1/2:_The_Princess_Present/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_VII:_Party_Princess/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_VII_and_1/2:_Sweet_Sixteen_Princess/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_VII_and_3/4:_Valentine_Princess/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_VIII:_Princess_on_the_Brink/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_IX:_Princess_Mia/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_X:_Forever_Princess/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Princess_Diaries,_Volume_XI:_Royal_Wedding/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid_(book)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_Rodrick_Rules/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_The_Last_Straw/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_Dog_Days_(novel)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_The_Ugly_Truth/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_Cabin_Fever/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_The_Third_Wheel/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_Hard_Luck/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_The_Long_Haul/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_Old_School/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_Double_Down/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_The_Getaway/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_The_Meltdown/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_Wrecking_Ball/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_The_Deep_End/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_Big_Shot/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Diary_of_a_Wimpy_Kid:_Diper_%C3%96verl%C3%B6de/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Geronimo_Stilton/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Tintin_in_the_Land_of_the_Soviets/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Tintin_in_the_Congo/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Tintin_in_America/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Cigars_of_the_Pharaoh/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Blue_Lotus/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Broken_Ear/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Black_Island/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/King_Ottokar'_Sceptre/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Crab_with_the_Golden_Claws/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Shooting_Star/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Secret_of_the_Unicorn/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Red_Rackham'_Treasure/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Seven_Crystal_Balls/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Prisoners_of_the_Sun/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Land_of_Black_Gold/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Destination_Moon_(comics)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Explorers_on_the_Moon/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Calculus_Affair/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Red_Sea_Sharks/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Tintin_in_Tibet/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Castafiore_Emerald/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Flight_714_to_Sydney/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Tintin_and_the_Picaros/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Tintin_and_Alph-Art/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/A_Game_of_Thrones/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/A_Clash_of_Kings/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/A_Storm_of_Swords/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/A_Feast_for_Crows/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/A_Dance_with_Dragons/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Lord_of_the_Rings/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Lion,_the_Witch_and_the_Wardrobe/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Prince_Caspian/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Voyage_of_the_Dawn_Treader/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Silver_Chair/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Horse_and_His_Boy/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Magician'_Nephew/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Last_Battle/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Eleanor_%26_Park/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Fangirl_(novel)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Carry_On_(novel)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Wayward_Son_(novel)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Attachments_(novel)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Landline_(novel)/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Don_Quixote/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Alice%27s_Adventures_in_Wonderland/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Adventures_of_Huckleberry_Finn/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Adventures_of_Tom_Sawyer/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Treasure_Island/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Pride_and_Prejudice/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Wuthering_Heights /html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Jane_Eyre/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Moby-Dick/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Scarlet_Letter/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Gulliver%27s_Travels/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/The_Pilgrim%27s_Progress/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/A_Christmas_Carol/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/David_Copperfield/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/A_Tale_of_Two_Cities/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Little_Women/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Great_Expectations/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Frankenstein/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Oliver_Twist/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Uncle_Tom%27s_Cabin/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Crime_and_Punishment/html",
    "https://en.wikipedia.org/w/rest.php/v1/page/Madame_Bovary/html",

]
