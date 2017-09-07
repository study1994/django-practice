# _*_ coding:utf-8 _*_
from django.shortcuts import render,HttpResponse
from choices.models import QuestionNaire
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

def quna_list(request):
    return render(request,'choices/rest_api.html',{})


class QunaSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuestionNaire
        fields =('title',)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def quna(request):
    print(request.user)
    print(request.auth)
    if request.method == 'GET':
        quna_list = QuestionNaire.objects.all()
        if request.auth:
            serializer = QunaSerializers(quna_list,many=True)
            return Response(serializer.data)
        else:
            return HttpResponse()