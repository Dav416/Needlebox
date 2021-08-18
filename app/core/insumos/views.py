from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # nececario para el decorador
from django.shortcuts import redirect
from django.utils.decorators import method_decorator  # nececario para el decorador
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView, UpdateView
from core.insumos.models import InsRegInsu, InsRegProv
from core.insumos.forms import RegInsumoForm, RegProveedorForm
from django.urls import reverse_lazy


# view para la plantilla y las tablas de insumos y proveedores


class NeedleInsu(TemplateView):
    template_name = '../templates/insumos.html'

    # @method_decorator(login_required)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = InsRegInsu.objects.all()
        context['object_list2'] = InsRegProv.objects.all()

        context['form1'] = RegInsumoForm
        context['form2'] = RegProveedorForm

        # context['LoadInsulist'] = reverse_lazy('lista_insumos')
        return context


# ----------------------------------------------------
# Formulario para INSUMOS
class RegInsumoCreateView(CreateView):
    model = InsRegInsu
    form_class = RegInsumoForm
    template_name = 'insumos.html'
    success_url = reverse_lazy('insumos')

    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # if request.method == 'GET':
        #    return redirect('insumos')
        return super().dispatch(request, *args, **kwargs)

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = InsRegInsu.objects.all()
        context['form1'] = RegInsumoForm
        return context


class EditInsumoUpdateView(UpdateView):
    model = InsRegInsu
    form_class = RegInsumoForm
    template_name = 'insumos.html'
    success_url = reverse_lazy('insumos')

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
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = InsRegInsu.objects.all()
        context['form1'] = RegInsumoForm
        return context









# ---------------------------------------------------------------------------------
# Formulario para PROVEEDORES
class RegProveedorCreateView(CreateView):
    model = InsRegProv
    form_class = RegProveedorForm
    template_name = 'insumos.html'
    success_url = reverse_lazy('insumos')

    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
    #    if request.method == 'GET':
    #        return redirect('insumos')
        return super().dispatch(request, *args, **kwargs)

    """
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = InsRegProv.objects.get(pk=request.POST['id']).provtojson()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = InsRegInsu.objects.all()
        context['form1'] = RegInsumoForm
        context['object_list2'] = InsRegProv.objects.all()
        context['form2'] = RegProveedorForm
        return context


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