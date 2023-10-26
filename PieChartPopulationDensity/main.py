import read_data as r
import functions as f

if __name__ == '__main__':
  final = f.llave(r.read_csv('./data.csv'))

  f.generate_pie_chart(final[0], final[1])