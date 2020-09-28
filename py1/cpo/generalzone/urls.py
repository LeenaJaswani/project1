from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^about',views.about,name='about'),
    url(r'^registration',views.registration,name='registration'),
    url(r'^login',views.login,name='login'),
    url(r'^enquiry',views.enquiry,name='enquiry'),
    url(r'^saveenquiry',views.saveenquiry,name='saveenquiry'),
    url(r'^custreg',views.custreg,name='custreg'),
    url(r'^validateuser',views.validateuser,name='validateuser'),

]