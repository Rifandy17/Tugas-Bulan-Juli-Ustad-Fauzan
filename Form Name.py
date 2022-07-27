# print("="*11)
# print("Form Name")
# print("="*11)
# print()


# username = input("Masukkan Username      :   ")

# if(len(username) > 9 and " " not in username) == True:
#     status = "Username berhasil di validasi"
# else:
#     status = "Username tidak valid"
#     username = username.capitalize()

# print(status)
# print(username)
# print()

# email = input("Masukkan Email         :   ")

# if ("@" and "." in email) == True:
#     status = "Email berhasil di validasi"
# else:
#     status = "Email tidak valid"

# print(status)
# nomor = input("Masukkan Nomor         :   ")

# if nomor.isdigit() == True:
#     status = "Nomor Berhasil di validasi"
# else:
#     status = "Nomor tidak valid"

# print(status)
# print()

import os
os.system('cls')

status = ''

def username() :
    print("="*40)
    inputan = input("Masukkan Username : ")
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3 = inputan.capitalize()

    if cek1 > 9 and cek2 == False and cek3 == inputan :
        status = "Berhasil"
        return inputan, status
    else :
        inputan = "Username tidak valid"
        status = "Gagal"
        return inputan, status

def email() :
    inputan = input("Masukkan Email    : ")
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3 = '@' and '.' in inputan

    if cek1 > 7 and cek2 == False and cek3 == True :
        status = "Berhasil"
        return inputan, status
    else :
        inputan = "Email tidak valid"
        status = "Gagal"
        return inputan, status

def nomor_Hp() :
    inputan = str(input("Masukkan Nomor Hp : "))
    cek1 = len(inputan)
    cek2 = ' ' in inputan

    if cek1 < 13 and cek2 == False :
        status = "Berhasil"
        return inputan, status
    else :
        inputan = "Nomor tidak valid"
        status = "Gagal"
        return inputan, status
 
def main() :
    while True :
        u1, u2 = username()
        print("\nUsername   = ", u1)
        print("Status     = ", u2)
        print("="*40)
        if u2 == "Berhasil" :
            break
        


    while True :
        e1, e2 = email()
        print("\nEmail      = ", e1)
        print("Status     = ", e2)
        print("="*40)
        if e2 == "Berhasil" :
            break



    while True :
        n1, n2 = nomor_Hp()
        print("\nNomor Hp   = ", n1)
        print("Status     = ", n2)
        print("="*40)
        if n2 == "Berhasil" :
            break


main()