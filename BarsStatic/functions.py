import matplotlib.pyplot as plt

def filtro(dict, country):
  paises = [item['Country/Territory'] for item in dict]
  try:
    if country.capitalize() not in paises:
        raise IndexError(f'Escoge un país de la lista de arriba')
    res = list(filter(lambda x: x['Country/Territory'] if x['Country/Territory'] == country.capitalize() else None, dict))[0] #--> con esto escojo la primera llave dentro de la lista(solo hay una) y uso filter para traerme solo la que cumple la condición.
    population_data = {int(''.join(filter(str.isdigit, key))): int(value) for key, value in res.items() if key.endswith('Population')}
    labels = [x for x in population_data.keys()]
    values = [x for x in population_data.values()]
    return labels, values
  except IndexError as index:
    print(index)

def generate_bar_chart(labels, values):
  label = labels
  value = values
  fig, ax = plt.subplots() # coordenadas
  ax.bar(label, value) # los datos
  plt.show() # con esto se hace la gráfica

def list_count(dict):
  paises = [item['Country/Territory'] for item in dict]
  return paises

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()