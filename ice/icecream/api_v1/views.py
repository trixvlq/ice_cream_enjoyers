from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsOwnerOrReadOnly
from ..models import *
from .serializers import *
class IceCreamApiList(generics.ListAPIView):
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class IceCreamUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = IceCreamSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        return IceCream.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        return generics.get_object_or_404(queryset, slug=slug)