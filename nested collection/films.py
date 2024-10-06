movies=[

    {
        "title": "Bad Asses on the Bayou",
        "year": 2015,
        "cast": [
            "Danny Trejo",
            "Danny Glover",
            "John Amos",
            "Loni Love"
        ],
        "genres": [
            "Action"
        ]
    },
    {
        "title": "Chappie",
        "year": 2015,
        "cast": [
            "Sharlto Copley",
            "Dev Patel",
            "Watkin Tudor Jones",
            "Yolandi Visser"
        ],
        "genres": [
            "Science Fiction"
        ]
    },
    {
        "title": "Road Hard",
        "year": 2015,
        "cast": [
            "Adam Carolla",
            "David Koechner",
            "Diane Farr",
            "Jay Mohr",
            "David Alan Grier"
        ],
        "genres": [
            "Comedy"
        ]
    },
    {
        "title": "The Second Best Exotic Marigold Hotel",
        "year": 2015,
        "cast": [
            "Judi Dench",
            "Maggie Smith",
            "Bill Nighy"
        ],
        "genres": [
            "Comedy",
            "Drama"
        ]
    },
    {
        "title": "Unfinished Business",
        "year": 2015,
        "cast": [
            "Vince Vaughn",
            "Dave Franco",
            "Sienna Miller",
            "Nick Frost"
        ],
        "genres": [
            "Comedy"
        ]
    },
    {
        "title": "Cinderella",
        "year": 2015,
        "cast": [
            "Lily James",
            "Richard Madden",
            "Cate Blanchett",
            "Helena Bonham Carter",
            "Holliday Grainger"
        ],
        "genres": [
            "Romance"
        ]
    },
    {
        "title": "The Cobbler",
        "year": 2015,
        "cast": [
            "Adam Sandler",
            "Dustin Hoffman",
            "Dan Stevens",
            "Steve Buscemi"
        ],
        "genres": [
            "Comedy",
            "Drama"
        ]
    },
    {
        "title": "Cymbeline",
        "year": 2015,
        "cast": [
            "Ed Harris",
            "Milla Jovovich",
            "Ethan Hawke",
            "John Leguizamo"
        ],
        "genres": [
            "Crime"
        ]
    },
    {
        "title": "Home Sweet Hell",
        "year": 2015,
        "cast": [
            "Patrick Wilson",
            "Katherine Heigl",
            "Jordana Brewster",
            "Jim Belushi"
        ],
        "genres": [
            "Comedy"
        ]
    },
    {
        "title": "It Follows",
        "year": 2015,
        "cast": [
            "Maika Monroe",
            "Keir Gilchrist",
            "Jake Weary",
            "Daniel Zovatto"
        ],
        "genres": [
            "Horror"
        ]
    }
]

# q1 total number of movies

print(len(movies))

# q2 print all movie title

all_movie_title=[m.get("title") for m in movies]
print (all_movie_title)

# q3 comedy movies

comedy_movies=[m.get("title") for m in movies if "Comedy" in m.get("genres")]
print(comedy_movies)

# q4 cast

film_cast=[m.get("cast") for m in movies if m.get ("title")=="Home Sweet Hell"]
print(film_cast)

# q5 comedy drama movies

comedy_drama_movies=[m.get("title") for m in movies if "Comedy" and "Drama" in m.get("genres")]
print(comedy_drama_movies)

# q6 comedy or drama movies

comedy_or_drama=[m.get("title") for m in movies if "Comedy" in m.get("genres") or "Drama" in m.get("genres")]
print(comedy_or_drama)

# q7 actors who is casted 

actors=[]

for m in movies:
      for a in m.get("cast"):
        actors.append(a)

print(actors)        