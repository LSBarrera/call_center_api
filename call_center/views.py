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
    name = request.POST.get('name')
    Descuentopociento = request.POST.get('Descuentopociento')
    cobrarimpuesto = request.POST.get('cobrarimpuesto')
    propina = request.POST.get('propina')
    SaldoCliente = request.POST.get('SaldoCliente')
    CobrarValorExtra = request.POST.get('CobrarValorExtra')
    NombreClientePrepago = request.POST.get('NombreClientePrepago')
    CantPersonas = request.POST.get('CantPersonas')
    DescuentoEspecial = request.POST.get('DescuentoEspecial')
    DescuentoEn = request.POST.get('DescuentoEn')
    DescuentoLibre = request.POST.get('DescuentoLibre')
    DescuentoCortesia = request.POST.get('DescuentoCortesia')
    ValueNITClient = request.POST.get('ValueNITClient')
    DirClient = request.POST.get('DirClient')
    TotalSubsidio = request.POST.get('TotalSubsidio')
    QuitarSubsidio = request.POST.get('QuitarSubsidio')
    EsPorCuentaPendiente = request.POST.get('EsPorCuentaPendiente')
    TipoOrden = request.POST.get('TipoOrden')
    IDOrdenCE = request.POST.get('IDOrdenCE')
    TipoEstadoCE = request.POST.get('TipoEstadoCE')
    TotalMontoDelivery = request.POST.get('TotalMontoDelivery')
    EsNuevaCE = request.POST.get('EsNuevaCE')
    Notas = request.POST.get('Notas')
    Payment_ID_CE = request.POST.get('Payment_ID_CE')
    Delivery_Address_ID_CE = request.POST.get('Delivery_Address_ID_CE')
    Driver_ID_CE = request.POST.get('Driver_ID_CE')
    Driver_ID_EW = request.POST.get('Driver_ID_EW')
    Want_FE_CE = request.POST.get('Want_FE_CE')
    Document_Type_ID_FE_CE = request.POST.get('Document_Type_ID_FE_CE')
    Document_ID_FE_CE = request.POST.get('Document_ID_FE_CE')
    Email_Client_FE_CE = request.POST.get('Email_Client_FE_CE')
    Email_Client_CE = request.POST.get('Email_Client_CE')
    Telefono_Client_CE = request.POST.get('Telefono_Client_CE')
    Nombre_Mesa_CE = request.POST.get('Nombre_Mesa_CE')
    Mesa_ID_CE = request.POST.get('Mesa_ID_CE')
    MetodoPago_CE = request.POST.get('MetodoPago_CE')
    TipoConsumoCE = request.POST.get('TipoConsumoCE')
    CobrarDeliveryCE = request.POST.get('CobrarDeliveryCE')
    Eliminada_CE = request.POST.get('Eliminada_CE')
    Eliminada_Aplicada_CE = request.POST.get('Eliminada_Aplicada_CE')
    orden_impresa = request.POST.get('orden_impresa')
    CuponWeb = request.POST.get('CuponWeb')
    retencion = request.POST.get('retencion')
    TypeCoupon = request.POST.get('TypeCoupon')
    Coupons_Real_Value = request.POST.get('Coupons_Real_Value')
    Coupons_Perceived_Value = request.POST.get('Coupons_Perceived_Value')
    Client_IntegrationCode = request.POST.get('Client_IntegrationCode')
    TotalRedemptionsAvailablePerCoupon = request.POST.get('TotalRedemptionsAvailablePerCoupon')
    TotalRedemptionsAvailablePerUser = request.POST.get('TotalRedemptionsAvailablePerUser')
    cliente = request.POST.get('cliente')
    empleado = request.POST.get('empleado')
    detalles = request.POST.get('detalles')
    sucursal = request.POST.get('sucursal')

    try:
        orden = Orden()

        orden.id_order = id_order
        orden.name = name
        orden.Descuentopociento = Descuentopociento
        orden.cobrarimpuesto = cobrarimpuesto
        orden.propina = propina
        orden.SaldoCliente = SaldoCliente
        orden.CobrarValorExtra = CobrarValorExtra
        orden.NombreClientePrepago = NombreClientePrepago
        orden.CantPersonas = CantPersonas
        orden.DescuentoEspecial = DescuentoEspecial
        orden.DescuentoEn = DescuentoEn
        orden.DescuentoLibre = DescuentoLibre
        orden.DescuentoCortesia = DescuentoCortesia
        orden.ValueNITClient = ValueNITClient
        orden.DirClient = DirClient
        orden.TotalSubsidio = TotalSubsidio
        orden.QuitarSubsidio = QuitarSubsidio
        orden.EsPorCuentaPendiente = EsPorCuentaPendiente
        orden.TipoOrden = TipoOrden
        orden.IDOrdenCE = IDOrdenCE
        orden.TipoEstadoCE = TipoEstadoCE
        orden.TotalMontoDelivery = TotalMontoDelivery
        orden.EsNuevaCE = EsNuevaCE
        orden.Notas = Notas
        orden.Payment_ID_CE = Payment_ID_CE
        orden.Delivery_Address_ID_CE = Delivery_Address_ID_CE
        orden.Driver_ID_CE = Driver_ID_CE
        orden.Driver_ID_EW = Driver_ID_EW
        orden.Want_FE_CE = Want_FE_CE
        orden.Document_Type_ID_FE_CE = Document_Type_ID_FE_CE
        orden.Document_ID_FE_CE = Document_ID_FE_CE
        orden.Email_Client_FE_CE = Email_Client_FE_CE
        orden.Email_Client_CE = Email_Client_CE
        orden.Telefono_Client_CE = Telefono_Client_CE
        orden.Nombre_Mesa_CE = Nombre_Mesa_CE
        orden.Mesa_ID_CE = Mesa_ID_CE
        orden.MetodoPago_CE = MetodoPago_CE
        orden.TipoConsumoCE = TipoConsumoCE
        orden.CobrarDeliveryCE = CobrarDeliveryCE
        orden.Eliminada_CE = Eliminada_CE
        orden.Eliminada_Aplicada_CE = Eliminada_Aplicada_CE
        orden.orden_impresa = orden_impresa
        orden.CuponWeb = CuponWeb
        orden.retencion = retencion
        orden.TypeCoupon = TypeCoupon
        orden.Coupons_Real_Value = Coupons_Real_Value
        orden.Coupons_Perceived_Value = Coupons_Perceived_Value
        orden.Client_IntegrationCode = Client_IntegrationCode
        orden.TotalRedemptionsAvailablePerCoupon = TotalRedemptionsAvailablePerCoupon
        orden.TotalRedemptionsAvailablePerUser = TotalRedemptionsAvailablePerUser
        orden.cliente = cliente
        orden.empleado = empleado
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
