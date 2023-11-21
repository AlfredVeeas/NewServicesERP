from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, login_view, menu_view, gestorOperaciones, nueva_ficha, eliminar_ficha, descargar_excel, inventario, gestorQuimico, nuevaFichaQuimico, gestorVehiculo, eliminar_fichaQuimico, descargar_excelQuimico, nuevaFichaVehiculo, descargar_excelVehiculo, gestorHerramientas, nuevaFichaHerramientas, descargar_excelHerramientas, eliminar_fichaHerramientas

app_name = 'erp'  

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu_view, name='menu'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='erp:home'), name='logout'),
    path('gestor-operaciones/', gestorOperaciones, name='gestor-operaciones'),
    path('nueva-ficha/', nueva_ficha, name='nueva_ficha'),
    path('eliminar-ficha/<int:ficha_id>/', eliminar_ficha, name='eliminar-ficha'),
    path('descargar-excel/', descargar_excel, name='descargar-excel'),
    path('inventario/', inventario, name='inventario'),
    path('gestor-quimico/', gestorQuimico, name='gestor-quimico'),
    path('ficha-quimico/', nuevaFichaQuimico, name='ficha-quimico'),
    path('eliminar-fichaQuimico/<int:ficha_id>/', eliminar_fichaQuimico, name='eliminar-fichaQuimico'),
    path('descargar-excelQuimico/', descargar_excelQuimico, name='descargar-excelQuimico'),    
    path('gestor-vehiculo/', gestorVehiculo, name='gestor-vehiculo'),
    path('ficha-vehiculo/', nuevaFichaVehiculo, name='ficha-vehiculo'),
    path('eliminar-fichaVehiculo/<int:ficha_id>/', eliminar_fichaQuimico, name='eliminar-fichaVehiculo'),
    path('descargar-excelVehiculo/', descargar_excelVehiculo, name='descargar-excelVehiculo'),   
    path('gestor-herramientas/', gestorHerramientas, name='gestor-herramientas'),
    path('ficha-herramientas/', nuevaFichaHerramientas, name='ficha-herramientas'),
    path('descargar-excelHerramientas/', descargar_excelHerramientas, name='descargar-excelHerramientas'),  
    path('eliminar-fichaHerramientas/<int:ficha_id>/', eliminar_fichaHerramientas, name='eliminar-fichaHerramientas'),

    # Otras rutas aquí...
]
