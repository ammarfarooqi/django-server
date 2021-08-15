
from django.contrib import admin

from .models import Question, Memant, Choice

admin.site.register([Question, Memant, Choice])
# Register your models here.
