from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .models import User

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file')
            for file in files:
                user = User.objects.create(document=file)
                user.save()
            return HttpResponse(f"The file '{user.document}' uploaded by the user {user.pk} is uploaded successfully.")
    else:
        form = UploadFileForm()
    return render(request, 'administration/upload.html', {'form': form})

def view_files(request):
    files = User.objects.all()
    return render(request, 'upload.html', {'files': files})