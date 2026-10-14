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


# Barcha categoriyalar: ishlarning faqat nomi
class CategorySerializer(serializers.ModelSerializer):
    jobs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Category
        fields = ['id', 'name', 'jobs']


# Bitta categoriya: ishlar to'liq
class CategoryDetailSerializer(serializers.ModelSerializer):
    jobs = JobInCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'jobs']


# Barcha joblar: categoriya ma'lumoti bilan
class JobSerializer(serializers.ModelSerializer):
    category_info = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ['id', 'title', 'company', 'description', 'salary',
                  'category', 'category_info']

    def get_category_info(self, obj):
        return {'id': obj.category.id, 'name': obj.category.name}


# Bitta job: categoriya va commentlar bilan
class JobDetailSerializer(JobSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'company', 'description', 'salary',
                  'category', 'category_info', 'comments']
