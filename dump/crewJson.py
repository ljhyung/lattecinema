import json
from msvcrt import open_osfhandle
from pprint import pprint
import requests


# def mk_crew():
#     BASE_URL = 'https://api.themoviedb.org/3'
#     a = 0
#     params = {
#         'api_key': 'a9af69151c5a9c137a2d271958c89e3f',
#         # 'region': 'KR',
#         'language': 'ko'
#     }
#     crew = []
#     index = 1547
#     while len(crew) < 5:
#         path2 = f'/movie/{index}/credits'
#         crew_response = requests.get(BASE_URL+path2, params=params)
        
#         crew_data = crew_response.json()
#         if crew_data != {'success': False, 'status_code': 34, 'status_message': 'The resource you requested could not be found.'}:
            
#             crew_obj = {
#                 "id":crew_data['id'],
#                 # 'Director':crew_data['crew']['job']
#                 'Director':[],
#                 'Actor':[]
#             }
#             if len(crew_data['cast']) < 9:
#                 for dic in crew_data['cast']:
#                     crew_obj['Actor'].append(dic)
#             else:
#                 for i in range(9):
#                     crew_obj['Actor'].append(crew_data['cast'][i])
            
#             for dic in crew_data['crew']:
#                 if dic['job'] == "Director":
#                     crew_obj['Director'] = dic
#                     break
            
#             crew.append(crew_obj)
            
#         index += 1
        
#     with open('crew.json', 'w', encoding='utf-8') as make_files:
#         json.dump(crew, make_files, ensure_ascii=False, indent="\t")
#     return 1

# 장르 가져오기
# def mk_gan_json():
#     gen = []
#     BASE_URL = 'https://api.themoviedb.org/3'
#     a = 0
#     params = {
#         'api_key': 'a9af69151c5a9c137a2d271958c89e3f',
#         # 'region': 'KR',
#         'language': 'ko'
#     }
#     path = f'/genre/movie/list'
#     response = requests.get(BASE_URL+path, params=params)
#     data = response.json()
#     gen.append(data)
    
#     with open('gen.json', 'w', encoding='utf-8') as make_files:
#         json.dump(gen, make_files, ensure_ascii=False, indent="\t")



def mk_movie_json():
    BASE_URL = 'https://api.themoviedb.org/3'
    a = 0
    params = {
        'api_key': 'a9af69151c5a9c137a2d271958c89e3f',
        # 'region': 'KR',
        'language': 'ko'
    }
    movies = []
    crew = []
    index = 628
    pk_id = 1
    while len(crew) < 500:
        # path = f'/movie/{index}'
        # response = requests.get(BASE_URL+path, params=params)
        
        path2 = f'/movie/{index}/credits'
        crew_response = requests.get(BASE_URL+path2, params=params)
        
        #print(response.status_code, response.url)
        # data = response.json()
        crew_data = crew_response.json()
        # print(type(data))
        if crew_data != {'success': False, 'status_code': 34, 'status_message': 'The resource you requested could not be found.'}:
            print(f'인덱스:{index}, 데이터개수:{len(crew)}')
            # movie_obj_sub = {
            #     "adult":data['adult'],
            #     "backdrop_path":data["backdrop_path"],
            #     "genres":[g['id'] for g in data["genres"]],
            #     "id":data['id'],
            #     "original_language":data['original_language'],
            #     "original_title":data['original_title'],
            #     "overview":data['overview'],
            #     "popularity":data['popularity'],
            #     "poster_path":data['poster_path'],
            #     "release_date":data['release_date'],
            #     "runtime":data['runtime'],
            #     "tagline":data['tagline'],
            #     "title":data['title'],
            #     "vote_average":data['vote_average'],
            #     "vote_count":data['vote_count'],
            # }
            # movie_obj = {
            #     "model": "movies.Movie",
            #     "pk": pk_id,
            #     "fields": movie_obj_sub
            # }
            
            
            # movies.append(movie_obj)
            
            # crew_obj = {
            # }
            crew_sub_obj = {
                "id":crew_data['id'],
                # 'Director':crew_data['crew']['job']
                'Director':[],
                'Actor':[]
            }
            if len(crew_data['cast']) < 9:
                for dic in crew_data['cast']:
                    crew_sub_obj['Actor'].append(dic)
            else:
                for i in range(9):
                    crew_sub_obj['Actor'].append(crew_data['cast'][i])
            
            for dic in crew_data['crew']:
                if dic['job'] == "Director":
                    crew_sub_obj['Director'] = dic
                    break
            crew_obj = {
                "model": "movies.Crew",
                "pk": pk_id,
                "fields": crew_sub_obj
            }

            
            crew.append(crew_obj)
            
            
            pk_id += 1
            
        index += 1

    # with open('movies.json', 'w', encoding='utf-8') as make_files:
    #     json.dump(movies, make_files, ensure_ascii=False, indent="\t")
    
    with open('crew2.json', 'w', encoding='utf-8') as make_files:
        json.dump(crew, make_files, ensure_ascii=False, indent="\t")
    
    return 1

def mk_trailers_json():
    BASE_URL = 'https://api.themoviedb.org/3'
    a = 0
    params = {
        'api_key': 'a9af69151c5a9c137a2d271958c89e3f',
        # 'region': 'KR',
        'language': 'ko'
    }
    trailers = []
    index = 3
    pk_id = 1
<<<<<<< Updated upstream
    while len(trailers) < 500:
=======
    while len(trailers) < 10:
>>>>>>> Stashed changes
        path = f'/movie/{index}/videos'
        response = requests.get(BASE_URL+path, params=params)
        # print(response)
        # print(response.status_code, response.url)
        data = response.json()
        # print(data)
        # print(type(data))
        if data != {"success": False, "status_code": 34, "status_message": "The resource you requested could not be found."} and data["results"]:
            print(f'인덱스:{index}, 데이터개수:{len(trailers)}')
            # print(data["results"][0]['name'])
            movieId = data["id"]
            data = data["results"][0]
            trailer_obj_sub = {
                "trailer_id":data['id'],
                "movie_id": movieId,
                "iso_639_1":data['iso_639_1'],
                "iso_3166_1":data["iso_3166_1"],
                "name":data["name"],
                "key":data['key'],
                "site":data['site'],
                "size":data['size'],
                "type":data['type'],
                "official":data['official'],
                "published_at":data['published_at'],
                
            }
            trailer_obj = {
                "model": "movies.trailers",
                "pk": pk_id,
                "fields": trailer_obj_sub
            }
            
            
            trailers.append(trailer_obj)
            
           
            
            
            pk_id += 1
            
        index += 1

    with open('trailers2.json', 'w', encoding='utf-8') as make_files:
        json.dump(trailers, make_files, ensure_ascii=False, indent="\t")
    
    return 1

mk_movie_json()
# mk_trailers_json()
# mk_gan_json()
# mk_crew()