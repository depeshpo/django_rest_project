from rest_framework.response import Response
from rest_framework.views import APIView


class CheckAppStatus(APIView):
    def get(self, request):
        return Response({
            "message": "Test successful"
        })
