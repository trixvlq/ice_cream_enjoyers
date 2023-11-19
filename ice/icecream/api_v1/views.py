from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .permissions import IsOwnerOrReadOnly
from ..models import *
from .serializers import *
from .pagination import *

class IceCreamApiList(generics.ListAPIView):
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer
    pagination_class = PaginationAPIView

class IceCreamUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = IceCreamSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return IceCream.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        return generics.get_object_or_404(queryset, slug=slug)


class IceCreamDelete(generics.RetrieveDestroyAPIView):
    serializer_class = IceCreamSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        return IceCream.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        return generics.get_object_or_404(queryset, slug=slug)


class IceCreamCreate(generics.CreateAPIView):
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer
    permission_classes = (IsAuthenticated,)

class CategoryAPIList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

