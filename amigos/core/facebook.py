import requests, json

GRAPH_URL = "http://graph.facebook.com/"
ACCESS_TOKEN_FIELD = "access_token="

def get_user_info(token):
    requisition = requests.get(GRAPH_URL + "me?" + ACCESS_TOKEN_FIELD + token)
    user_info = json.loads(requisition)
    return user_info

def get_movies(token):
    requisition = requests.get(GRAPH_URL + "me/movies?" + ACCESS_TOKEN_FIELD + token)
    movies = json.loads(requisition)
    return movies

def get_books(token):
    requisition = requests.get(GRAPH_URL + "me/books?" + ACCESS_TOKEN_FIELD + token)
    books = json.loads(requisition)
    return books

def get_television(token):
    requisition = requests.get(GRAPH_URL + "me/television?" + ACCESS_TOKEN_FIELD + token)
    television = json.loads(requisition)
    return television