from rest_framework import generics
from blog.models import Post
from .serializers import Postserializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = Postserializer
    pass


class PostDetail(generics.RetrieveDestroyAPIView):
    pass
