import matplotlib.pyplot as plt
import numpy as np
import random

matris_sayi = int(input("Matris sayısını girin: "))
#gidebilecegi butun yollar
all_paths = []
#en kısa yol
exit_paths = []

#ilk matrisi random 0 ve 1 ile doldurur
matris = np.array([[random.choice([0, 1]) for _ in range(matris_sayi)] for _ in range(matris_sayi)])

#Yalnızca 1 çıkış olması için en alt satırı 0 yapıyoruz
matris[-1, :] = 0

#2.Matrisi tamamını X ile doldurur
matris2 = np.full((matris_sayi, matris_sayi), "X", dtype=str)

#Matris sınırları içinde mi  kontrolü yapar
def is_valid(i, j):
    return 0 <= i < matris_sayi and 0 <= j < matris_sayi

#Renklendirme kodlarimiz
def paint_cells(ax):
    for i in range(matris_sayi):
        for j in range(matris_sayi):
            if matris2[i, j] == "O":
                if i == giris_r and j == giris_c:
                    ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=True, color='red'))
                elif i == cikis_r and j == cikis_c:
                    ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=True, color='yellow'))
                elif [i, j] in exit_paths:
                    ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=True, color='purple'))
                else:
                    ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=True, color='green'))
def find_path(i, j, path):
    # Labirentin girişini belirtiyoruz
    matris2[0, randomss] = "O"
    # labirentin çıkışını belirtiyoruz
    matris2[matris_sayi - 1, randoms] = "O"
    # Çıkış yolumuzu belirtiyor
    matris[matris_sayi - 1, randoms] = 1
    # mevcut konumun en alt satıra ulaşıp ulaşmadığını kontrol eder. Ulaşmışsa, bu yolun sonunu belirten bir işaretleme yapar ve bu yolu all_paths listesine ekler
    if i == len(matris) - 1:
        all_paths.append(path + [[1]])

    possibilities = []

    #Searching
    for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        positionx = i + x
        positiony = j + y

        if is_valid(positionx, positiony):
            if matris[positionx][positiony] == 1:
                #Aynı yoldan geçmemesini sağlıyor
                if [positionx, positiony] not in path:
                    matris2[positionx, positiony] = "O"
                    possibilities.append([positionx, positiony])
    #Çıkmaz sokağa geldiğinde sonu -1 yapar
    if len(possibilities) == 0:
        all_paths.append(path + [[-1]])
        return
    #Döngüyü tekrarlatma yeri
    for coord in possibilities:
        find_path(coord[0], coord[1], path + [coord])


#Görselleştiren kısım 1kütüphaneyi çalıştırır
def visualize_maze():
    fig, ax = plt.subplots()

    # Display the maze
    ax.imshow(matris, cmap="Blues", interpolation="nearest")

    # Add annotations for the path
    for i in range(matris_sayi):
        for j in range(matris_sayi):
            ax.text(j, i, str(matris2[i, j]), ha='center', va='center', fontsize=12,
                    color='black' if matris2[i, j] == "O" else 'white')
    # Paint the cells with "O" in green
    paint_cells(ax)
    plt.show()

#Random giriş belirtiyoruz
randomss=int(random.random()*(matris_sayi-1))

#Random çıkış belirtiyoruz
randoms = int(random.random() * (matris_sayi - 1))

#Çıkışı olan bir matris yapana kadar tekrarlasın
while matris2[matris_sayi - 2, randoms] != "O":
    matris = np.array([[random.choice([0, 1]) for _ in range(matris_sayi)] for _ in range(matris_sayi)])
    matris[-1, :] = 0
    #Mevcut yol olup kesişmesi olmayanları oluşturur ve İsimlerini X olarak atarız
    matris2 = np.full((matris_sayi, matris_sayi), "X", dtype=str)
    find_path(0, randomss, [[0, randomss]])

giris_r = 0
giris_c = randomss

cikis_r = matris_sayi - 1
cikis_c = randoms
print(matris2)
print(matris)
#çıkışa ulaşılacak en kısa yol
exit_paths = min([path for path in all_paths if path[-1] == [1]], key=len)
print(exit_paths)
visualize_maze()