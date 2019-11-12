from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
from .forms import Weatherform
from .models import City,Question
from .serializers import QuestionSerializer

from rest_framework import viewsets
# import requests
import json
from bs4 import BeautifulSoup
def index(request):
    if request.method == 'POST':
        form = Weatherform(request.POST)
        # form.save()
        if form.is_valid():
            name = form.cleaned_data['city']
            forms = City(name=name)
            forms.save()
            print(forms)
        url = 'https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'
        cities = City.objects.all()
        weather_data = []
        for city in cities:
            r = requests.get(url.format(city)).json()
            city_weather = {
                'city': city.name,
                'temprature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)
        # city = 'kericho
        
        print(weather_data)
        context = {
            "city_weather":city_weather,
            "form": form
        }
        return render(request,'index.html',context)
    else:
        form = Weatherform()
    return render(request,'index.html',{"form":form})

class QuestionApi(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def latest(request):
    try:
        res = requests.get('https://stackoverflow.com/questions')
        soup = BeautifulSoup(res.text,"html.parser")
        questions = soup.select('.question-summary')

        for question in questions:
            q = question.select_one('.question-hyperlink').getText()
            vote_count = question.select_one('.vote-count-post').getText()
            views = question.select_one('.views').attrs['title']
            tags = [i.getText() for i in (question.select('.post-tag'))]

            questionz = Question()
            questionz.question = q
            questionz.vote_count = vote_count
            questionz.views = views
            questionz.tags = tags

            questionz.save()
        return HttpResponse("latest data fettched from stack")
    except e as Exception:
        return HttpResponse("Failed ")
