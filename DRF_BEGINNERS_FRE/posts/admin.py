from django.contrib import admin

from posts.models import Post, Author

admin.site.register(Author)
admin.site.register(Post)
