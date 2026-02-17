from django.urls import path
from .views import QueryCreateView
from .views import QueryRespondView


urlpatterns = [
    path('', QueryCreateView.as_view(), name='query-create'),
    path('<int:pk>/respond/', QueryRespondView.as_view(), name='query-respond'),
]
