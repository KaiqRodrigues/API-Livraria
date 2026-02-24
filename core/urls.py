from django.contrib import admin
from django.urls import path, include
from nucleo.views import (
    CategoriaView,
    CategoriasList,
    CategoriaDetail,
    CategoriasListGeneric,
    CategoriasDetailGeneric,
    CategoriaViewSet,
    EditoraViewSet,
    AutorViewSet,
    LivroViewSet, CompraViewSet
)
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



rota = routers.DefaultRouter()

rota.register(r'categorias', CategoriaViewSet)
rota.register(r'editora', EditoraViewSet )
rota.register(r'autores', AutorViewSet)
rota.register(r'livros', LivroViewSet)
rota.register(r'compras', CompraViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('categorias-class/', CategoriaView.as_view()),
    # path('categorias/<int:id>', CategoriaView.as_view()),

    # path('categorias-apiview/', CategoriasList.as_view()),
    # path('categorias-apiview/<int:id>', CategoriaDetail.as_view()),

    # path('categorias-generic/', CategoriasListGeneric.as_view()),
    # path('categorias-generic/<int:id>', CategoriasDetailGeneric.as_view()),

    path('api/', include(rota.urls)),
]
