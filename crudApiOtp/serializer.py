from rest_framework import serializers
from .models import Authentication2Af
import random


class crudApiOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authentication2Af
        fields = ['phone', 'email', 'document','state']
        read_only_fields = ('created_at','updated_at',)

    def create(self, validated_data):
        # Generamos el código dinámicamente
        generated_code = generateCode(validated_data['document'])

        if generated_code  is False:
            raise serializers.ValidationError({
                'document': "CANT CREATE CODE, YOU ALREADY HAVE ONE"
            })
        # Asignar un valor por defecto para 'state' si es requerido

        validated_data['state'] = 1  # Por ejemplo, 1 para indicar "creado" o lo que corresponda
        # Crear y retornar la instancia
        validated_data['code'] = generated_code
        return Authentication2Af.objects.create(**validated_data)
def generateCode(documento):
    code=str(random.randint(1000, 9999))
    if Authentication2Af.objects.filter(document=documento,state=1).exists():
        return False
    return code