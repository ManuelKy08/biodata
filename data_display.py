import json
import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)

# Kelas untuk menyimpan data pengguna
class User:
    def __init__(self, name, gender, address, phone, social_media):
        self.name = name
        self.gender = gender
        self.address = address
        self.phone = phone
        self.social_media = social_media

    def __str__(self):
        return (f"Nama: {self.name}\n"
                f"Jenis Kelamin: {self.gender}\n"
                f"Alamat: {self.address}\n"
                f"Nomor Telepon: {self.phone}\n"
                f"Akun Media Sosial: {self.social_media}\n")

# Fungsi untuk menampilkan banner
def display_banner():
    banner_text1 = """
██╗  ██╗ ██████╗ ██╗  ██╗ ██████╗ ██╗  ██╗     ███████╗███████╗ ██████╗
██║ ██╔╝██╔═══██╗██║ ██╔╝██╔═══██╗██║ ██╔╝     ██╔════╝██╔════╝██╔════╝
█████╔╝ ██║   ██║█████╔╝ ██║   ██║█████╔╝█████╗███████╗█████╗  ██║     
██╔═██╗ ██║   ██║██╔═██╗ ██║   ██║██╔═██╗╚════╝╚════██║██╔══╝  ██║     
██║  ██╗╚██████╔╝██║  ██╗╚██████╔╝██║  ██╗     ███████║███████╗╚██████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚══════╝╚══════╝ ╚═════╝ 
           Menampilkan dan Menambahkan Biodata
    """
    banner_text2 = """
     ====================================================================
     **                  Instagram : @risky.manuel                     **
     **                  Telegram  : @kikikokok9                       **
     **                  Email     : riskymanuel08@proton.me           **
     ====================================================================
    """
    print(banner_text1)
    print(banner_text2)

# Fungsi untuk membaca data dari file
def read_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [User(**item) for item in data]
    except FileNotFoundError:
        logging.error(f"File {filename} tidak ditemukan.")
        return []
    except json.JSONDecodeError:
        logging.error(f"File {filename} tidak dapat dibaca sebagai JSON.")
        return []

# Fungsi untuk menulis data ke file
def write_data_to_file(filename, data):
    with open(filename, 'w') as file:
        json.dump([user.__dict__ for user in data], file, indent=4)

# Fungsi untuk menemukan biodata
def find_biodata(data, username):
    result = [entry for entry in data if entry.name.lower() == username.lower()]
    return result[0] if result else None

# Fungsi untuk menambah pengguna
def add_user(data):
    name = input("Nama: ")
    gender = input("Jenis Kelamin: ")
    address = input("Alamat: ")
    phone = input("Nomor Telepon: ")
    social_media = input("Akun Media Sosial: ")

    new_user = User(name, gender, address, phone, social_media)
    data.append(new_user)
    write_data_to_file('data.json', data)
    print("Data berhasil ditambahkan!")

# Fungsi untuk menampilkan data
def display_data(biodata):
    if biodata:
        print(biodata)
    else:
        print("Biodata tidak ditemukan.")

# Fungsi untuk menampilkan menu
def show_menu():
    print("\nMenu:")
    print("1. Tampilkan biodata")
    print("2. Tambah biodata")
    print("3. Keluar")

# Fungsi utama
def main():
    display_banner()  # Menampilkan banner saat program dijalankan
    filename = 'data.json'
    data = read_data_from_file(filename)

    while True:
        show_menu()
        choice = input("Pilih tindakan (1/2/3): ")

        if choice == '1':
            username = input("Masukkan nama pengguna: ")
            biodata = find_biodata(data, username)
            display_data(biodata)
        elif choice == '2':
            add_user(data)
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
