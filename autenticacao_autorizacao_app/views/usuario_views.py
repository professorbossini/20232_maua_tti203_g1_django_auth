from rest_framework import views, status
from rest_framework.response import Response
from autenticacao_autorizacao_app.serializers import UserSerializer
from django.contrib.auth.models import User
class CadastroNovoUsuarioView(views.APIView):
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      # kwargs: keywordargs
      user = User.objects.create_user(**serializer.validated_data)

  