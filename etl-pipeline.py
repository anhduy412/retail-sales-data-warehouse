import pandas as pd
import requests
import config

#Extract
api_key = config.api_key
url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=coronavirus&api-key={api_key}'
r  = requests.get(url)

response_list = []

api_key = config.api_key

for movie_id in range(550, 560):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    r = requests.get(url)
    response_list.append(r.json())

df = pd.DataFrame.from_dict(response_list)

#Transform
df_columns = ['budget', 'genre', 'id', 'imdb_id' , 'original_title', 'release_date', 'revenue', 'runtime', 'title', 'vote_average', 'vote_count']

genre_list = df['genres'].tolist()
flat_list = [item for sublist in genre_list for item in sublist]

result = []
for l in genre_list:
    r = [d['name'] for d in l]
    result.append(r)
df = df.assign(genre_all = result)
df_genre = pd.DataFrame.from_records(flat_list).drop_duplicates()

df_columns = ['budget', 'id', 'imdb_id' , 'original_title', 'release_date', 'revenue', 'runtime', 'title', 'vote_average', 'vote_count']
df_genre_columns = df_genre['name'].tolist()
df_columns.extend(df_genre_columns)

s = df['genre_all'].explode()
df = df.join(pd.crosstab(s.index, s))

df['release_date'] = pd.to_datetime(df['release_date'])
df['day'] = df['release_date'].dt.day
df['month'] = df['release_date'].dt.month
df['year'] = df['release_date'].dt.year
df['day_of_week'] = df['release_date'].dt.day_name()
df_time_columns = ['id', 'release_date', 'day', 'month', 'year', 'day_of_week']

#load
df[df_columns].to_csv('tmdb_movies.csv', index=False)
df_genre.to_csv('tmdb_genres.csv', index=False)
df[df_time_columns].to_csv('tmdb_datetimes.csv', index=False)