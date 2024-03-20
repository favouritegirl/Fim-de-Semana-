from .models import consumidor, Endereco
from rest_framework import viewsets, status
from datetime import datetime
from .serializers import ConsumidorSerializer , EnderecoSerializer, EmailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.db.models import Q
import requests
import random
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import HttpResponse

#Página de Cadastro
class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = ConsumidorSerializer(data=request.data)
        serializer.is_valid(raise_exception="True")
        serializer.save()
        return Response(serializer.data)

#Página de Login
class LoginUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        telefone = request.data.get('telefone')
        cpf = request.data.get('cpf')
        user = consumidor.objects.filter(email=email, telefone=telefone).first()

        if user is None:
            return Response({'error': 'Credenciais inválidas'}, status=400)
        
        
        user_data = ConsumidorSerializer(user).data
   

        return Response(user_data, status=200)
    
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    #informações pessoais cadastradas
    def get(self, request, id):
        if request.user.id != id:
            return Response({"error": "Você não tem permissão para ver essas informações."}, status=status.HTTP_403_FORBIDDEN)

        user = get_object_or_404(consumidor, id=id)
        serializer = ConsumidorSerializer(user)
        return Response(serializer.data)

    #Editar informações pessoais
    def put(self, request, id):
        if request.user.id != id:
            return Response({"error": "Você não tem permissão para ver essas informações."}, status=status.HTTP_403_FORBIDDEN)
        
        user = get_object_or_404(consumidor, id=id)
        serializer = ConsumidorSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class SendEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Verifica se os dados recebidos são para envio de e-mail
        if 'assunto' in request.data and 'mensagem' in request.data and 'remetente' in request.data and 'destinatarios' in request.data:
            assunto = request.data['assunto']
            mensagem = request.data['mensagem']
            remetente = request.data['remetente']
            destinatarios = request.data['destinatarios']

            # Envia o e-mail
            send_mail(
                assunto,
                mensagem,
                remetente,
                destinatarios,
                fail_silently=False,
            )

            # Retorna uma resposta JSON
            return Response({'status': 'E-mail enviado com sucesso!'})
        else:
            return Response({'error': 'Dados incompletos para envio de e-mail'}, status=400)
    