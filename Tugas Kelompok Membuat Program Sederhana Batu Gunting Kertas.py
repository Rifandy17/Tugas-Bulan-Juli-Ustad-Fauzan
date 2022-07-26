# Mengambil elemen acak pada objek yang ada di array
import random

# Membuat sebuah variabel pilihan yang didalamnya ada "y"
pilihan = "y"

# Membuat sebuah while agar terjadi pengulangan setiap selesai bermain
while pilihan.lower() == "y":

    # Membuat list yang akan digunakan oleh komputer
    list = ["gunting", "batu", "kertas"]
    # Komputer akan menginput data dari
    komputer = random.choice(list)
   
    # Menampilkan Judul Permainan dan inputan pemain
    print()
    print("="*30)
    print("Game Suit Gunting Batu Kertas")
    print("="*30,"\n")
    pemain = input("Masukkan pilihan Gunting, Batu, Kertas ? : ")

    # Jika Pemain dan Komputer bermain dan hasilnya Seri
    if pemain.lower() == komputer:
      print()
      print("="*25)
      print("Hasil suit Seri!")
      print("="*25,"\n")

    # Jika selain itu Pemain menggunakan pilihan gunting  
    elif pemain.lower() == "gunting":

        #Jika Pemain memilih gunting dan komputer memilih batu maka pemain kalah dari komputer
        if komputer == "batu":
          print()
          print("="*25)
          print("Yahh kamu kalah :(")
          print()
          print("Kamu     =", pemain, "\nKomputer = ", komputer)
          print()
          print("Nice Try Kawan")
          print("="*25,"\n")
        
        #Selain itu Pemain memilih gunting dan komputer memilih kertas maka pemain menang dari komputer
        else:
          print()
          print("="*25)
          print("Horee kamu menang :)")
          print()
          print("Kamu     =", pemain, "\nKomputer = ", komputer)
          print()
          print("Well Played Bro")
          print("="*25,"\n")

    # Jika selain itu Pemain menggunakan pilihan batu  
    elif pemain.lower() == "batu":

        #Jika Pemain memilih batu dan komputer memilih kertas maka pemain kalah dari komputer
        if komputer == "kertas":
          print()
          print("="*25)
          print("Yahh kamu kalah :(")
          print()
          print("Kamu     =", pemain, "\nKomputer = ", komputer)
          print()
          print("Nice Try Kawan")
          print("="*25,"\n")

        #Selain itu Pemain memilih batu dan komputer memilih gunting maka pemain menang dari komputer
        else:
          print()
          print("="*25)
          print("Horee kamu menang :)")
          print()
          print("Kamu    =", pemain, "\nKomputer = ", komputer)
          print()
          print("Well Played Bro")
          print("="*25,"\n")

    # Jika selain itu Pemain menggunakan pilihan kertas  
    elif pemain.lower() == "kertas":

        #Jika Pemain memilih kertas dan komputer memilih gunting maka pemain kalah dari komputer
        if komputer == "gunting":
          print()
          print("="*25)
          print("Yahh kamu kalah :(")
          print()
          print("Kamu    =", pemain, "\nKomputer = ", komputer)
          print()
          print("Nice Try Kawan")
          print("="*25,"\n")

        #Selain itu Pemain memilih kertas dan komputer memilih batu maka pemain menang dari komputer
        else:
          print()
          print("="*25)
          print("Horee kamu menang :)")
          print()
          print("Kamu    =", pemain, "\nKomputer = ", komputer)
          print()
          print("Well Played Bro")
          print("="*25,"\n")
    
    # Selain dari pilihan dari List diatas maka akan mengeluarkan output seperti berikut
    else:
        print("-"*35)
        print("Pilihan yang kamu masukan salah")
        print("-"*35)

    # Membuat outputan pilihan y/n
    pilihan = input("Apakah kamu ingin bermain kembali? y/n = ")
    print()

    # Jika pilihan n atau berhenti maka akan mengeluarkan output sebagai berikut
    if pilihan == "n" :
        print("-"*35)
        print("Permainan Berhenti")
        print("Terima Kasih untuk Permainannya")
        print("-"*35)
        print()
        break

    # Selain itu pilihan y akan mengeluarkan output sebagai berikut
    elif pilihan == "y" :
        print("-"*25)
        print("Ayo Bermain Lagi")
        print("-"*25)
