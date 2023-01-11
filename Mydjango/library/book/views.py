from django.shortcuts import render

# Create your views here.
from django.shortcuts import View

class HomeView(View):

    def get(self,requset,*args,**kwargs):
        return render(requset,"home.html")

class SingUp(View):

    def get(self,requset,*args,**kwargs):
        return render(requset,"register.html")