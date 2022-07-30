# Program Sederhana Nasabah Bank

# Modul CSV untuk membaca dan menulis file CSV
import csv

# Modul Os untuk membersihkan layar
import os
os.system('cls')

# Menyiapkan variabel untuk menentukan file CSV yang akan digunakan
csv_filename = 'nasabah.csv'

# Membuat fungsi 'show_menu' yang akan menampilkan daftar menu dan menjalankan fungsi tertentu sesuai dengan menu yang dipilih user
def show_menu():
    print("==========================================")
    print("^^^^^ SELAMAT DATANG DI SYARIAH BANK ^^^^^")
    print("==========================================")
    print()
    print("MENU :")
    print()
    print("[1] Buka Rekening")
    print("[2] Cek Saldo")
    print("[3] Tarik Tunai")
    print("[4] Transfer")
    print("[5] Setoran Tunai")
    print("[6] Donasi")
    print("[0] Exit")
    print()
    print("------------------------")
    selected_menu = input("Masukkan Pilihan : ")
    print("------------------------")
    print()
    
    if(selected_menu == "1"):
        buka_rekening()
    elif(selected_menu == "2"):
        cek_saldo()
    elif(selected_menu == "3"):
        tarik_tunai()
    elif(selected_menu == "4"):
        tranfer()
    elif(selected_menu == "5"):
        setoran_tunai()
    elif(selected_menu == "6"):
        donasi()
    elif(selected_menu == "0"):
        exit()
    else:
        print("-"*30)
        print("Kamu memilih menu yang salah!")
        print("-"*30)
        back_to_menu()

# Membuat fungsi 'back_to_menu' untuk kembali ke menu utama 
def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    print()

    show_menu()

# Membuat fungsi buka_rekening, meminta user untuk menginputkan data baru
# Dan akan ditulis ke dalam file CSV
def buka_rekening():
    print("---Buka Rekening---")
    print()
    with open(csv_filename, mode='a') as csv_baca:
        fieldnames = ['Nomor Rekening', 'Nama Nasabah', 'Saldo saat ini']
        writer = csv.DictWriter(csv_baca, fieldnames=fieldnames)

        nomor = input("Nomor Rekening : ")
        nama  = input("Nama Nasabah   : ")
        saldo = input("Setoran Awal   : ")

        writer.writerow({'Nomor Rekening' : nomor, 'Nama Nasabah' : nama, 'Saldo saat ini' : saldo})
        print("Pembukaan rekening dengan nomor",nomor,"atas nama",nama,"berhasil.")

    back_to_menu()

# Membuat fungsi cek_saldo, yang akan membaca inputan user dan menampilkan jumlah saldo user
def cek_saldo():
    print("---Cek Saldo---")
    print()
    print("-"*15)
    n = int(input("Rp. "))
    print("-"*15)
    print("Saldo yang Anda miliki adalah Rp.",n) 

    back_to_menu()

# Membuat fungsi tarik_tunai, yang akan membaca inputan user dan menampilkan jumlah saldo yang diambil
def tarik_tunai():
    print("---Tarik Tunai---")
    print()
    print("-"*15)
    n = int(input("Rp. "))
    print("-"*15)
    print()
    nominal = int(input("Masukkan Nominal : Rp. "))
    if nominal > n:
        print("Nominal yang Anda masukkan Tidak Cukup!")
    else:
        proses = n - nominal
        print("Saldo Anda berhasil diambil Rp.",nominal)
        print("-"*30)
        print("Saldo Sisa : Rp.", proses)
        print("-"*30)
      
    back_to_menu()

# Membuat fungsi transfer, yang akan menerima inputan user dan akan menampilkan jumlah transfer yang dikirim ke penerima nanti
def tranfer():
    print("---Transfer---")
    print()
    print("-"*15)
    n = int(input("Rp. "))
    print("-"*15)
    print("Masukkan Tujuan !")
    nama = str(input("Nama             : "))
    no   = (input("No. Rekening     : "))
    nominal = int(input("Masukkan Nominal : Rp. "))
    if nominal > n:
        print("Nominal yang Anda masukkan Tidak Cukup !")
    else:
        proses = n - nominal
        print("Anda Berhasil Transfer ke",nama,"Sebesar Rp.",nominal)
        print("-"*30)
        print("Saldo Sisa : Rp.", proses)
        print("-"*30)

    back_to_menu()

# Membuat fungsi setoran_tunai, yang akan menerima inputan user dan menampilkan jumlah saldo yang dimasukkan
def setoran_tunai():
    print("---Setoran Tunai---")
    print()
    print("-"*15)
    n = int(input("Rp. "))
    print("-"*15)
    print()
    nominal = int(input("Masukkan Nominal : Rp. "))
    proses = n + nominal
    print("-"*30)
    print("Jumlah Saldo Anda sekarang adalah Rp.", proses)
    print("-"*30)

    back_to_menu()

# Membuat fungsi donasi, yang akan menerima inputan user dan menampilkan jumlah donasi yang dikirim ke penerima nanti
def donasi():
    print("---Donasi---")
    print()
    print("-"*15)
    n = int(input("Rp. "))
    print("-"*15)
    print()
    print("Masukkan Tujuan !")
    print("-"*20)
    nama = str(input("Nama             : "))
    no   = (input("No. Rekening     : "))
    pesan= str(input("Pesan            : "))
    nominal = int(input("Masukkan Nominal : Rp. "))
    if nominal > n :
        print("Nominal yang Anda masukkan Tidak Cukup !")
    else:
        proses = n - nominal
        print("Anda Berhasil Donasi ke",nama,"Sebesar Rp.",nominal)
        print("-"*30) 
        print("Saldo Sisa : Rp.", proses)
        print("-"*30) 

    back_to_menu()

# Membuat fungsi exit, sebagai penutup dari program nasabah bank diatas
def exit():
    print("Terima Kasih untuk Kunjungan Anda...")
    print()

back_to_menu()