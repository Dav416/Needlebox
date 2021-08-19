from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # nececario para el decorador
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from core.insumos.models import InsRegInsu, InsRegProv
from core.insumos.forms import RegInsumoForm, RegProveedorForm
from django.urls import reverse_lazy


# MENÚ INSUMOS
class NeedleInsu(TemplateView):
    template_name = '../templates/insumos.html'


# ---------------------------------------------------------------------------------


# LISTA DE INSUMOS
class ListInsumosView(ListView):
    model = InsRegInsu
    template_name = 'ListInsumosInsu.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = InsRegInsu.objects.get(pk=request.POST['id']).insutojson()
        except Exception as e:
            data['error en post lista insu'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = InsRegInsu.objects.all()
        context['list_url'] = reverse_lazy('lista_insumos')
        return context


# LISTA DE PROVEEDORES
class ListProveedoresView(ListView):
    model = InsRegProv
    template_name = 'ListInsumosProv.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = InsRegProv.objects.get(pk=request.POST['id']).provtojson()
        except Exception as e:
            data['error en post list prov'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list2'] = InsRegProv.objects.all()
        context['list_url'] = reverse_lazy('lista_proveedores')
        return context


# ----------------------------------------------------
# REGISTRO para INSUMOS
class RegInsumoCreateView(CreateView):
    model = InsRegInsu
    form_class = RegInsumoForm
    template_name = 'FormInsumos.html'
    success_url = reverse_lazy('lista_insumos')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['ERROR EN POST REG INSUMOS'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #   context['form1'] = RegInsumoForm
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('lista_insumos')
        context['titulo'] = "Registrar insumo"

        return context


# REGISTRO para PROVEEDORES
class RegProveedorCreateView(CreateView):
    model = InsRegProv
    form_class = RegProveedorForm
    template_name = 'FormProveedores.html'
    success_url = reverse_lazy('lista_proveedores')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['ERROR EN POST REG PROVEEDORES'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form2'] = RegProveedorForm
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('lista_proveedores')
        context['titulo'] = "Registrar proveedor"
        return context


# ---------------------------------------------------------------------------------

# EDITAR para INSUMOS
class EditInsumoUpdateView(UpdateView):
    model = InsRegInsu
    form_class = RegInsumoForm
    template_name = 'FormInsumos.html'
    success_url = reverse_lazy('lista_insumos')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'ERROR post edit insumos: No ha ingresado a ninguna opción'
        except Exception as e:
            data['ERROR POST EDIT INSUMOS'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form1'] = RegInsumoForm
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('lista_insumos')
        context['titulo'] = "Editar insumo"
        return context


# EDITAR para Proveedores
class EditProveedorUpdateView(UpdateView):
    model = InsRegProv
    form_class = RegProveedorForm
    template_name = 'FormProveedores.html'
    success_url = reverse_lazy('lista_proveedores')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'ERROR post edit Proveedor: No ha ingresado a ninguna opción'
        except Exception as e:
            data['ERROR POST EDIT PROVEEDOR'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form2'] = RegProveedorForm
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('lista_proveedores')
        context['titulo'] = "Editar proveedor"
        return context


# -----------------------------------------------------------------------------------------


# BORRAR para INSUMOS
class BorrarInsumoDeleteView(DeleteView):
    model = InsRegInsu
    template_name = 'BorrarInsumo.html'
    success_url = reverse_lazy('lista_insumos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = reverse_lazy('lista_insumos')
        return context


# BORRAR para PROVEEDORES
class BorrarProveedorDeleteView(DeleteView):
    model = InsRegProv
    template_name = 'BorrarProveedor.html'
    success_url = reverse_lazy('lista_proveedores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = reverse_lazy('lista_proveedores')
        return context

    """
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = InsRegProv.objects.get(pk=request.POST['id']).provtojson()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    """

    """
         sobreescritura de POST: escrito como en este ejemplo, al ejecutarse correctamente el form, nos llevará
         de la vista /insumos a la de /prov, (es decir a la del formulario proveedores), pero no cargará el 
         contenido nor mal de la página, sino un fondo blanco solo con el contenido del diccionario

        def post(self, request, *args, **kwargs):
            data = {'Esta sobrreescritura de post parece solo admitir': 'diccionarios'}
            return JsonResponse(data)

        En esta otra forma crea un diccionario informando de un errror, con las variables 'error' e 'id' 
        que se aprecian, de esta forma {'error' : 'id'}          

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = InsRegInsu.objects.get(pk=request.POST['id']).insutojson()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    """


"""
    def post(self, request, *args, **kwargs):
        form = RegProveedorForm(request.POST)
        if ValueError:

            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})
"""

"""
class ListInsuView(ListView):
    model = InsRegInsu
    template_name = '../templates/ListInsumosInsu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = InsRegInsu.objects.all()
        return context
"""

"""
TemplateView = no base de datos
Listview = base de datos, es decir para tablas
CreateView = para formularios

"""

"""
*Primero se añadió la ruta del documento de views de su nueva app al 'installed_apps' de settings, después se 
creó una clase con el modelo Templateview como parametro, el cual es importado como se ve en la parte 
superior, esto permite que se pueda visualizar la plantilla principal del modulo insumos como una vista basada
en clase, de modo que puedan ser compatibles con la forma en que las urls la recibiran (NombreClase.as_view()).

A la clase se le añade entonces la variable generica y predetermianda template_name y se le pasa la plantilla 
del modulo,recordemos que estas son hijas con herencia de las principales, con solo esto es ya suficiente 
para verla siempre que se configure la url como se ha dicho ya, sin embargo como verán me ví obligaddo a usar 
la función de get content, con el fin de indicarle a la clase que pase los atributos de cada tabla/entidad a 
la variable que se usara para iterar los registros y que se puedan ver los mismos.

La plantillas de tablas fueron pasadas a la plantilla de insumos como un include, de modo que la clase rastrea
las variables de cada tabla y permite iterar-mostrar el contenido correspondiente, ya que cada tabla tiene una
variable distinta (object_list1 para la de insumos y object_list2 para la de proveedores). En sus tablas 
pueden llamar esta variabe como quieran simepre que sea el mismo nombre que el pasado ppor la función get

finalmente se pone el return context, pues esa la vairable predifinida que se usa en esta función, de modo que
pueda retornar esa info al usuario, la cual como vemos se hace viisble para el mismo gracias a que los modelos
se pasan a la plantilla, a su ves pasadas como vistas. 

Lo otro que está comentarlo decidí dejarlo para recordar ese recurso en futuras ocasiones, ya que creí que era
necesario para el funcionamiento de esta vista pero no fue así.

"""