from core import facebook
from accounts.models import User, Books, Videos, Games, Musics, BookUser, MusicUser, GameUser, VideoUser

def checkUser(token):
    result = facebook.get_user_info(token)
    name = result['name']
    email = result['email']
    cover = result['cover']
    picture = result['picture']
    link = result['link']
    fb_id = result['id']

    users = User.objects.all()
    try:
        result = users.get(fb_id=fb_id)
        # Se existe, atualiza
        result.name = name
        #result.email = email
        result.token_api = token
        result.cover = cover
        result.picture = picture
        result.link = link
        result.save()
        print('usuario ja existe')
    except:
        #Se nao, cria novo
        new_user = User.objects.create(username=fb_id, name=name,email=email,token_api=token, picture=picture, cover=cover, fb_id=fb_id, link=link)
        new_user.save()
        insertBooks(token, fb_id)
        insertGames(token, fb_id)
        insertMusic(token, fb_id)
        insertVideos(token, fb_id)
        print("usuario criado")

def insertBooks(token, fb_id):
    user = User.objects.get(fb_id=fb_id)
    books = facebook.get_likes(token, 'books')
    for book in books:
        b, created = Books.objects.get_or_create(name=book['name'], id_api=book['id'])
        b.save()
        bu, created = BookUser.objects.get_or_create(user=user, book=b)
        bu.save()

def insertGames(token, fb_id):
    user = User.objects.get(fb_id=fb_id)
    games = facebook.get_likes(token, 'games')
    for game in games:
        g, created = Games.objects.get_or_create(name=game['name'], id_api=game['id'])
        g.save()
        gu, created = GameUser.objects.get_or_create(user=user, game=g)
        gu.save()

def insertMusic(token, fb_id):
    user = User.objects.get(fb_id=fb_id)
    musics = facebook.get_likes(token, 'music')
    for music in musics:
        m, created = Musics.objects.get_or_create(name=music['name'], id_api=music['id'])
        m.save()
        mu, created = MusicUser.objects.get_or_create(user=user, music=m)
        mu.save()

def insertVideos(token, fb_id):
    user = User.objects.get(fb_id=fb_id)
    videos = facebook.get_likes(token, 'movies')
    for video in videos:
        v, created = Videos.objects.get_or_create(name=video['name'], id_api=video['id'])
        v.save()
        vu, created = VideoUser.objects.get_or_create(user=user, video=v)
        vu.save()
