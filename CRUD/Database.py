from os import rename
Nama_database = "CRUD/KumpulanBuku.txt"
Nama_html = "CRUD/KumpulanBuku.html"

def Initialize(): 
	with open(Nama_database, mode="a", encoding="utf-8") as buku: buku.write("")

def lihat_buku():
	with open(Nama_database, mode="r", encoding='utf-8') as lihat_buku: return lihat_buku.readlines()

def tambah_buku(judul, pengarang, tahun_terbit, halaman):
	with open(Nama_database, mode="a", encoding="utf-8") as tambah_file:
		info_buku = f"{judul:<250}|{pengarang:<250}|{tahun_terbit:<250}|{halaman:<250}\n"
		tambah_file.write(info_buku)

def update_buku(no_buku, posisi, data_baru):
	posisi_sebenarnya = ((no_buku-1)*1004)+posisi
	with open(Nama_database, mode="r+", encoding="utf-8") as update_file:
		update_file.seek(posisi_sebenarnya)
		update_file.write(data_baru)

def hapus_buku(no_buku):
	with open(Nama_database, mode="r", encoding="utf-8") as file:
		isi = file.readlines()
		if (len(isi) == 1): return True
		else:
			for i in range(len(isi)):
				if (i == (no_buku-1)): continue
				with open("CRUD/temp.txt", mode="a", encoding="utf-8") as files: files.write(isi[i])
			rename("CRUD/temp.txt", Nama_database)

def lihat_html():
	with open(Nama_html, mode="w", encoding="utf-8") as file:
		pass