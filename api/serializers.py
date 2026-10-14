from rest_framework import serializers

from .models import Category, Job, Comment


class JobInCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ['category']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    jobs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Category
        fields = ['id', 'name', 'jobs']


class CategoryDetailSerializer(serializers.ModelSerializer):
    jobs = JobInCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'jobs']


class JobSerializer(serializers.ModelSerializer):
    category_info = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ['id', 'title', 'company', 'description', 'salary',
                  'category', 'category_info']

    def get_category_info(self, obj):
        return {'id': obj.category.id, 'name': obj.category.name}


class JobDetailSerializer(JobSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'company', 'description', 'salary',
                  'category', 'category_info', 'comments']
