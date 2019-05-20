from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index, name='index'),
   # path('page2',views.page2, name='page2'),
   # path('page3',views.page3, name='page3'),
    path('',views.accueil, name='accueil'),

    path('article/<int:id>',views.lire, name='lire'),
    path('contact/',views.contact, name='contact'),
]

