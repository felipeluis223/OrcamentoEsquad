import pandas as pd

def item(perfil, medida, corte, quantidade, descricao, altura_largura):
    return {
        'Perfil': perfil,
        'Medida': medida,
        'Corte': corte,
        'Quantidade': int(quantidade),
        'Descricao': descricao,
        'L/H': altura_largura
    }
 # Lembrando que está contando o CM:
class Suprema:
    def porta_giro(self, width, height, amount):
        width_marco = width - (28+26) #SU004
        height_marco = height - 15 #SU007

        width_batente = width_marco #SU279
        height_batente = height - (15+17) #SU279

        width_folha = width - (28+26+64) #SU241
        height_folha = height - (15+17+42) #SU241

        width_veneziana_ventilada = width -(28+26+64+100) #US-294
        amount_veneziana = int(((height_folha-100)/60)*amount)

        return [
            item("SU004", width_marco, "90/90", amount, "Marco", "L"),
            item("SU007", height_marco, "90/90", (amount * 2), "Marco", "H"),

            item("SU279", width_batente, "45/45", amount, "Batente", "L"),
            item("SU279", height_batente, "45/90", amount, "Batente", "H"),
            item("SU279", height_batente, "90/45", amount, "Batente", "H"),

            item("SU241", width_folha, "45/45", amount, "Folha", "L"),
            item("SU241", height_folha, "45/45", amount, "Folha", "H"),

            item("US-294", width_veneziana_ventilada, "90/90",amount_veneziana, "Folha", "L"),
        ]

esquadria = Suprema()

print("\nPorta de Giro - Linha Suprema\n")

width = int(input("Digite a largura(mm): "))
height =  int(input("Digite a altura(mm): "))
amount = int(input("Digite a quantidade de peças: "))

df = pd.DataFrame(
    esquadria.porta_giro(width, height, amount), 
    columns=['Perfil', 'L/H', 'Quantidade', 'Descricao' , 'Corte', 'Medida']
)
print(df)
