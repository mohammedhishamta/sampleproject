from django.shortcuts import render

# Create your views here.
from  rest_framework.views import APIView
from  rest_framework.response import Response

class Productsview(APIView):
    def get(self,requset,*args,**kw):
        return Response(data="list all products")
    def post(self,requset,*args,**kw):
        return Response(data="creating a products")

class ProductsdatailsView(APIView):
    def get(self,requset,*args,**kw):
        return  Response(data="detail of a products")
    def put(self,requset,*args,**kw):
        return Response(data="updating a products")
    def delete(self,requset,*args,**kw):
        return Response(data="delete a object")
