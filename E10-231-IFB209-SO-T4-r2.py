import datetime
import time
import sys

database = {"E10": "123"}
file_database = {}


# Function awal booting, POST
def check_memory1():
    # Simulasi cek memori
    print("Checking Memory Slot 1...")
    time.sleep(2)


# Add similar functions for check_memory2, check_memory3, and check_memory4
def check_memory2():
    # Simulasi cek memori
    print("Checking Memory Slot 2...")
    time.sleep(2)


def check_memory3():
    # Simulasi cek memori
    print("Checking Memory Slot 3...")
    time.sleep(2)


def check_memory4():
    # Simulasi cek memori
    print("Checking Memory Slot 4...")
    time.sleep(2)


def so_initialization():
    # Simulasi cek memori
    print("Sistem Operasi Initialization...")
    time.sleep(2)


def display_info():
    print()
    print("Spesifikasi : ")
    print("Intel I5 13400F")
    print("Intel RTX 3050")
    print("Asrock B760M PRO RS/D4")
    print("RAM DELTA RGB DDR4 32 GB of 4 Slot Memory")
    print("Memory slot 1 use 7,5 GB free of 8 GB")
    print("Memory slot 2 use 5 GB free of 8 GB")
    print("Memory slot 3 use 0.9 GB free of 8 GB")
    print("Memory slot 4 use 0 GB free of 8 GB")
    print("SSD WD Black SN850", end='')
    print("SSD use 12,5 GB free of 1 TB ")


# Main program POST
def POST():
    print("Microsoft Windows [Version 10.0.22631.2715]")
    print("(c) Microsoft Corporation. All rights reserved.")
    for i in range(1, 101):
        print(f"System Check Progress: {i}%", end="\r")
        time.sleep(0.1)  # Adjust the sleep time as needed for the desired speed

    print("\n")  # Move to the next line

    # Call the memory check functions
    check_memory1()
    check_memory2()
    check_memory3()
    check_memory4()
    so_initialization()
    display_info()


if __name__ == "__main__":
    POST()


def belum_login():
    print("\n")
    while True:
        user_input = input("Users > ")
        if user_input.lower() == 'help':
            print("1. login")
            print("2. help")
        elif user_input.lower() == 'login':
            nama_pengguna = input("Username : ")
            kata_sandi = input("Password : ")
            if nama_pengguna in database and database[nama_pengguna] == kata_sandi:
                print("Login berhasil")
                main(nama_pengguna)
                break
            else:
                print("Nama pengguna atau kata sandi salah.")
        else:
            print("Anda belum login. Silahkan login terlebih dahulu")


def help_menu():
    print("Perintah:")
    print("help     - Tampilkan perintah yang tersedia")
    print("dir      - Daftar isi direktori")
    print("del      - Hapus file")
    print("mkdir    - Buat direktori baru")
    print("mkfil    - Buat file baru")
    print("cls      - clear screen ")
    print("exit     - Keluar program")


def dir_menu():
    for timestamp, file_content in file_database.items():
        print(f"{timestamp} {file_content}")


def delete_file(file_path):
    global file_database

    try:
        file_to_delete_name = file_path.strip()[4:]
        if file_to_delete_name in file_database.values():
            file_database = {key: val for key, val in file_database.items() if val != file_to_delete_name}
            print(f"File '{file_to_delete_name}' berhasil dihapus.")
        else:
            print(f"File '{file_to_delete_name}' tidak ditemukan dalam database.")
    except PermissionError:
        print(f"Tidak diizinkan untuk menghapus file '{file_to_delete_name}'.")
    except Exception as e:
        print(f"Error: {e}")





def mkdir_menu(file_content):
    _, file_content = file_content.split(' ', 2)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_database[timestamp] = file_content
    print(f"Directory '{file_content}' berhasil dibuat")


def mkfil(file_content):
    _, file_content = file_content.split(' ', 2)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_database[timestamp] = file_content
    print("file berhasil disimpan")


def clear_screen():
    print("\033[2J\033[H", end="")


def main(username):
    while True:
        user_input = input(f"C:\\Users\\{username}>")

        if user_input == "help":
            help_menu()

        elif user_input == "dir":
            dir_menu()


        elif user_input.startswith('del '):
            delete_file(user_input)

        elif user_input.startswith('mkdir '):
            mkdir_menu(user_input)

        elif user_input.startswith('mkfil '):
            mkfil(user_input)

        elif user_input == "cls":
            clear_screen()

        elif user_input == "exit":
            sys.exit()

        else:
            print(f"Command '{user_input}' not recognized. Please enter a valid command.")


if __name__ == "__main__":
    belum_login()
