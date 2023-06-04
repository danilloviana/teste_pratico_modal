def converter_notas_para_graus(notas):
    graus = {
        'Dó': 'I',
        'Ré': 'II',
        'Mi': 'III',
        'Fa': 'IV',
        'Sol': 'V',
        'Lá': 'VI',
        'Si': 'VII'
    }
    
    graus_notas = []
    
    for nota in notas:
        grau = graus.get(nota)
        graus_notas.append(grau)
    
    return graus_notas

## Exemplo de uso
#notas = ['Ré', 'Sol', 'Dó']
#resultado = converter_notas_para_graus(notas)
#print(resultado)
