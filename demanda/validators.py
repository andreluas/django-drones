import re

def contato_valido(info_contato):
    """Validação de Celular para Info_contato"""
    format = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(format, info_contato)
    return response