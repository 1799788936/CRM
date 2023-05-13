from rest_framework import serializers
from rbac.models import Permission, Role, UserInfo


from rest_framework.exceptions import ErrorDetail, ValidationError

from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.serializers import empty, as_serializer_error



class PermissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Permission
        fields = ["permission", "id", "title"]


class RoleSerializers(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ["role_name", "id", "permission_id"]
    


class UserInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserInfo
        fields = ["user_name", "id", "role_id"]