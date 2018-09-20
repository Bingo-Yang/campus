# coding=utf-8

def sess(request):
    name = request.session['uname']
    return {'name':name}
