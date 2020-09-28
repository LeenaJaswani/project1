from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^homeuser',views.homeuser,name='homeuser'),
    url(r'^changepassword',views.changepassword,name='changepassword'),
    url(r'^complainlog',views.complainlog,name='complainlog'),
    url(r'^discussion',views.discussion,name='discussion'),
    url(r'^searchsolution',views.searchsolution,name='searchsolution'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^savecomplain',views.savecomplain,name='savecomplain'),
    url(r'^changepwd',views.changepwd,name='changepwd'),
    url(r'postquestion',views.postquestion,name='postquestion'),
    url(r'^answer/(?P<qid>\d+)$',views.answer,name='answer'),#id is getting recieved
    url(r'^postanswer',views.postanswer,name='postanswer'),
    url(r'^viewanswer/(?P<qid>\d+)$',views.viewanswer,name='viewanswer'),
    url(r'^search',views.search,name='search'),
]