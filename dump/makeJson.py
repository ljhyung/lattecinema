import json
from msvcrt import open_osfhandle
from pprint import pprint
import requests

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    a = 0
    params = {
        'api_key': 'f3fabe74cb0dd74f8821476495ddee85',
        # 'region': 'KR',
        'language': 'ko'
    }
    movies = []
    index = 1
    while len(movies) < 10:
        path = f'/movie/{index}'
        response = requests.get(BASE_URL+path, params=params)
    #print(response.status_code, response.url)
        data = response.json()
        # print(type(data))
        if data != {'success': False, 'status_code': 34, 'status_message': 'The resource you requested could not be found.'}:
            md = {
                # "pk":data['id'],
                "adult":data['adult'],
                "backdrop_path":data["backdrop_path"],
                "genres":data["genres"],
                # "id":data['id'],
                "original_language":data['original_language'],
                "original_title":data['original_title'],
                "overview":data['overview'],
                "popularity":data['popularity'],
                "poster_path":data['poster_path'],
                "release_date":data['release_date'],
                "runtime":data['runtime'],
                "tagline":data['tagline'],
                "title":data['title'],
                "vote_average":data['vote_average'],
                "vote_count":data['vote_count'],
                }
            movie_obj = {
                "pk": data['id'],
                "model":"movie.movie",
                "fields": md,
            }
            movies.append(movie_obj)
        index += 1
    # for num in range(0000):
    #     path = f'/movie/{num}'
    #     response = requests.get(BASE_URL+path, params=params)
    # #print(response.status_code, response.url)
    #     data = response.json()
    #     # print(type(data))
    #     if data != {'success': False, 'status_code': 34, 'status_message': 'The resource you requested could not be found.'}:
    #         movie_obj = {
    #             "adult":data['adult'],
    #             "backdrop_path":data["backdrop_path"],
    #             "genres":[g['name'] for g in data["genres"]],
    #             "id":data['id'],
    #             "original_language":data['original_language'],
    #             "original_title":data['original_title'],
    #             "overview":data['overview'],
    #             "popularity":data['popularity'],
    #             "poster_path":data['poster_path'],
    #             "release_date":data['release_date'],
    #             "runtime":data['runtime'],
    #             "tagline":data['tagline'],
    #             "title":data['title'],
    #             "vote_average":data['vote_average'],
    #             "vote_count":data['vote_count'],
    #         }
    #         movies.append(movie_obj)
    
    # pprint(movies)
    # print(len(movies))
    # return movies
    # print(json.dumps(movies, ensure_ascii=False, id))
    
    with open('movies.json', 'w', encoding='utf-8') as make_files:
        json.dump(movies, make_files, ensure_ascii=False, indent="\t")
    return 1
        
            
            
        # return data['genres'][0]['name']
    
    
    # cnt = 0
    # return data['results']
    # for i in data['results']:
    #     cnt += 1
    # return cnt 
    # 여기에 코드를 작성합니다.  

if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """    
    print(popular_count())
    # => 20