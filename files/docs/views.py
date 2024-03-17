from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .models import User
from datetime import datetime
from docs.models import Contact
from django.contrib import messages


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
        files = User.objects.all()
    return render(request, 'administration/upload.html', {'form': form,'files':files})

def view_files(request):
    files = User.objects.all()
    return render(request, 'upload.html', {'files': files})

def index(request):
    context={
        "variable1":"Anshika is great.",
        "variable2":"Vishnu is her best friend."
    }
    # messages.success(request,"This is a text message.")
    return render(request,'index.html',context)
    #return HttpResponse("This is homepage.")

def about(request):
    # return HttpResponse("This is about page.")
    return render(request,'about.html')

def services(request):
    # return HttpResponse("This is services page.")
    return render(request,'services.html')

def sidebar(request):
    return render(request,'sidebar.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    
    return render(request,'contact.html')

  

