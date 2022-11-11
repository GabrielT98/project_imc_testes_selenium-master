from django.shortcuts import HttpResponse, redirect, render
def home(request):
    if request.method == 'GET':
        return render(request=request, template_name='index.html')
    
    if request.POST:
        sexo_masculino = request.POST.get('masculino', None)
        sexo_feminino = request.POST.get('feminino', None)
        peso = float(request.POST.get('peso'))
        altura_metro = float(request.POST.get('altura'))
        imc = (peso / (altura_metro * altura_metro))
        def verificar_imc():
            if sexo_masculino:
                if imc < 20.7:
                    return 'abaixo do peso'
                else:
                    if imc <= 26.4:
                        return 'no peso normal'
                    else:
                        if imc <= 27.8:
                            return 'marginalmente acima do peso'
                        else:
                            if imc <= 31.1:
                                return 'acima do peso ideal'
                            else:
                                return 'obeso'
            if sexo_feminino:
                if imc < 19.1:
                    return 'abaixo do peso'
                else:
                    if imc <= 25.8:
                        return 'no peso normal'
                    else:
                        if (imc <= 27.3):
                            return 'marginalmente acima do peso'
                        else:
                            if imc <= 32.3:
                                return 'acima do peso ideal'
                            else:
                                return 'obeso'
        resultado = verificar_imc()
        context = {
            'resultado': resultado
        }
        return render(request=request, template_name='index.html', context=context)
