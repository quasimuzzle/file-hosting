from django.shortcuts import render

from django.shortcuts import render
from .models import File, Comment, Rating

def file_list(request):
    files = File.objects.all()
    return render(request, 'files/file_list.html', {'files': files})

# Другие представления для вывода комментариев, оценок и прочего
