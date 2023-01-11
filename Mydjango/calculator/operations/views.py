from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class AdditionView(APIView):
    def post(self,request,args,*kwargs):
        print("addition")
        print(request.data)
        n1=int(request.data.get("num1"))
        n2=int(request.data.get("num2"))
        res=n1+n2
        return Response(data=res)

class cubeview(APIView):
    def post(self,request,args,*kwargs):
        n=int(request.data.get("num"))
        res=n**3
        return Response(data=res)

class primeview(APIView):
    def post(self,request,args,*kwargs):
        num=int(request.data.get("num"))
        isPrime=True
        for i in range(2,num):
            if(num%i==0):
                isprime=False
                break
        return Response(data=isPrime)

class subview(APIView):
    def post(self,request,args,*kwargs):
        print("subtraction")
        a1 = int(request.data.get("num3"))
        a2 = int(request.data.get("num4"))
        result = a1 - a2
        return Response(data=result)
class mulview(APIView):
    def post(self,request,args,*kwargs):
        print("multiplication")
        b1 = int(request.data.get("num5"))
        b2 = int(request.data.get("num6"))
        resultt = b1 * b2
        return Response(data=resultt)

class divview(APIView):
    def post(self,request,args,*kwargs):
        print("division")
        c1 = int(request.data.get("num7"))
        c2 = int(request.data.get("num8"))
        resulttt = c1 / c2
        return Response(data=resulttt)

# Create your views here.