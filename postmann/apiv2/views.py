from rest_framework.response import Response
from .models import UsersAPI
from rest_framework.views import APIView
from .serializers import UserApiSerializer
from django.shortcuts import get_object_or_404

class UserApiView(APIView):
    def get(self,request):

        queryset=UsersAPI.objects.filter(email=request.data.get('email'))
        if queryset:
            if queryset.values('password').first()['password']==request.data.get('password'):
                return Response("You are successfully login")
            else:
                return Response("Password id incorrect")
        else:
             return Response("User is not register")

    def post(self,request):
        queryset=request.data

        serializer=UserApiSerializer(data=queryset)
        if serializer.is_valid(raise_exception=True):
            save_data=serializer.save()
        return Response("User Saved")

    def put(self,request,pk):
        queryset=get_object_or_404(UsersAPI.objects.all(),pk=pk)
        parsed_data=request.data
        serializer=UserApiSerializer(instance=queryset,data=parsed_data,partial=True)

        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()
        return Response({"Success":"User '{}' updated successfully".format(save_data.name)})

    def delete (self,request, pk):
        queryset=get_object_or_404(UsersAPI.objects.all(), pk=pk)
        queryset.delete()
        return Response({"Success" : "User with id '{}' deleted successfully".format(pk)})










