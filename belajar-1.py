def belajar(): #fungsi
    masukan = int(input('\nMasukan nilai ujian : ')) # ini adalah variable input (integer)
    if masukan >= 90: # jika nilai input lebih dari atau sama dengan 90
        print('Nilai kamu',masukan,'dengan predikat [A]\n') # output maka kamu predikat [A]
    elif masukan  >= 80: # jika nilai input lebih dari atau sama dengan 80
        print('Nilai kamu',masukan,'dengan predikat [B]\n') # output maka kamu predikat [B]
    elif masukan >= 70: # jika nilai input lebih dari atau sama dengan 70
        print('Nilai kamu',masukan,'dengan predikat [C]\n') # output maka kamu predikat [C]
    else : # jika nilai input kurang terpenuhi dari semua kondisi
        print('Nilai kamu',masukan,'dengan predikat [D]\n') # output maka di berikan predikat [D]
def looping(): # fungsi
    print('\n') # untuk membuat baris baru
    data = ['apel', 'anggur', 'jeruk', 'salak', 'semangka', 'pepaya'] # list data array buah-buahan
    for i in data : # perulangan data array buah
        print('Ini buah', i, '') # output perulangan
    print('\n')# untuk membuat baris baru
def hitung(): # fungsi
    masukan = int(input('\nMasukan total yang akan di ulang : ')) # inputan total perulangan (integer)
    print('\n')# untuk membuat baris baru
    for i in range(masukan): # perulangan nilai yang sudah di tentukan
        print('Ini perulangan ke ',i) # output perulangan
    print('\n')# untuk membuat baris baru
def menu(): # fungsi
    print('\n[1] Menghitung nilai ujian (if, elif, else)') #output untuk menu
    print('[2] Perulangan data (looping)')
    print('[3] Perulangan nilai (looping)')
    menu = int(input('\nSilahkan pilih menu nya : ')) # inputan menut (integer)
    if menu > 3: # jika nilai input lebih dari 3
        print('Masukan nilai sesuai menu!') # output masukan nilai dengan benar
    elif menu == 1: # jika nilai input sama dengan nilai 1
        belajar() # maka memanggil fungsi belajar - Menghitung nilai ujian (if, elif, else)
    elif menu == 2: # jika nilai input sama dengan nilai 2
        looping() # maka memanggil fungsi looping - Perulangan data (looping)
    elif menu == 3: # jika nilai input sama dengan nilai 3
        hitung() # maka memanggil fungsi hitung - Perulangan nilai (looping)
    else : # jika tidak sesuai kondisi maka
        print('Masukan dengan benar! (1-3)') # output masukan dengan benar / menegaskan inputan yang di masukan

# memanggil menu
menu()
