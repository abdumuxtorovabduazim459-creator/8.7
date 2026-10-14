from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, Job
from .serializers import (CategorySerializer, CategoryDetailSerializer,
                          JobSerializer, JobDetailSerializer)


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.kwargs.get("pk"):
            return CategoryDetailSerializer
        return CategorySerializer


class JobViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        jobs = Job.objects.all()
        category_id = self.kwargs.get("category_id")
        if category_id:
            jobs = jobs.filter(category_id=category_id)
        return jobs

    def get_serializer_class(self):
        if self.kwargs.get("pk"):
            return JobDetailSerializer
        return JobSerializer
