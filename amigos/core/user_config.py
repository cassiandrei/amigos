from core import facebook
from accounts.models import User

def checkUser(token):
    name = facebook.get_user_info()['name']
    email = facebook.get_user_info()['email']

    users = User.objects.all()
    result = users.filter(token=token)
    if(result):
        #Se existe, atualiza
        result.name = name
    else:
        #Se nao, cria novo
        new_user = User.objects.create(name=name,email=email)
        new_user.save()