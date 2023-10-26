import matplotlib.pyplot as plt

def llave(dict):
  # aquí lo que hago es que tomo la data del csv leido y hago un zip de dos list comprehension, una con los nombres del país y otra con el porcentaje de participación
  # a esto lo que hago es de una leerlo en un dictionary comprehension para poder ya tener el formato diccionario correcto con "pais: % population"
  popu = {key: value for key, value in list(zip([item['Country/Territory'] for item in dict], [float(item['World Population Percentage']) for item in dict]))}

  #luego lo que hago es crear otra variable para ordenar de mayor a menor la participación.
  # como al ordenarlo vuelve a quedar como una lista, vuelvo a hacer un dictionary comprehension con la lista de ordenamiento para tener el formato correcto.
  my_dict = {key: value for key, value in list(sorted(popu.items(), key=lambda item: item[1], reverse=True))}

  # luego creo una variable del top 15 de los paises y me lo traigo con [:15] ya que al estar ordenado me trae las 15 primeras  llaves y valores
  top_15 = {key: value for key, value in list(my_dict.items())[:15] }

  # creo la variable del procentaje restante con una resta de la suma de dict values (el total) - la suma de valores de la variable que cree recién.
  porcentaje_restante = sum(my_dict.values()) - sum(top_15.values())

  #y lo que hago acá es agregar como "otros" el porcentaje resultante de la resta anterior para que el gráfico sea más amigable
  top_15["Otros"] = porcentaje_restante

  # creo los labels y values correspondientes para poder retornar y gráficar.
  paises = [x for x in top_15.keys()]
  world = [x for x in top_15.values()]

  # print(my_dict)
  # print(top_15)
  # print(porcentaje_restante)
  return paises, world

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()

  # Hemos agregado (auto porcentaje) autopct='%1.1f%%' al primer llamado de ax.pie en la función para que se muestren los porcentajes en formato de texto dentro de cada porción.
  # Luego, utilizamos la variable autotexts para modificar los valores de porcentaje y agregar el signo "%" al final.

  # La opción autopct en Matplotlib se utiliza para especificar el formato de presentación de los porcentajes dentro de las porciones de un gráfico de pastel.
  #Por ejemplo, autopct='%1.1f%%' significa que los porcentajes se presentarán con un formato que muestra un dígito antes del punto decimal y un dígito después del punto decimal,
  # seguido del signo "%" (por ejemplo, "12.3%").

  #startangle define en que grado se empezará a posicionar los valores en el caso de 180 china se empieza a graficar a las 9 horas reloj

  ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=360)
  ax.axis('equal')

  # Agregar el número del porcentaje dentro de cada porción
  #   En un gráfico de pastel (pie chart) de Matplotlib, wedges, texts, y autotexts son variables que se obtienen cuando se llama a la función ax.pie()
  # y se utilizan para personalizar y manipular elementos del gráfico. Aquí te explico brevemente el propósito de cada uno:

# wedges: Esta variable contiene información sobre las porciones individuales del gráfico de pastel.
  #Puedes utilizar wedges para realizar cambios en el aspecto de las porciones, como colores, sombreado, bordes, etc.

  # texts: Esta variable contiene información sobre las etiquetas de las porciones. Puedes usar texts para personalizar las etiquetas, como cambiar su color, tamaño de fuente o posición.

# autotexts: Esta variable contiene información sobre los números del porcentaje que se muestran dentro de las porciones.
# Puedes utilizar autotexts para personalizar cómo se muestran los números del porcentaje, como el tamaño de fuente, el formato o la posición.

  wedges, texts, autotexts = ax.pie(values, labels=labels, autopct='', startangle=360)

  # for text, autotext in zip(texts, autotexts):
  #   autotext.set_text(f'{autotext.get_text()}%')
  #   autotext.set_fontsize(0.01)  # Ajusta el tamaño de la fuente aquí

  plt.show()