from rest_framework import serializers
from posts.models import Post, Author

class AuthorSerializer(serializers.ModelSerializer):
	username = serializers.SerializerMethodField() #for serializerMethod Field checked info.txt

	class Meta:
		model = Author
		fields = (
			'username',
			)

	def get_username(self,obj): #obj will contain the Author model instances (e.g admin, Areeba)
		return obj.user.username


class PostSerializer(serializers.ModelSerializer):
	author = serializers.SerializerMethodField()

	class Meta:
		model = Post
		fields = (
			'id',
			'title',
			'content',
			'publish_date',
			'updated',
			'author'
			)

	def get_author(self,obj): #obj will contain the Post model instances like (1st post, 2nd post, 3rd post)
		return obj.author.user.username 


class PostCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = (
			'title',
			'content',
			'author'
			)
