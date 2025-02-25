from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products




class ProductCreateApiView(APIView):
    def post(self,request):
        print (request.data)
        product=Products(product_name=request.data.get('product_name'),product_qty=request.data.get('product_qty'),email=request.data.get('email'))
        print(product)
        product.save()
        return Response({"message":"api called"},status=201)