from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# detail = [
#     {
#         'name' : 'Neil',
#         'game' : 'football',
#         'country':'USA',
#         'phone':'123-45-678'
#     },
#     {
#         'name' : 'Noel',
#         'game' : 'tennis',
#         'country':'Canada',
#         'phone':'876-54-321'
#     },
#     {
#         'name' : 'Peter',
#         'game' : 'fooseball',
#         'country':'England',
#         'phone':'034-63-841'
#     },
# ]


def home(request):
    return render(request,'app1/homePage.html' )

def display(request):
    context={
        
        'details': Post.objects.all(),

    }   
    return render(request, 'app1/displayPage.html', context)


