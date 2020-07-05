from django.shortcuts import render
from django.shortcuts import render, redirect
from .utils import check_data
from .models import Address
from django.contrib import messages
from .models import Address
from .utils import search_cep_in_viacep
import re

def AddressIndex(request):
    return render(request, 'address.html')


def SearchCEP(request):
    if request.method == 'POST':
        cep = request.POST.get('cep')
        if re.search(r'[^0-9]', cep):
            messages.info(request, 'O CEP precisa ser apenas números')
            return redirect('AddressIndex')
        try:
            cep_exists_in_db = Address.objects.get(cep=cep)
        except:
            cep_exists_in_db = None
        if not cep_exists_in_db:
            # Localzindo via API viacep.
            cep_exists_in_viacep = search_cep_in_viacep(cep)
            if not cep_exists_in_viacep:
                messages.info(request, 'CEP não encontrado.')
                request.session['address'] = {}
                return redirect('AddressIndex')
            messages.info(request, 'CEP encontrado pelo viacep.')
            request.session['address'] = cep_exists_in_viacep
            return redirect('AddressIndex')
        # Caso exista, usar as informações do banco de dados para preencher
        data = {}
        data['cep'] = cep_exists_in_db.cep
        data['logradouro'] = cep_exists_in_db.address
        data['bairro'] = cep_exists_in_db.neighborhood
        data['localidade'] = cep_exists_in_db.city
        data['uf'] = cep_exists_in_db.uf
        request.session['address'] = data
        messages.info(request, 'CEP ja existia no banco de dados')
        return redirect('AddressIndex')
    return render(request, 'address.html')


def Index(request):
    address = Address.objects.all()
    return render(request, 'index.html', {'address': address})


def RegisterAddress(request):
    if request.method == 'POST':
        cep = request.session.get('address')['cep']
        address = request.POST.get('address')
        number = request.POST.get('number')
        complement = request.POST.get('complement')
        neighborhood = request.POST.get('neighborhood')
        city = request.POST.get('city')
        uf = request.POST.get('uf')
        description = request.POST.get('description')
        # Verificação de campos obrigatórios
        msg_info = check_data(cep, address, number, neighborhood, city, uf)
        try:
            cep_exists_in_db = Address.objects.get(cep=cep)
        except:
            cep_exists_in_db = None
        if cep_exists_in_db and msg_info == True:
            cep_exists_in_db.address = address
            cep_exists_in_db.number = number
            cep_exists_in_db.complement = complement
            cep_exists_in_db.neighborhood = neighborhood
            cep_exists_in_db.city = city
            cep_exists_in_db.uf = uf
            cep_exists_in_db.description = description
            cep_exists_in_db.save()
            messages.info(request, 'Endereço atualizado com sucesso.')
            return redirect('index')

        if msg_info == True:
            address_create = Address.objects.create(cep=cep, address=address, number=number,
                                                    complement=complement, neighborhood=neighborhood,
                                                    city=city, uf=uf, description=description)
            address_create.save()
            messages.info(request, 'Endereço cadastrado com sucesso.')
            return redirect('index')
        messages.info(request, msg_info)
        return redirect('RegisterAddress')

    return render(request, 'address.html')
