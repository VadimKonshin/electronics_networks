from django.urls import path
from rest_framework.routers import SimpleRouter

from store.apps import StoreConfig
from store.views import NetworkEntityCreateAPIView, NetworkEntityListAPIView, NetworkEntityRetrieveAPIView, \
    NetworkEntityUpdateAPIView, NetworkEntityDestroyAPIView, ProductViewSet

app_name = StoreConfig.name
router = SimpleRouter()
router.register(r"product", ProductViewSet, basename="product")


urlpatterns = [
    path('create/', NetworkEntityCreateAPIView.as_view(), name='net_create'),
    path('', NetworkEntityListAPIView.as_view(), name='net_list'),
    path('<int:pk>/', NetworkEntityRetrieveAPIView.as_view(), name='net_retrieve'),
    path('<int:pk>/update/', NetworkEntityUpdateAPIView.as_view(), name='net_update'),
    path('<int:pk>/delete/', NetworkEntityDestroyAPIView.as_view(), name='net_delete'),
] + router.urls