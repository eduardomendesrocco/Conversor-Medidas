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
                  "angulo"]

fatores_comprimento = {
    "milha": 1609.34, "mi": 1609.34,
    "quilometro": 1000, "km": 1000,
    "metro": 1, "m": 1,
    "pe": 0.3048,
    "polegada": 0.0254, "in": 0.0254,
    "centimetro": 0.01, "cm": 0.01,
    "milimetro": 0.001, "mm": 0.001
}

fatores_massa = {
    "tonelada": 1000000, "t": 1000000,
    "quilograma": 1000, "kg": 1000,
    "grama": 1, "g": 1,
    "miligrama": 0.001, "mg": 0.001,
    "libra": 453.592, "lb": 453.592
}

fatores_volume = {
    "metro_cubico": 1000, "m3": 1000,
    "litro": 1, "L": 1,
    "mililitro": 0.001, "ml": 0.001, "mL": 0.001
}

fatores_tempo = {
    "anos": 8760,
    "meses": 720,
    "semanas": 168,
    "dias": 24, "d": 24,
    "horas": 1, "h": 1,
    "minutos": 1/60, "m": 1/60,
    "segundos": 1/3600, "s": 1/3600,
    "milissegundos": 1/3600000, "ms": 1/3600000
}

fatores_dados_digitais = {
    "zettabyte":1024**7, "ZB": 1024**7,
    "exabyte": 1024**6, "EB": 1024**6,
    "petabyte": 1024**5, "PB": 1024**5,
    "terabyte": 1024**4, "TB": 1024**4,
    "gigabyte": 1024**3, "GB": 1024**3,
    "megabyte": 1024**2, "MB": 1024**2,
    "quilobyte": 1024, "KB": 1024,
    "byte": 1, "B": 1,
    "bit": 1/8, "b": 1/8
}

fatores_area = {
    "quilometro_quadrado": 1000**2, "km2": 1000**2,
    "metro_quadrado": 1, "m2": 1,
    "centimetro_quadrado": 0.01**2, "cm2": 0.01**2,
    "milimetro_quadrado": 0.001**2, "mm2": 0.001**2,
    "pe_quadrado": 0.3048**2, "pe2": 0.3048**2,
    "polegada_quadrada": 0.0254**2, "in2": 0.0254**2,
    "milha_quadrada": 1609.34**2, "mi2": 1609.34**2
}

fatores_energia = {
    "joule": 1, "J": 1,
    "quilojoule": 1000,
    "caloria": 4.184,
    "quilocaloria": 4184,
    "watt_hora": 3600,
    "quilowatt_hora": 3600000,
    "btu": 1055.06
}

fatores_velocidade = {
    "metro_por_segundo": 1, "m/s": 1,
    "quilometro_por_hora": 1000/3600, "km/h": 1000/3600,
    "milha_por_hora": 1609.34/3600, "mi/h": 1609.34/3600,
    "no": 1852/3600, "knot": 1852/3600,
    "pe_por_segundo": 0.3048, "pe/s": 0.3048
}

fatores_angulo = {
    "radiano": 1, "rad": 1,
    "grau": math.pi/180, "deg": math.pi/180,
    "gradiano": math.pi/200, "gon": math.pi/200,
    "arcominuto": math.pi/10800, "amin": math.pi/10800,
    "arcossegundo": math.pi/648000, "asec": math.pi/648000
}

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
      f"|     Ângulo           |\n"
      f"| [x] Moeda (em breve) |\n"
      f"========================\n")

print(f"Níveis de precisão -> | Alto | Medio | Baixo |")
nivel_precisao = input(f"Qual será o nível de precisão dos resultados? (Irá alterar levemente os valores): ")

if nivel_precisao.lower() == "alto":
    num_precisao = 10
elif nivel_precisao.lower() == "medio":
    num_precisao = 6
elif nivel_precisao.lower() == "baixo":
    num_precisao = 1

def main():

    measureType = input("Digite uma categoria de medida acima desejada (sem acentos e utilize _ invés de espaços): ")
    while measureType.lower() not in acceptMeasures:
        measureType = input("Digite uma categoria válida para avançar: ")

    initial_measure = input("Digite a unidade inicial:  ")

    valor_numerico = float(input(f"Digite o valor em {initial_measure}: "))

    final_measure = input("Digite a unidade desejada: ")
    print("\n|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
    print("                  Resultados da Conversão                    \n")

    if measureType.lower() == acceptMeasures[0]:
        print(f"               Medida utilizada: {measureType}\n"
              f"               Valor original ({initial_measure}): {valor_numerico}\n"
              f"               {converter_comprimento(valor_numerico, initial_measure, final_measure)}")

    if measureType.lower() == acceptMeasures[1]:
        print(f"               Medida utilizada: {measureType}\n"
              f"               Valor original ({initial_measure}): {valor_numerico}\n"
              f"               {converter_massa(valor_numerico, initial_measure, final_measure)}")

    if measureType.lower() == acceptMeasures[2]:
        print(f"               Medida utilizada: {measureType}\n"
              f"               Valor original ({initial_measure}): {valor_numerico}\n"
              f"               {converter_volume(valor_numerico, initial_measure, final_measure)}")

    temperatura_aceita = ["celsius", "c", "fahrenheit", "f", "kelvin", "k"]

    if measureType.lower() == acceptMeasures[3]:

        resultado = valor_numerico
        if initial_measure in temperatura_aceita and final_measure in temperatura_aceita:

            if initial_measure.lower() in ("celsius", "c"):
                if final_measure.lower() in ("fahrenheit", "f"):
                    resultado = (valor_numerico * 9/5) + 32
                elif final_measure.lower() in ("kelvin", "k"):
                    resultado = valor_numerico + 273.15

            elif initial_measure.lower() in ("fahrenheit", "f"):
                if final_measure.lower() in ("celsius", "c"):
                    resultado = (valor_numerico - 32) * 5/9
                elif final_measure.lower() in ("kelvin", "k"):
                    resultado = (valor_numerico - 32) * 5/9 + 273.15

            elif initial_measure.lower() in ("kelvin", "k"):
                if final_measure.lower() in ("celsius", "c"):
                    resultado = valor_numerico - 273.15
                elif final_measure.lower() in ("fahrenheit", "f"):
                    resultado = (valor_numerico - 273.15) * 9/5 + 32

            print(f"               Medida utilizada: {measureType}\n"
                  f"               Valor original ({initial_measure}): {valor_numerico}\n"
                  f"               Valor final ({final_measure}): {resultado:.{num_precisao}f}")



    if measureType.lower() == acceptMeasures[4]:
        print(f"               Medida utilizada: {measureType}\n"
              f"               Valor original ({initial_measure}): {valor_numerico}\n"
              f"               {converter_area(valor_numerico, initial_measure, final_measure)}")

    if measureType.lower() == acceptMeasures[5]:
        print(f"               Medida utilizada: {measureType}\n"
              f"               Valor original ({initial_measure}): {valor_numerico}\n"
              f"               {converter_velocidade(valor_numerico, initial_measure, final_measure)}")

    if measureType.lower() == acceptMeasures[6]:
        print(f"               Medida utilizada: {measureType}\n"
              f"               Valor original ({initial_measure}): {valor_numerico}\n"
              f"               {converter_tempo(valor_numerico, initial_measure, final_measure)}")

    if measureType.lower() == acceptMeasures[7]:
        print(f"               Medida utilizada: {measureType}\n"
              f"               Valor original ({initial_measure}): {valor_numerico}\n"
              f"               {converter_dados_digitais(valor_numerico, initial_measure, final_measure)}")

    if measureType.lower() == acceptMeasures[8]:
        print(f"               Medida utilizada: {measureType}\n"
              f"               Valor original ({initial_measure}): {valor_numerico}\n"
              f"               {converter_energia(valor_numerico, initial_measure, final_measure)}")

    if measureType.lower() == acceptMeasures[9]:
        print(f"               Medida utilizada: {measureType}\n"
              f"               Valor original ({initial_measure}): {valor_numerico}\n"
              f"               {converter_angulo(valor_numerico, initial_measure, final_measure)}")

# ===============================================================================================

def converter_comprimento(valor, unidade_inicial, unidade_final):
    valor_metros = valor * fatores_comprimento[unidade_inicial]
    resultado = valor_metros / fatores_comprimento[unidade_final]

    return f"Valor final ({unidade_final}): {resultado:.{num_precisao}f}"

def converter_massa(valor, unidade_inicial, unidade_final):
    valor_gramas = valor * fatores_massa[unidade_inicial]
    resultado = valor_gramas / fatores_massa[unidade_final]

    return f"Valor final ({unidade_final}): {resultado:.{num_precisao}f}"

def converter_volume(valor, unidade_inicial, unidade_final):
    valor_litros = valor * fatores_massa[unidade_inicial]
    resultado = valor_litros / fatores_massa[unidade_final]

    return f"Valor final ({unidade_final}): {resultado:.{num_precisao}f}"

def converter_area(valor, unidade_inicial, unidade_final):
    valor_m2 = valor * fatores_area[unidade_inicial]
    resultado = valor_m2 / fatores_area[unidade_final]

    return f"Valor final ({unidade_final}): {resultado:.{num_precisao}f}"

def converter_velocidade(valor, unidade_inicial, unidade_final):
    valor_ms = valor * fatores_velocidade[unidade_inicial]
    resultado = valor_ms / fatores_velocidade[unidade_final]

    return f"Valor final ({unidade_final}): {resultado:.{num_precisao}f}"

def converter_tempo(valor, unidade_inicial, unidade_final):
    valor_horas = valor * fatores_tempo[unidade_inicial]
    resultado = valor_horas / fatores_tempo[unidade_final]

    return f"Valor final ({unidade_final}): {resultado:.{num_precisao}f}"

def converter_dados_digitais(valor, unidade_inicial, unidade_final):
    valor_bytes = valor * fatores_dados_digitais[unidade_inicial]
    resultado = valor_bytes / fatores_dados_digitais[unidade_final]

    return f"Valor final ({unidade_final}): {resultado:.{num_precisao}f}"

def converter_energia(valor, unidade_inicial, unidade_final):
    valor_joules = valor * fatores_energia[unidade_inicial]
    resultado = valor_joules / fatores_energia[unidade_final]

    return f"Valor final ({unidade_final}): {resultado:.{num_precisao}f}"

def converter_angulo(valor, unidade_inicial, unidade_final):
    valor_radianos = valor * fatores_angulo[unidade_inicial]
    resultado = valor_radianos / fatores_angulo[unidade_final]

    return f"Valor final ({unidade_final}): {resultado:.{num_precisao}f}"

# ===============================================================================================
if __name__ == '__main__':
    main()