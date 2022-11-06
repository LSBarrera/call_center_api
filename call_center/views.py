import json
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, renderer_classes, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework.views import exception_handler
from call_center.models import Orden


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username=username)     
    except User.DoesNotExist:
        response = {
            'error':True,
            'mensaje':'Usuario o contraseña incorrectos.'
        }
        return Response(response)

    pwd_valid = check_password(password,user.password)

    if not pwd_valid:
        response = {
            'error':True,
            'mensaje':'Usuario o contraseña incorrectos.'
        }
        return Response(response)

    token,created = Token.objects.get_or_create(user=user)

    response = {
        'error':False,
        'username':user.username,
        'token':token.key
    }

    return Response(response)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def insertar(request):
    id_order = request.POST.get('id_order')
    empleado = request.POST.get('empleado')
    cliente = request.POST.get('cliente')
    descuento = request.POST.get('descuento')
    impuesto = request.POST.get('impuesto')
    propina = request.POST.get('propina')
    valor_extra = request.POST.get('valor_extra')
    nit = request.POST.get('nit')
    direccion = request.POST.get('direccion')
    detalles = request.POST.get('detalles')
    sucursal = request.POST.get('sucursal')

    try:
        orden = Orden()
        orden.id_order = id_order
        orden.empleado = empleado
        orden.cliente = cliente
        orden.descuento = descuento
        orden.impuesto = impuesto
        orden.propina = propina
        orden.valor_extra = valor_extra
        orden.nit = nit
        orden.direccion = direccion
        orden.detalles = detalles
        orden.sucursal = sucursal
        orden.save()

        response = {
            'error':False,
            'detail':''
        }

    except Exception as error:
        response = {
            'error':True,
            'detail':str(error)
        }

    return Response(response)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def ordenes(request):
    try:
        sucursal = request.POST.get('sucursal')

        #user = User.objects.get(username=username)
        ordenes = Orden.objects.filter(sucursal=sucursal,recibido=False)

        arr_ordenes = []

        for o in ordenes:
            arr = {
                'Id':o.id,
                'IdOrder':o.id_order,
                'Empleado':o.empleado,
                'Cliente':o.cliente,
                'Descuento':o.descuento,
                'Impuesto':o.impuesto,
                'Propina':o.propina,
                'ValorExtra':o.valor_extra,
                'Nit':o.nit,
                'Direccion':o.direccion,
                'Detalles':o.detalles
            }
            arr_ordenes.append(arr)

        response = {
            'error':False,
            'ordenes':arr_ordenes
        }

    except Exception as error:
        response = {
            'error':True,
            'detail':str(error)
        }

    return Response(response)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def recibido(request):

    try:
        id = request.POST.get('id')
        orden = Orden.objects.get(id=id)
        orden.recibido = True
        orden.fecha_recibido = datetime.now()
        orden.save()
        response = {
            'error':False,
            'detail':''
        } 

    except Exception as error:
        response = {
            'error':True,
            'detail':str(error)
        } 

    return Response(response)

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        response.data['error'] = True

    return response
