from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        errors = {}

        if not validate_cpf(data['cpf']):
            errors['cpf'] = "Número de CPF inválido"

        if not validade_nome(data['nome']):
            errors['nome'] = "Não inclua números neste campo"

        if not validade_rg(data['rg']):
            errors['rg'] = "O RG deve ter 9 dígitos"

        if not validade_celular(data['celular']):
            errors['celular'] = "O número de celular deve seguir este modelo: 11 91234-1234 (respeitando os espaços e traço)"

        if errors:
            raise serializers.ValidationError(errors)
        return data