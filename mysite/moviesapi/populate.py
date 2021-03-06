# collect movie names in a list
text = open(r'the_journal_movies.txt', 'r').read().split('\n')

# file to store names that don't have data
f = open(r'error_movies.txt', 'a')

# requesting website for information on movies
import json, re, urllib, time, http.client

# set up django to get database populated
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviesapi.settings')
django.setup()

# import required models

from .models import movie, genre, director, actor




# set up fixed headers, varicables and meta data
conn = http.client.HTTPSConnection("api.themoviedb.org")
poster_path = "https://image.tmdb.org/t/p/w640"
payload = "{}"

credit = "/3/movie/{}/credits?api_key=a0cda0670d10a1f96ea56ac1d70c5067"
film = "/3/search/movie?include_adult=false&page=1&query={}&language=en-US&api_key=a0cda0670d10a1f96ea56ac1d70c5067"

# genres dictionary
genre_dict = {'37': u'Western', '10402': u'Music', '12': u'Adventure', '14': u'Fantasy',\
              '878': u'Science Fiction', '16': u'Animation', '18': u'Drama', '28': u'Action',\
              '36': u'History', '35': u'Comedy', '99': u'Documentary', '10770': u'TV Movie',\
              '27': u'Horror', '9648': u'Mystery', '10749': u'Romance', '10751': u'Family',\
              '80': u'Crime', '53': u'Thriller', '10752': u'War'}

def get_info_and_store(name):
    name = re.sub(r"\s+", "%20", name)
    conn.request("GET", film.format(name), payload)
    res = conn.getresponse()
    data = json.loads(res.read())

    if not data['total_results']:
        print("Could not find",name)
        f.write(name+'\n')
        f.flush()
    else:
        data_1 = data['results'][0]

        #populating movie database
        if movie.objects.filter(name=data_1['title']):
            object1 = movie.objects.filter(name=data_1['title'])[0]
        else:
            if data_1['poster_path']:
                object1 = movie(name=data_1['title'],
                                release=data_1['release_date'],
                                poster=str(poster_path+data_1['poster_path']))
            else:
                object1 = movie(name=data_1['title'],
                                release=data_1['release_date'])
            object1.save()
        print ("stored:", data_1['title'])
        movie_id = data_1['id']

        # populating genre database
        for j in data_1['genre_ids']:
            if genre.objects.filter(name=genre_dict[str(j)]):
                object4 = genre.objects.filter(name=genre_dict[str(j)])[0]
                object4.movie_name.add(object1)
            else:
                object4 = genre(name=genre_dict[str(j)])
                object4.save()
                object4.movie_name.add(object1)

        # getting movie credits to store actors and cast
        conn.request("GET", credit.format(movie_id), payload)
        res = conn.getresponse()
        data = json.loads(res.read())

        # populating director database
        for k in data['crew']:
            if k['job'] == "Director":
                if director.objects.filter(name=k['name']):
                    object2 = director.objects.filter(name=k['name'])[0]
                    object2.movie_name.add(object1)
                    break
                else:
                    object2 = director(name=k['name'])
                    object2.save()
                    object2.movie_name.add(object1)
                    break

        # populating actors database with only first seven or less actors
        if len(data['cast']) < 7:
            cast_range = len(data['cast'])
        else:
            cast_range = 7

        for m in range(0,cast_range):
            if actor.objects.filter(name=data['cast'][m]['name']):
                object3 = actor.objects.filter(name=data['cast'][m]['name'])[0]
                object3.movie_name.add(object1)
            else:
                object3 = actor(name=data['cast'][m]['name'])
                object3.save()
                object3.movie_name.add(object1)


count = 444
for i in range(count, len(text)):
    print(i),
    get_info_and_store(text[i])