from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Posting
from .serializers import PostingSerializer
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.authentication import BasicAuthentication

class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True  
        if request.method in ['POST', 'PUT', 'DELETE']:
            return request.user.is_superuser
        return False

class PostListCreate(APIView):
    permission_classes = [WriteByAdminOnlyPermission]

    def get(self, request):
        posts = Posting.objects.all()
        serializer = PostingSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    permission_classes = [WriteByAdminOnlyPermission]

    def get(self, request, pk):
        try:
            post = Posting.objects.get(pk=pk)
        except Posting.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostingSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            post = Posting.objects.get(pk=pk)
        except Posting.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostingSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            post = Posting.objects.get(pk=pk)
        except Posting.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
