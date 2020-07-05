import requests


def check_data(cep, address, number, neighborhood, city, uf):
    if not cep:
        return 'CEP é um campo obrigatório, favor preencher'
    elif not address:
        return 'Endereço é um campo obrigatório, favor preencher'
    elif not number:
        return 'Número é um campo obrigatório, favor preencher'
    elif not neighborhood:
        return 'Bairro é um campo obrigatório, favor preencher'
    elif not city:
        return 'Cidade é um campo obrigatório, favor preencher'
    elif not uf:
        return 'Estado é um campo obrigatório, favor preencher'
    return True


def search_cep_in_viacep(cep):
    result = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
    result = result.json()
    if len(result) == 1:
        return None
    result2 = result['cep'].replace('-', '')
    result['cep'] = result2
    return result