from django.http import HttpResponse
from django.template import loader

from testapp.dbtesting import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def specific_user(request, username):
    def get():
        db_user_data = User().get_users_from_collection({'name': username})

        user = db_user_data[0]
        del user['_id']

        template = loader.get_template('test.html')
        return HttpResponse(template.render({'userData': [user]}, request))


    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)


def all_users(request):
    def get():
        dbUserData = User().get_users_from_collection({})

        users = []
        for user in dbUserData:
            user['u_id']=str(user['_id'])
            users.append(user)

        template = loader.get_template('test.html')
        return HttpResponse(template.render({'userData': users}, request))


    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)
