import csv
#se inicializan las variables para la playlist, las canciones con like y la lista que contendrá las canciones con like que NO se encuentren ya en la playlist
playlist = []
like = []
out = []
#se inicializa el lector de csv y se recorre el archivo guardando unicamente los datos pertinentes (canción, artista) en una lista de 2D,
#en caso de haber un descuadre en los datos, se guarda toda la linea.
with open ('la_playlist.csv', 'r') as csv_file:
    read_playlist = csv.reader(csv_file, delimiter=',')
    try:
        for line in read_playlist:
            playlist.append([line[1], line[3]])
    except:
            playlist.append([line])



with open ('liked.csv','r') as csv_file:
    read_like = csv.reader(csv_file, delimiter=',')
    try:
        for line in read_like:
            like.append([line[1], line[3]])
    except:
        like.append([line])
#se imprimien las longitudes y listas completas para verificación, esto se eliminará una vez se demuestre que el programa funciona
print(len(playlist))
print(len(like))
print('Playlist:')
for element in playlist:
    print(element)
print('Like:')
for element in like:
    print(element)

