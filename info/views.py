from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import UserData

# Create your views here.
def index(request):
    return HttpResponse("/admin/ => 관리자페이지")

def Question(request):
    if request.method == 'POST':
        post = UserData() 
        post.Userid = request.POST['Userid'] 
        post.UserTemp = request.POST['UserTemp']
        post.UserHumid = request.POST['UserHumid']
        post.Philipshuetoken = request.POST['Philipshuetoken']
        post.Smartthingstoken = request.POST['Smartthingstoken']
        post.Userlocation = request.POST['Userlocation']
        post.save() # 데이터베이스 안에 저장 
        # return redirect('Question') 
        return render(request,'info/index.html')

    else:
        post = UserData.objects.all()    
        return render(request,'info/index.html')            
