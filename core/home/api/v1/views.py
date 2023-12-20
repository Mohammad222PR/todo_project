from rest_framework.viewsets import ModelViewSet
from .serializers import *
from home.models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import PagInationClass
from rest_framework.response import Response
from rest_framework.views import APIView
# Imported Livery
class TodoApi(ModelViewSet):
    """
    This Class API For retrieve, update, created, deleted, list
    & we also put filters, fields as search and ordering filters
    """

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["complete", "created_date", "updated_date"]
    search_fields = ["title", "user"]
    ordering_fields = ["complete"]
    pagination_class = PagInationClass

class Test(APIView):
    def get(self, request):
        return Response({'detail':'hi'})
