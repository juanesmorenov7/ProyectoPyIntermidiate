import matplotlib.pyplot as plt

def filtro(dict, country):
  res = list(filter(lambda x: x['Country/Territory'] if x['Country/Territory'] == country.capitalize() else None, dict))[0] #--> con esto escojo la primera llave dentro de la lista(solo hay una)
  population_data = {int(''.join(filter(str.isdigit, key))): int(value) for key, value in res.items() if key.endswith('Population')}
  return population_data

def generate_bar_chart(labels, values):
  label = labels
  value = values
  fig, ax = plt.subplots() # coordenadas
  ax.bar(label, value) # los datos
  plt.show() # con esto se hace la gráfica

def list_count(dict):
  paises = [item['Country/Territory'] for item in dict]
  return paises