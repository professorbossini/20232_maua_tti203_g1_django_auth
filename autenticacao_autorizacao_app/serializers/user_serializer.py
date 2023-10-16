from django.contrib.auth.models import User
from rest_framework import serializers
import re

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  def validate_username(self, username):
    return username

  def validate_password(self, password):
    if not re.search('[A-Z]',password):
      raise serializers.ValidationError('Pelo menos uma letra maiúscula')
    if not re.search('[a-z]', password):
      raise serializers.ValidationError('Pelo menos uma letra minúscula')
    if not re.search('\\d', password): #[0-9]
      raise serializers.ValidationError('Pelo menos um dígito')
    if not re.search('[^A-Za-z0-9]', password):
      raise serializers.ValidationError("Pelo menos um caractere especial")
    if len(password) < 8:
      raise serializers.ValidationError("Comprimento pelo menos 8")
    return password

    

  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'password']
