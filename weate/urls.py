from django.conf.urls import url,include

from .views import index,QuestionApi,latest
from rest_framework import routers
router = routers.DefaultRouter()
router.register('question',QuestionApi)
urlpatterns = [
    url(r'^latest/',latest,name="latest"),
    url(r'^stack/',include(router.urls)),
    url(r'',index,name="index"),
]
urlpatterns += [
 url(r'^stack/',include(router.urls)),   
]
