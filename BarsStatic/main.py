import functions as f
import read_data as r


if __name__ == '__main__':
  datos = r.read_csv('./data.csv')
  prueba = f.list_count(datos)
  pais = input(f'escoje un país: ')
  print(f'País escogido es --> {pais}')
  final = f.filtro(datos,pais)
  print(final)
  # labels = list(final.keys())
  # values = list(final.values())
  f.generate_bar_chart(final[0],final[1])
  f.generate_pie_chart(final[0],final[1])