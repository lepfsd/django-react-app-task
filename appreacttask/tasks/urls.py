from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from tasks import views
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
)
from .api import TaskApiView

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'tasks')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls('task api')),
    path('api/v1/products/', TaskApiView.as_view(), name='products'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]