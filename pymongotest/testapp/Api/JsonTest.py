from django.http import HttpResponse

import json

from bson import ObjectId

from testapp.dbtesting import User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def specific_user(request, username):
    def get():
        users = User().get_users_from_collection({'name': username})
        response = users[0]
        del response['_id']

        return HttpResponse(json.dumps(response), status=200)


    def post():
        try:
            age, job = request.POST['age'], request.POST['job']
        except:
            return HttpResponse(status=400)


        user = {
            'name': username,
            'age': age,
            'job' : job
        }

        result = User().add_user_on_collection(user)
        return HttpResponse(status=201) if result else HttpResponse(status=500)

    if request.method == 'GET':
        return get()
    elif request.method == 'POST':
        return post()
    else:
        return HttpResponse(status=405)


def all_users(request):
    def get():
        users = User().get_users_from_collection({})
        response = []
        print(users)
        for user in users:
            user['_id']=str(user['_id'])
            response.append(user)

        return HttpResponse(json.dumps(response), status=200)


    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)
