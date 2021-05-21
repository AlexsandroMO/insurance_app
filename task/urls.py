
from django.urls import path
from .views import index, ListaCliente, EditSegur, DeleteSegur, DeleteConfirm, NewSegur, VCliente
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    #path('', Home, name='home-home'),
    path('lista_cliente', ListaCliente, name='lista-cliente'),
    path('edite_segur/<int:id>', EditSegur, name='edit-segur'),
    path('delete_segur/<int:id>', DeleteSegur, name='delete-segur'),
    path('delete_confirm/<int:id>', DeleteConfirm, name='delete-confir'),
    path('new_segur', NewSegur, name='new-segur'),
    path('v_cliente', VCliente, name='v-cliente'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

