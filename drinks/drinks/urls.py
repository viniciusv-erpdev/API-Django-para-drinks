from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# importar views do seu app (a pasta que tem models.py)
from drinks import views  # substitua 'seu_app' pelo nome real do app

urlpatterns = [
    path('admin/', admin.site.urls),

    # rotas da API
    path('api/drinks/', views.drink_list, name='drink-list'),
    path('api/drinks/<int:id>/', views.drink_detail, name='drink-detail'),

    # página de teste
    path('testpage/', views.test_page, name='testpage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
