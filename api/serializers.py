from rest_framework import serializers

from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('author','title','content','updated_on')