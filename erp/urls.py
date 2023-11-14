from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, login_view, menu_view, gestorOperaciones, nueva_ficha, eliminar_ficha, descargar_excel, gestor_personal, nueva_fichaPersonal, HijoFormSet

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
    path('gestor-personal/', gestor_personal, name='gestor_personal'),
    path('nueva-fichaPersonal/', nueva_fichaPersonal, name='nueva_fichaPersonal'),
    
    # Otras rutas aquí...
]
