import requests, json

GRAPH_URL = "https://graph.facebook.com/"
ACCESS_TOKEN_FIELD = "?access_token="
CLIENT_ID = "1625366447519489"
CLIENT_SECRET = "d94c27f2b5cf98b53a4b53488ace6161"
SCOPE = "public_profile,email,user_about_me,user_actions.books,user_actions.music,user_actions.video,user_birthday,user_friends,user_likes"

def url_to_login(url):
    return "https://www.facebook.com/dialog/oauth?client_id={client_id}&redirect_uri={url}&scope={scope}".format(
        client_id = CLIENT_ID, 
        url = url, 
        scope = SCOPE
    )

def get_token(url, code):
    requisition = requests.get("https://graph.facebook.com/oauth/access_token?client_id={client_id}&redirect_uri={url}&client_secret={client_secret}&code={code}".format(
        client_id = CLIENT_ID,
        url = url,
        client_secret = CLIENT_SECRET,
        code = code
    ))
    return json.loads(requisition.text)

def get_user_info(token):
    requisition = requests.get(GRAPH_URL + "me" + ACCESS_TOKEN_FIELD + token + "&fields=name,email,gender,cover,link")
    user_info = json.loads(requisition.text)
    user_info["cover"] = user_info["cover"]["source"]
    requisition = requests.get(GRAPH_URL + "me/picture" + ACCESS_TOKEN_FIELD + token + "&width=250&redirect=false")
    picture_info = json.loads(requisition.text)
    user_info["picture"] = picture_info['data']["url"]
    return user_info

def get_likes(token, items):
    """
    Itens possiveis: movies, games, television, music, books
    """
    if items not in ("movies", "games", "television", "music", "books"):
        return None
    full_list = []
    url = GRAPH_URL + "me/" + items + ACCESS_TOKEN_FIELD + token
    while url is not None:
        requisition = requests.get(url).text
        partial_list = json.loads(requisition)
        full_list += partial_list['data']
        if partial_list.get("paging") and partial_list["paging"].get("next"):
            url = partial_list["paging"]["next"]
        else:
            url = None
    return full_list

def get_page_picture(token, page_id):
    url = GRAPH_URL + page_id + "/picture" + ACCESS_TOKEN_FIELD + token
    requisition = requests.get(url).text
    return json.loads(requisition)["data"]["url"]