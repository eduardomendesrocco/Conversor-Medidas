import math

acceptMeasures = ["comprimento",
                  "massa",
                  "volume",
                  "temperatura",
                  "area",
                  "velocidade",
                  "tempo",
                  "dados_digitais",
                  "energia",
                  "porcentagem",
                  "angulo"]

fatores_comprimento = {
    "milha": 1609.34,
    "quilometro": 1000,
    "metro": 1,
    "pe": 0.3048,
    "polegada": 0.0254,
    "centimetro": 0.01,
    "milimetro": 0.001
}

fatores_massa = {
    "tonelada": 1000000,
    "quilograma": 1000,
    "grama": 1,
    "miligrama": 0.001,
    "libra": 453.592
}

fatores_volume = {
    "metro_cubico": 1000,
    "litro": 1,
    "mililitro": 0.001
}

fatores_tempo = {
    "anos": 8760,
    "meses": 720,
    "semanas": 168,
    "dias": 24,
    "horas": 1,
    "minutos": 1/60,
    "segundos": 1/3600,
    "milissegundos": 1/3600000
}

def main():

    print(f"========================\n"
          f"|     Comprimento      |\n"
          f"|     Massa            |\n"
          f"|     Volume           |\n"
          f"|     Temperatura      |\n"
          f"|     Área             |\n"
          f"|     Velocidade       |\n"
          f"|     Tempo            |\n"
          f"|     Dados_digitais   |\n"
          f"|     Energia          |\n"
          f"|     Porcentagem      |\n"
          f"|     Ângulo           |\n"
          f"| [x] Moeda (em breve) |\n"
          f"========================")

    measureType = input("Digite a categoria de medida desejada (sem acentos e utilize _ invés de espaços): ")

    while measureType.lower() not in acceptMeasures:
        measureType = input("Digite uma categoria válida para avançar: ")

    valor_numerico = float(input(f"Valor inicial da sua unidade ({measureType}): "))


    if measureType.lower() == acceptMeasures[0]:
        converter_comprimento()

    if measureType.lower() == acceptMeasures[1]:
        converter_massa()

    if measureType.lower() == acceptMeasures[2]:
        converter_volume()

    if measureType.lower() == acceptMeasures[3]:
        converter_temperatura()

    if measureType.lower() == acceptMeasures[4]:
        converter_area()

    if measureType.lower() == acceptMeasures[5]:
        converter_velocidade()

    if measureType.lower() == acceptMeasures[6]:
        converter_tempo()

    if measureType.lower() == acceptMeasures[7]:
        converter_dados_digitais()

    if measureType.lower() == acceptMeasures[8]:
        converter_energia()

    if measureType.lower() == acceptMeasures[9]:
        converter_porcentagem()

    if measureType.lower() == acceptMeasures[10]:
        converter_angulo()

def converter_comprimento(valor, unidade, res):
    return res

if __name__ == '__main__':
    main()