from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    imagem_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Drink
        fields = ['id', 'nome', 'descricao', 'dificuldade', 'ingredientes', 'imagem', 'imagem_url']

    def get_imagem_url(self, obj):
        request = self.context.get('request')
        if obj.imagem:
            if request is not None:
                return request.build_absolute_uri(obj.imagem.url)
            return obj.imagem.url
        return None
