# from rest_framework import serializers
from rbac.models import UserInfo
from rest_framework.generics import GenericAPIView
from rest_framework.views import Response
from rbac.serializers import UserInfoSerializer


# class UserInfoSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = UserInfo
#         fields = ["user_name", "id", "role_id"]

class UserInfoView(GenericAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def get(self, request):
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        # serializer.save()
        # # print(serializer.data)
        # return Response(serializer.data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

        
class UserInfoViewPk(GenericAPIView):

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    
    def get(self, request, pk):
        # print(pk)
        serializer = self.get_serializer(instance=self.get_object(), many=False)
        return Response(serializer.data)
    
    def put(self,request, pk):
        print(request.data)
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)
        # serializer.save()
        # return Response(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request, pk):
        self.get_object().delete()
        return Response()
    
