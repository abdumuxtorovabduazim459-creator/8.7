from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, JobViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('jobs', JobViewSet, basename='job')

urlpatterns = router.urls + [
    path('jobs/category/<int:category_id>/', JobViewSet.as_view({'get': 'list'})),
]
