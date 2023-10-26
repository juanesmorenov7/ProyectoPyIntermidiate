import functions as f
import read_data as r


if __name__ == '__main__':
    datos = r.read_csv('./data.csv')
    prueba = f.list_count(datos)
    final = f.filtro(datos, 'Colombia')
    labels = list(final.keys())
    values = list(final.values())
    print(final)
    f.generate_bar_chart(labels, values)