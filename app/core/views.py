from django.shortcuts import render


# ------codigo proyecto-------------------
def needle_cliente(request):
    return render(request, 'clientes.html')


def needle_nuevocliente(request):
    return render(request, 'clientesnuevousu.html')


def needle_nuevocliente2(request):
    return render(request, 'clientesnuevousu2.html')


def needle_editcliente(request):
    return render(request, 'clientesedit.html')


def needle_crono(request):
    return render(request, 'cronograma.html')


def needle_pedidos(request):
    return render(request, 'pedidos.html')


def needle_nosotros(request):
    return render(request, 'nosotros.html')


def needle_reperror(request):
    return render(request, 'reportar_error.html')


def needle_ayuda(request):
    return render(request, 'ayuda.html')


def needle_cont(request):
    return render(request, 'contacto.html')


def needle_login(request):
    return render(request, 'loginprincipal.html')


def needle_regis(request):
    return render(request, 'loginregusu.html')


def needle_recpass(request):
    return render(request, 'loginrecpass.html')