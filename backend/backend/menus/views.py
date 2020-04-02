from easy_pdf.views import PDFTemplateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from menus.models import Menus
from menus.serializers import MenusSerializer, MenusCreateSerializer

#Create PDF menus
class PDFMenus(PDFTemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        menus = Menus.objects.filter(user=self.request.user)
        return super(PDFMenus, self).get_context_data(
            pagesize='A4',
            menus=menus,
            **kwargs
        )

#Create Menus Api
class MenusListCreateAPIView(ListCreateAPIView):
    serializer_class = MenusSerializer
    create_serializer_class = MenusCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.create_serializer_class
        return self.serializer_class

    def get_queryset(self):
        return Menus.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        return instance


class MenusRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenusCreateSerializer
    # permission_classes = (IsAuthenticated, DjangoModelPermissions)
    lookup_field = 'id'
    list_serializer_class = MenusSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.serializer_class

    def get_queryset(self):
        return Menus.objects.filter(user=self.request.user)
