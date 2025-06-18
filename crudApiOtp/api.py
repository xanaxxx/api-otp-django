from .models import Authentication2Af
from rest_framework import viewsets, permissions,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import crudApiOtpSerializer



class crudApiOtpViewSet(viewsets.ModelViewSet):
    queryset = Authentication2Af.objects.all()
    
    permission_classes = [
        permissions.AllowAny
    ]

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        instance = serializer.save()
        if instance.code == False:
            return Response({'cedula':instance.document,'code': "CANT CREATE CODE YOU ALREADY HAVE ONE"}, status=status.HTTP_400_BAD_REQUEST)
        # Retornamos solo el código generado en la respuesta
        return Response({'cedula':instance.document,'code': instance.code}, status=status.HTTP_200_OK)


    @action(detail=False, methods=['post'], url_path='desactivateOtp')
    def desactivate(self, request):
        document = request.data.get('document')
        if not document:
            return Response({'error': 'Document is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        instances = Authentication2Af.objects.filter(document=document, state=1)
        if not instances.exists():
            return Response({'error': 'OTP not found or already deactivated'}, status=status.HTTP_404_NOT_FOUND)
        
        instances.update(state=0)  # Assuming 0 means deactivated
        return Response({'message': 'OTP deactivated successfully'}, status=status.HTTP_200_OK)


    serializer_class = crudApiOtpSerializer