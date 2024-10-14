import random 
from prettytable import PrettyTable # Untuk memanggil prettytable

# Dictionary untuk menyimpan data akun admin dan user
akun = {
    'admin' : {'password': 'admin#123', 'role': 'admin'},
    'user' : {'password': 'belajarbahasa', 'role': 'user'}
}

# Fungsi Login
def login():
    while True:
        username = input('Masukkan username: ')
        password = input('Masukkan password: ')
    
        if username in akun and akun[username]['password'] == password:
            print(f'Login berhasil sebagai {akun[username]['role']}')
            return akun[username]['role'] # Mengembalikan role (admin/user)
        else:
            print('login gagal, silahkan coba lagi')
            continue

# Dictionary untuk kosakata yang disimpan
kata = {
    1: {'prancis': 'Au Revoir', 'inggris': 'Goodbye', 'arti': 'Selamat tinggal'},
    2: {'prancis': 'Amusante', 'inggris': 'Funny', 'arti': 'Lucu'},
    3: {'prancis': 'intelligente', 'inggris': 'Smart', 'arti': 'Pintar'},
    4: {'prancis': 'Aiment', 'inggris': 'Love', 'arti': 'Cinta'},
    5: {'prancis': 'Etudiant', 'inggris': 'Student', 'arti': 'Mahasiswa'},
    6: {'prancis': 'Mange', 'inggris': 'Eat', 'arti': 'Makan'},
    7: {'prancis': 'Parle', 'inggris': 'Speak', 'arti': 'berbicara'},
    8: {'prancis': 'Trois', 'inggris': 'Three', 'arti': 'Tiga'},
    9: {'prancis': 'Deux', 'inggris': 'Two', 'arti': 'Dua'},
    10: {'prancis': 'Avec', 'inggris': 'With', 'arti': 'Bersama'}
}

# Fungsi untuk admin
def menu_admin():
    while True:
        print('\n===== Menu Admin =====')
        print('1. Tambah kata')
        print('2. Lihat kata')
        print('3. Update kata')
        print('4. Hapus Kata')
        print('5. Keluar')
        pilih_menu = int(input('Pilih menu: '))
        
        if pilih_menu == 1:
            tambah_kata() # Memanggil fungsi tambah kata
        elif pilih_menu == 2:
            lihat_kata() # Memanggil fungsi lihat kata
        elif pilih_menu == 3:
            update_kata() # Memanggil fungsi update kata
        elif pilih_menu == 4:
            hapus_kata() # Memanggil fungsi hapus kata
        elif pilih_menu == 5:
            print('Berhasil keluar') # Keluar dari Program
            break
        else:
            print('Pilihan tidak valid')
            
# Fungsi untuk admin menambah kata baru 
def tambah_kata():
        if kata:
            no_kata = max(kata.keys()) + 1 # Untuk nomor kata baru
        else:
            no_kata = 1  # Mulai dari 1 jika belum ada kata
        
        # Input admin untuk menambah kata baru
        prancis = input('Masukkan kata bahasa prancis: ')
        inggris = input('Masukkan kata bahasa inggris: ')
        arti = input('Masukkan arti: ')

        # Menambah kata baru ke dictionary kata  
        kata[no_kata] = {'prancis': prancis, 'inggris': inggris, 'arti': arti}
        print(f'Kata baru berhasil ditambahkan dengan NO {no_kata}.')

# Fungsi untuk admin dan user melihat kata 
def lihat_kata():
    print('\n================== Daftar kata ===================')
    
    # Prettytable untuk menampilkan kata dengan tabel
    table = PrettyTable() 
    table.field_names = ['No', 'Prancis', 'Inggris', 'Indonesia'] 

    # Menambahkan kata ke dalam tabel
    for no_kata, kata_item in kata.items():
        table.add_row([no_kata, kata_item['prancis'], kata_item['inggris'], kata_item['arti']])

    print(table)

# Fungsi untuk admin mengupdate kata 
def update_kata():
    lihat_kata() # Menampilkan kata yang ada
    no_kata = int(input('Masukkan nomor kata yang ingin diupdate: '))
       
    if no_kata in kata:
        # Input dari admin untuk mengupdate kata
        prancis = input(f'Masukkan kata bahasa prancis baru: ')
        inggris = input(f'Masukkan kata bahasa inggris baru: ')
        arti = input(f'Masukkan arti baru: ')

        # Mengupdate kata yang ada di dictionary
        kata[no_kata] = {'prancis': prancis, 'inggris': inggris, 'arti': arti}
        print(f'Kata nomor {no_kata} berhasil diperbarui.')
    else:
        print('Nomor kata tidak ditemukan.')
    
# Fungsi untuk admin menghapus 
def hapus_kata():
    lihat_kata() # Menampilkan kata yang ada
    no_kata = int(input('Masukkan nomor kata yang ingin dihapus: '))

    if no_kata in kata:
        del kata[no_kata] # Menghapus kata yang ada di dictionary
        print(f'Kata nomor {no_kata} berhasil dihapus.')
    else:
        print('Nomor kata tidak ditemukan.')
    
# Fungsi untuk user
def menu_user():
    while True:
        print('\n=== Menu User ===')
        print('1. Lihat Kata')
        print('2. Belajar Kata')
        print('3. Logout')
        pilih_menu_user = input('Pilih menu: ')

        if pilih_menu_user == '1':  
            lihat_kata() # Memanggil fungsi lihat kata
        elif pilih_menu_user == '2':
            belajar_kata() # Memanggil fungsi belajar kata   
        elif pilih_menu_user == '3':
            print('Berhasil keluar') # Keluar dari program
            break 
        else:
            print('Pilihan tidak valid!')

# Fungsi untuk user belajar kata (Kuis)
def belajar_kata():
    print('\n============ Kuis belajar kata ==============')
    
    # Mengambil kata secara acak
    soal = random.choice(list(kata.values()))
    jawaban_benar = soal['arti'] # Jawaban benar

    # Membuat pilihan acak
    pilihan = random.sample([k['arti'] for k in kata.values() if k['arti'] != jawaban_benar], 2)
    pilihan.append(jawaban_benar)
    random.shuffle(pilihan) # Agar pilihan jawaban teracak

    print(f"Apa arti dari kata bahasa Prancis '{soal['prancis']}'")

    # Menampilkan pilihan jawaban
    for i in range(1, len(pilihan) + 1):  #
        print(f'{i}. {pilihan[i - 1]}')
    
    jawaban_user = int(input('Pilih jawaban (1/2/3): ')) # User memasukkan jawaban

    # Mengecek jawaban apakah benar atau salah
    if pilihan[jawaban_user - 1] == jawaban_benar:
        print('Jawaban benar!') # Untuk apabila jawaban benar
    else:
        print(f'Jawaban salah. Yang benar adalah: {jawaban_benar}') # Jika jawaban salah maka akan ditunjukkan jawaban yang benar

                
# Fungsi utama
def main():
    print('=== Selamat datang di Program Pembelajaran Bahasa ===')
    role = login() # Memanggil fungsi login

    if role == 'admin':
        menu_admin() # Memanggil fungsi menu admin
    elif role == 'user':
        menu_user() # Memanggil fungsi menu user
    else:
        print('Login gagal. Silakan coba lagi.') # Jika role selain admin dan user
        
# Menjalankan Program
main()  