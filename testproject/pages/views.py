from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hey there! This is my first django app!!!')