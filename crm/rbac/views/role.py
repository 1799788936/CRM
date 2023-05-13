from django.shortcuts import render, HttpResponse
# from rest_framework import serializers
from rest_framework.views import APIView, Response
from rbac.models import Role
from rbac.serializers import RoleSerializers

# Create your views here.



# class RoleSerializers(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # role_name = serializers.CharField(max_length=32)
    # # permission_id =serializers.

    # class Meta:
    #     model = Role
    #     fields = ["role_name", "id", "permission_id"]
    
    # def create(self, validated_data):
    #     new_role = Role.objects.create(**self.validated_data)
    #     return new_role

    # def update(self, instance, validated_data):
    #     # print(self.instance.id)
    #     update_role = Role.objects.filter(id=self.instance.id).update(**self.validated_data)
    #     update_role = Role.objects.get(id=self.instance.id)
    #     return update_role




class RoleView(APIView):

    # queryset = Role.objects.all()
    # serializer_class = RoleSerializers

    def get(self, request):
        role_list = Role.objects.all()
        serializer = RoleSerializers(instance=Role.objects.all(), many=True)
        return Response(serializer.data)


    def post(self, request):
        serializers = RoleSerializers(data=request.data)
        # print(request.data)
        if serializers.is_valid():
            res = serializers.save()
            # print(serializers.instance)
            return Response(serializers.data)
        else:
            # print("qqq")
            return Response(serializers.errors)


    def put(self, request):
        # print(request.data["id"])
        role_update = Role.objects.get(id=request.data["id"])
        # print(role_update)
        serializers = RoleSerializers(data=request.data, instance=role_update)
        # serializers.save()
        # return Response(serializers.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)


    # def delete(self, request, **kwargs):
    #     print(kwargs)
        # print(request.Get)
        # Role.objects.get(id=id).delete()
        # return Response()
    
class RoleViewPk(APIView):

    def delete(self, request, pk):
        # pk = request.query_params.get("pk","")
        Role.objects.get(id=pk).delete()
        return Response()
    
    def get(self, request, pk):
        # pk = request.query_params.get("pk","")
        # print(pk)
        serializer = RoleSerializers(instance=Role.objects.get(id=pk))
        return Response(serializer.data)

    
# class RoleViewToPermission(APIView):
    

