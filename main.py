# Bot para gerar medidas - Esquadria
import pandas as pd

def porta_giro_suprema(largura, altura, quantidade):
    marco_largura_desconto = largura - (28+26) #SU004
    marco_altura_desconto = altura - 15 #SU007
    
    batente_largura_desconto = marco_largura_desconto #SU279
    batente_altura_desconto = altura - (15+17) #SU279
    
    folha_largura_desconto = largura - (28+26+64) #SU241
    folha_altura_desconto = altura - (15+17+42) #SU241

    veneziana_ventilada_largura = largura - (28+26+64+100) #US-294

    return [
        {
            'Perfil': 'SU004',
            'Medida': marco_largura_desconto,
            'Corte': '90/90',
            'Quantidade': quantidade,
            'Descricao': 'Marco',
            'L/H': 'L'
        },
        {
            'Perfil': 'SU007',
            'Medida': marco_altura_desconto,
            'Corte': '90/90',
            'Quantidade': quantidade * 2,
            'Descricao': 'Marco',
            'L/H': 'H'
        },
        {
            'Perfil': 'SU279',
            'Medida': batente_largura_desconto,
            'Corte': '45/45',
            'Quantidade': quantidade,
            'Descricao': 'Batente',
            'L/H': 'L'
        },
        {
            'Perfil': 'SU279',
            'Medida': batente_largura_desconto,
            'Corte': '45/90',
            'Quantidade': quantidade,
            'Descricao': 'Batente',
            'L/H': 'H'
        },
        {
            'Perfil': 'SU279',
            'Medida': batente_largura_desconto,
            'Corte': '90/45',
            'Quantidade': quantidade,
            'Descricao': 'Batente',
            'L/H': 'H'
        },
        {
            'Perfil': 'SU241',
            'Medida': folha_largura_desconto,
            'Corte': '45/45',
            'Quantidade': quantidade,
            'Descricao': 'Folha',
            'L/H': 'L'
        },
        {
            'Perfil': 'SU241',
            'Medida': folha_altura_desconto,
            'Corte': '45/45',
            'Quantidade': quantidade,
            'Descricao': 'Folha',
            'L/H': 'H'
        },
        {
            'Perfil': 'US-294',
            'Medida': veneziana_ventilada_largura,
            'Corte': '90/90',
            'Quantidade': ((folha_altura_desconto-100)/60)*quantidade,
            'Descricao': 'Venezianda Ventilada',
            'L/H': 'L'
        }
    ]

data = porta_giro_suprema(700, 2120, 1)
df = pd.DataFrame(data)