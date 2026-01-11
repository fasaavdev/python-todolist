lines = "_______________________"
bold = "\033[1m"
unbold = "\033[0m"
tugas = []

def menu():
    menu = f"1. {bold}Masukkan Tugas{unbold} \n2. {bold}Tugas Selesai{unbold} \n3. {bold}List Tugas{unbold} \n4. {bold}Keluar{unbold}"
    print(f"\n\n{lines}\n{bold}TUGAS.PY by FasaavDev{unbold}\n{lines}\n\n{menu}\n\n{lines}")
    return
    
def tugas_in():
    nama_tugas = input("Masukkan Nama Tugas: ")
    tugas.append("[   ]" + nama_tugas)
    print(f"{lines}\n\nTugas {nama_tugas} berhasil ditambahkan.\nSemangat!! proud of u :)\n{lines}")
    
def tugas_out():
    if len(tugas) == 0:
        print(f"\n\n{lines}\n\nTidak ada tugas sekarang!\nGood Job!\n\n{lines}")
        return    
    
    print("\n")
    for i in range(len(tugas)):
        print(f"{i + 1}" + ". " + tugas[i])
    pilihan = input(f"Masukkan Nomor Tugas: ")
        
    if not pilihan.isdigit():
        print(f"{lines}\n\nInput kamu tidak valid, lho!\nPastikan kamu menggunakan digit nomor dan ada nomornya di list tugas. :)\n\n{lines}")
        return

    if int(pilihan) <= 0:
        print(f"{lines}\n\nInput kamu tidak valid, lho!\nPastikan kamu mencari diatas 0 dan ada nomornya di list tugas. :(\n\n{lines}")
        return
        
    if int(pilihan) > len(tugas):
        print(f"{lines}\n\nInput yang kamu masukkan tidak ada di list, lho!\nPastikan ada nomornya di list tugas ya! :)\n\n{lines}")
        return
               
    pop = int(pilihan) - 1
    tugas_lama = tugas[pop] 
    nama_tugas = tugas_lama[5:]
    tugas[pop] = tugas[pop].replace("[   ]","[ X ]",1)
    print(f"\n\n{lines}\n\n{nama_tugas} telah diselesaikan.\nYeayy, kamu keren!\n{lines}")
    return
    
    

def tugas_list():
    range_check = len(tugas)
    if range_check <= 0:
        print(f"\n\n{lines}\n\nTidak ada tugas sekarang!\nGood Job!\n\n{lines}")
    for i in range(len(tugas)):
        print(f"{i + 1}" + ". " + tugas[i])
        return
        
        
while True:
    menu()
    pilihan = input("Balas: ")
    if pilihan == "1":
        tugas_in()
    elif pilihan == "2":
        tugas_out()
    elif pilihan == "3":
        tugas_list()
    elif pilihan == "4":
        break
    else:
        print(f'\n\n{lines}\n\nMenu tidak valid\nPilih angka yang ada di menu ya! :(\n\nContoh : "1" \n\n{lines}')
