from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Obra, PlanEmergencia, Contratista, EquipoSeguridad
from django.views.generic.edit import CreateView
from django import forms

def index(request):
    return render(request, 'index.html')

# Vistas para Obra
class ObraListView(ListView):
    model = Obra
    template_name = 'construction/obra_list.html'
    context_object_name = 'obras'


from django import forms

class ObraCreateView(CreateView):
    model = Obra
    template_name = 'construction/obra_form.html'
    fields = ['nombre', 'direccion', 'fecha_inicio', 'fecha_fin', 'estado', 'imagen']  # Incluye imagen
    success_url = reverse_lazy('obra-list')

    def get_form(self):
        form = super().get_form()
        form.fields['fecha_inicio'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['fecha_fin'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        messages.success(self.request, 'Obra creada exitosamente.')
        return super().form_valid(form)


class ObraUpdateView(UpdateView):
    model = Obra
    template_name = 'construction/obra_form.html'
    fields = ['nombre', 'direccion', 'fecha_inicio', 'fecha_fin', 'estado', 'imagen']  # Incluye imagen
    success_url = reverse_lazy('obra-list')

    def get_form(self):
        form = super().get_form()
        form.fields['fecha_inicio'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['fecha_fin'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        messages.success(self.request, 'Obra actualizada exitosamente.')
        return super().form_valid(form)


class ObraDeleteView(DeleteView):
    model = Obra
    template_name = 'construction/obra_confirm_delete.html'
    success_url = reverse_lazy('obra-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Obra eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from .models import Obra, PlanEmergencia, Contratista, EquipoSeguridad

# Vistas para PlanEmergencia
class PlanEmergenciaListView(ListView):
    model = PlanEmergencia
    template_name = 'construction/plan_list.html'
    context_object_name = 'planes'

class PlanEmergenciaCreateView(CreateView):
    model = PlanEmergencia
    template_name = 'construction/plan_form.html'
    fields = ['obra', 'nombre', 'descripcion', 'estado','imagen']
    success_url = reverse_lazy('plan-list')

    def form_valid(self, form):
        messages.success(self.request, 'Plan de emergencia creado exitosamente.')
        return super().form_valid(form)

class PlanEmergenciaUpdateView(UpdateView):
    model = PlanEmergencia
    template_name = 'construction/plan_form.html'
    fields = ['obra', 'nombre', 'descripcion', 'estado','imagen']
    success_url = reverse_lazy('plan-list')

    def form_valid(self, form):
        messages.success(self.request, 'Plan de emergencia actualizado exitosamente.')
        return super().form_valid(form)

class PlanEmergenciaDeleteView(DeleteView):
    model = PlanEmergencia
    template_name = 'construction/plan_confirm_delete.html'
    success_url = reverse_lazy('plan-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Plan de emergencia eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

class PlanEmergenciaUpdateView(UpdateView):
    model = PlanEmergencia
    template_name = 'construction/plan_form.html'
    fields = ['obra', 'nombre', 'descripcion', 'estado', 'imagen']  # Agrega 'imagen' aquí
    success_url = reverse_lazy('plan-list')

    def form_valid(self, form):
        messages.success(self.request, 'Plan de emergencia actualizado exitosamente.')
        return super().form_valid(form)

class PlanEmergenciaDeleteView(DeleteView):
    model = PlanEmergencia
    template_name = 'construction/plan_confirm_delete.html'
    success_url = reverse_lazy('plan-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Plan de emergencia eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vistas para Contratista
class ContratistaListView(ListView):
    model = Contratista
    template_name = 'construction/contratista_list.html'
    context_object_name = 'contratistas'

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy

class ContratistaCreateView(CreateView):
    model = Contratista
    template_name = 'construction/contratista_form.html'
    fields = ['nombre', 'rut', 'telefono', 'email', 'especialidad','imagen']
    success_url = reverse_lazy('contratista-list')

    def form_valid(self, form):
        # Guardar el contratista y obtener los datos
        contratista = form.save()

        # Obtener el valor del checkbox para saber si notificar
        enviar_notificacion = self.request.POST.get('enviar_notificacion') == 'on'
        
        # Si se seleccionó la opción de notificar, enviar el correo
        if enviar_notificacion:
            self.enviar_notificacion_correo(contratista)
        
        # Mostrar mensaje de éxito
        messages.success(self.request, 'Contratista creado exitosamente.')
        
        return super().form_valid(form)
    
from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import EmailMessage
from django.conf import settings

from django.core.mail import EmailMessage
from django.conf import settings

class ContratistaCreateView(CreateView):
    model = Contratista
    template_name = 'construction/contratista_form.html'
    fields = ['nombre', 'rut', 'telefono', 'email', 'especialidad', 'imagen']
    success_url = reverse_lazy('contratista-list')

    def form_valid(self, form):
        contratista = form.save()
        self.enviar_notificacion_correo(contratista)
        messages.success(self.request, 'Contratista creado exitosamente.')
        return super().form_valid(form)

    def enviar_notificacion_correo(self, contratista):
        subject = 'Bienvenido, nuevo Contratista!'
        imagen_url = contratista.imagen.url if contratista.imagen else None

        # Mensaje HTML para el correo
        message = f"""
        <p>Hola {contratista.nombre},</p>

        <p>Te damos la bienvenida al sistema como contratista.</p>

        <ul>
            <li><strong>RUT:</strong> {contratista.rut}</li>
            <li><strong>Teléfono:</strong> {contratista.telefono}</li>
            <li><strong>Especialidad:</strong> {contratista.especialidad}</li>
        </ul>

        {'<p><strong>Imagen de tu perfil:</strong></p><img src="http://{settings.HOST_NAME}{imagen_url}" alt="Imagen de contratista" style="max-width: 200px;">' if imagen_url else '<p>No has subido una imagen aún.</p>'}

        <p>¡Gracias por unirte a nosotros! Estamos felices de tenerte en nuestro equipo.</p>

        <p>Saludos,</p>
        <p>El equipo.</p>
        """

        # Crear correo
        email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [contratista.email],
        )
        email.content_subtype = "html"  # Indicamos que el contenido es HTML

        # Adjuntar la imagen si existe
        if contratista.imagen:
            email.attach_file(contratista.imagen.path)

        # Enviar el correo
        email.send(fail_silently=False)

class ContratistaUpdateView(UpdateView):
    model = Contratista
    template_name = 'construction/contratista_form.html'
    fields = ['nombre', 'rut', 'telefono', 'email', 'especialidad','imagen']
    success_url = reverse_lazy('contratista-list')

    def form_valid(self, form):
        messages.success(self.request, 'Contratista actualizado exitosamente.')
        return super().form_valid(form)

class ContratistaDeleteView(DeleteView):
    model = Contratista
    template_name = 'construction/contratista_confirm_delete.html'
    success_url = reverse_lazy('contratista-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Contratista eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vistas para EquipoSeguridad
class EquipoSeguridadListView(ListView):
    model = EquipoSeguridad
    template_name = 'construction/equipo_list.html'
    context_object_name = 'equipos'

class EquipoSeguridadCreateView(CreateView):
    model = EquipoSeguridad
    template_name = 'construction/equipo_form.html'
    fields = ['nombre', 'tipo', 'cantidad', 'fecha_adquisicion', 'estado', 'obra','imagen']
    success_url = reverse_lazy('equipo-list')
    def get_form(self):
        form = super().get_form()
        form.fields['fecha_adquisicion'].widget = forms.DateInput(attrs={'type': 'date'})
        return form
    def form_valid(self, form):
        messages.success(self.request, 'Equipo de seguridad creado exitosamente.')
        return super().form_valid(form)

class EquipoSeguridadUpdateView(UpdateView):
    model = EquipoSeguridad
    template_name = 'construction/equipo_form.html'
    fields = ['nombre', 'tipo', 'cantidad', 'fecha_adquisicion', 'estado', 'obra','imagen']
    success_url = reverse_lazy('equipo-list')

    def form_valid(self, form):
        messages.success(self.request, 'Equipo de seguridad actualizado exitosamente.')
        return super().form_valid(form)

class EquipoSeguridadDeleteView(DeleteView):
    model = EquipoSeguridad
    template_name = 'construction/equipo_confirm_delete.html'
    success_url = reverse_lazy('equipo-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Equipo de seguridad eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)
    
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Obra, PlanEmergencia, EquipoSeguridad

class ObraDetailView(DetailView):
    model = Obra
    template_name = 'construction/obra_detail.html'
    context_object_name = 'obra'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['planes'] = PlanEmergencia.objects.filter(obra=self.object)
        context['equipos'] = EquipoSeguridad.objects.filter(obra=self.object)
        return context
    