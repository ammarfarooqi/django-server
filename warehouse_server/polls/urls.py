from django.urls import path
from .views import MemantView
from .views import MemantDetails
from .views import GenericaView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('helloworld/', views.hmlyl, name='helloworld'),
    path('<int:question_id>/', views.detail, name='detail'),

    # importing function based views
    # path('memant/', views.Memant_list_rest),
    # path('memant/<int:pk>/', views.getOneMemant_rest)
    # class based views
    path('memant/', MemantView.as_view()),

    path('memant/<int:id>/', MemantDetails.as_view()),


    # using mixins
    path('generic/memant/<int:id>', GenericaView.as_view()),

]
