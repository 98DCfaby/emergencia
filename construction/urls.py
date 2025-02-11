from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
     path('obras/', views.ObraListView.as_view(), name='obra-list'),
    path('obras/crear/', views.ObraCreateView.as_view(), name='obra-create'),
    path('obras/<int:pk>/', views.ObraDetailView.as_view(), name='obra-detail'),
    path('obras/<int:pk>/editar/', views.ObraUpdateView.as_view(), name='obra-update'),
    path('obras/<int:pk>/eliminar/', views.ObraDeleteView.as_view(), name='obra-delete'),
    
    # URLs para PlanEmergencia
    path('planes/', views.PlanEmergenciaListView.as_view(), name='plan-list'),
    path('planes/create/', views.PlanEmergenciaCreateView.as_view(), name='plan-create'),
    path('planes/<int:pk>/update/', views.PlanEmergenciaUpdateView.as_view(), name='plan-update'),
    path('planes/<int:pk>/delete/', views.PlanEmergenciaDeleteView.as_view(), name='plan-delete'),
    
    # URLs para Contratista
    path('contratistas/', views.ContratistaListView.as_view(), name='contratista-list'),
    path('contratistas/create/', views.ContratistaCreateView.as_view(), name='contratista-create'),
    path('contratistas/<int:pk>/update/', views.ContratistaUpdateView.as_view(), name='contratista-update'),
    path('contratistas/<int:pk>/delete/', views.ContratistaDeleteView.as_view(), name='contratista-delete'),
    
    # URLs para EquipoSeguridad
    path('equipos/', views.EquipoSeguridadListView.as_view(), name='equipo-list'),
    path('equipos/create/', views.EquipoSeguridadCreateView.as_view(), name='equipo-create'),
    path('equipos/<int:pk>/update/', views.EquipoSeguridadUpdateView.as_view(), name='equipo-update'),
    path('equipos/<int:pk>/delete/', views.EquipoSeguridadDeleteView.as_view(), name='equipo-delete'),
    path('obras/<int:pk>/detalle/', views.ObraDetailView.as_view(), name='obra-detail'),

]