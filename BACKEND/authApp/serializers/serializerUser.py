from rest_framework import serializers
from authApp.models import User
from authApp.models.User import User
from authApp.models.Account import Account

from authApp.serializers.serializerAccount import SerializadorCuenta
from authApp.models import Account

from drf_writable_nested import WritableNestedModelSerializer
from setuptools.config._validate_pyproject.fastjsonschema_validations import validate

class SerializadorUsuario(WritableNestedModelSerializer, serializers.ModelSerializer):
    account = SerializadorCuenta(many = True)

    class Meta:
        model = User
        fields = ['id','username','password','name','email','account']

        def create(self, validated_data):
            accountData = validated_data.pop('account')
            userInstance = User.objects.create(**validated_data)
            Account.objects.create(user=userInstance, **accountData)
            return userInstance

        def to_representation(self, obj):
            user = User.objects.get(id=obj.id)
            account = Account.objects.get(user = obj.id)
            return {
                "id": user.id,
                "username" : user.username,
                "name": user.primerNombre,
                "email": user.email,
                "account" :{
                    "id": account.id,
                    "balance": account.balance,
                    "description": account.description
                }
            }