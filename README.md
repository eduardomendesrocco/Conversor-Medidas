# Conversor de Medidas

Um conversor de unidades de medida feito em Python, via linha de comando. O programa permite escolher uma categoria de medida (comprimento, massa, tempo, etc.), informar um valor e converter entre as unidades disponíveis dentro dessa categoria.

> 🚧 **Projeto em desenvolvimento** — ainda na fase inicial, funcionalidades e estrutura estão sendo construídas aos poucos.

## 📏 Categorias planejadas

- [x] Comprimento
- [x] Massa
- [x] Volume
- [x] Tempo
- [ ] Temperatura
- [ ] Área
- [ ] Velocidade
- [ ] Dados digitais
- [ ] Energia
- [ ] Porcentagem
- [ ] Ângulo
- [ ] Moeda *(planejado para o futuro)*

## 🛠️ Tecnologias

- Python 3

## ⚙️ Como funciona

1. O programa exibe um menu com as categorias de medida disponíveis.
2. O usuário escolhe a categoria e informa o valor a ser convertido.
3. O usuário informa a unidade de origem e a unidade de destino.
4. O programa retorna o valor convertido.

A lógica de conversão é baseada em dicionários de fatores por categoria, onde cada unidade tem um fator de conversão em relação a uma **unidade base** (ex: metro para comprimento, grama para massa, hora para tempo). O valor de entrada é convertido para a unidade base e, em seguida, da base para a unidade de destino — evitando a necessidade de uma fórmula para cada par de unidades possível.

A categoria de **temperatura** é uma exceção a essa lógica, já que a conversão entre Celsius, Fahrenheit e Kelvin envolve somas/subtrações, não apenas multiplicação — por isso será tratada com cálculos específicos dentro da própria função.

## 🚀 Como executar

```bash
python main.py
```

*(nome do arquivo principal sujeito a alteração conforme o projeto avança)*

## 👤 Autor

Projeto pessoal desenvolvido por Eduardo Mendes Rocco.
