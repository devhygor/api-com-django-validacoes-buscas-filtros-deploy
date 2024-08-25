from rest_framework import serializers


def validate_cpf(cpf):
    if len(cpf) != 11:
        raise serializers.ValidationError('O CPF deve ter 11 dígitos')
    return cpf

def validade_nome(nome):
    if not nome.isalpha():
        raise serializers.ValidationError('Este campo nao pode ter números e nem caracteres especiais')
    return nome

def validade_rg(rg):
    if len(rg) != 9:
        raise serializers.ValidationError('O RG deve ter 9 dígitos')
    return rg

def validade_celular(celular):
    if len(celular) < 11:
        raise serializers.ValidationError('O número do celular deve ter pelo menos 11 dígitos')
    return celular