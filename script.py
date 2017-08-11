
import json
import sqlite3
from decimal import *

conn = sqlite3.connect('/home/arjunsingh/practice/fynd/backend/core.db.sqlite3')
c = conn.cursor()


"""
Finding out the different types of genre and storing them in database
"""


# with open('imdb_data.json') as data_file:    
#     data = json.load(data_file)

# genre = []    
# for i in data:
#     for j in i['genre']:
#         genre.append(j.strip())



# index = 1
# for i in set(genre):
#     c.execute("insert into movie_genre values ({}, '{}')".format(index, i))
#     index += 1
# conn.commit()



"""
Adding all movies
"""

genres_database = {
    'Musical':1,
    'Talk-Show':2,
    'Biography':3,
    'Crime':4,
    'Sport':5,
    'Horror':6,
    'Family':7,
    'Film-Noir':8,
    'Thriller':9,
    'Western':10,
    'Adult':11,
    'Fantasy':12,
    'History':13,
    'War':14,
    'Documentary':15,
    'Romance':16,
    'Animation':17,
    'Mystery':18,
    'Drama':19,
    'Adventure':20,
    'News':21,
    'Action':22,
    'Comedy':23,
    'Music':24,
    'Game-Show':25,
    'Short':26,
    'Reality-TV':27,
    'Sci-Fi':28
}

with open('imdb_data.json') as data_file:    
    data = json.load(data_file)

index = 1
manyfieldid = 1
for i in data:
    c.execute("insert into movie_movie (id, name, popularity, director, imdbScore)  values ({}, '{}', '{}', '{}', '{}')".format(index, i['name'], Decimal(i['99popularity']), i['director'], Decimal(i['imdb_score'])))
    for j in i['genre']:
        c.execute("insert into movie_movie_genre (id, movie_id, genre_id) values ({}, {}, {})".format(manyfieldid, index, genres_database[j.strip()]))
        manyfieldid += 1
    index += 1


#c.execute("insert into movie_movie (id, name, popularity, director, imdbScore) values ({}, '{}', {}, '{}', {})".format(1, 'A', Decimal(83.3), 'AD', Decimal(8.3)))


conn.commit()

