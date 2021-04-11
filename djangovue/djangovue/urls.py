from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render

vue_urls = [
  path('', lambda request: HttpResponse(render(request, 'vue_index.html'))),
  path('another-path/', lambda request: HttpResponse(render(request, 'vue_index.html'))),
]

urlpatterns = [
  # the admin panel
  path('admin/', admin.site.urls),
  # the api/notes
  path('api/', include('notes.urls')),
  # the vue hello world page
  path('', include(vue_urls)),
]
