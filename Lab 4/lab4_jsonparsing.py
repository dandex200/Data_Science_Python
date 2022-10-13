# JSON PARSING
import urllib.request
import json
import csv

from attr import fields

# Download JSON file from URL
URL = "http://mlg.ucd.ie/modules/COMP30760/movies.json"
response = urllib.request.urlopen(URL)
raw_json = response.read().decode()

# Parse downloaded data
movie_data = json.loads(raw_json)

# Print list of all Movie Titles from JSON File
print("\nMovie Titles & Durations: \n")
for movie in movie_data:
    print("%s : %s" % (movie['Title'], movie['Runtime']))

# Print Genre Info
print("\nMovie Genre Info: \n")
for movie in movie_data:
    genre_string = movie['Genre']
    genres = genre_string.split(',')
    print("%s = %s" % (movie["Title"], genres))

# Export Movie Data to CSV file
f_out = open("movies.csv", "w")
fields = ['Title', 'Year', 'Rated', 'Runtime',  'Genre',
          'Director',  'Actors',  'Country',  'RatingScore', 'Type']
writer = csv.DictWriter(f_out, fieldnames=fields)

writer.writeheader()

for movie in movie_data:
    writer.writerow(movie)
f_out.close()
