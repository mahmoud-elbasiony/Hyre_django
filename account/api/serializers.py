from rest_framework import serializers
from Landlord.models import Tenant
from Tenant.models import User
from django.contrib.auth.hashers import  check_password
from django.contrib.auth import authenticate


class SigninSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    class Meta:
        model = User
        fields = ['email','password']
        # extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        email=attrs.get('email')
        password=attrs.get('password')
        user=User.objects.filter(email=email).first()
        if user:
            if check_password(password, user.password):
                return user
            else:
                raise serializers.ValidationError(
                    {
                        'password': "wrong email or passowrd."
                    }
                )
        else:
            raise serializers.ValidationError(
                {
                    'email': "wrong email or passowrd."
                }
            )
        

class SignupSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','name','email','password',"password_confirm"]
        extra_kwargs = {'password': {'write_only': True}}


    def validate(self, attrs):
        print("signup validation")
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError(
                {
                    'password': "Password doesn't match"
                }
            )
        return attrs
    def save(self, **kwargs):

        user = User(
            email=self.validated_data.get('email'),
            username=self.validated_data.get('username'),
            name=self.validated_data.get('username'),
            company=self.validated_data.get('company_id'),
        )

        user.set_password(self.validated_data.get('password'))

        user.save()
    
class TenantSerializer(serializers.ModelSerializer):
    user=SignupSerializer()
    
    class Meta:
        model = Tenant
        fields = '__all__'



