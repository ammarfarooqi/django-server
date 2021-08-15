from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import include, path

urlpatterns = [
    # connect the app urls to the project main app
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', lambda request:HttpResponse("hello world"+request.method))

]
