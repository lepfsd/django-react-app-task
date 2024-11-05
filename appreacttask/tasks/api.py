import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TaskApiView(APIView):
   
    def get(self, request):
        try:
            response = requests.get('https://dummyjson.com/products')
            response.raise_for_status()
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)