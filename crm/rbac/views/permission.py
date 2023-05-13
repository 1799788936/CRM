from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.generics import GenericAPIView
from rbac.serializers import PermissionSerializer
# from rest_framework import serializers
from rbac.models import Permission


# class PermissionSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Permission
#         fields = ["permission", "id", "title"]



class PermissionView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class PerMissionViewPk(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
    def get(self, request, pk):
        return self.retrieve(request, pk)