import statistics
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario
from .serlializers import UsuarioSerializer
from api import serlializers
from rest_framework import status

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_usuarios': '/',
		'Search by Region': '/?region=region_name',
		'Search by CentroFormacion': '/?centroFormacion=centroFormacion_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/user/pk/delete'
	}

	return Response(api_urls)

@api_view(['POST'])
def add_users(request):
    user = UsuarioSerializer(data=request.data)
  
    # validating for already existing data
    if Usuario.objects.filter(**request.data).exists():
        raise serlializers.ValidationError('This data already exists')
  
    if user.is_valid():
        user.save()
        return Response(user.data)
    else:
        return Response(status=statistics.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_users(request):
    # checking for the parameters from the URL
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)

    # if there is something in items else raise error
    if usuarios:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_users(request, pk):
	user = Usuario.objects.get(pk=pk)
	data = UsuarioSerializer(instance=user, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_usuarios(request, pk):
	user = get_object_or_404(Usuario, pk=pk)
	user.delete()
	return Response(status=status.HTTP_202_ACCEPTED)
