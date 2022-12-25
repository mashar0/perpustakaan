from os import system
from sys import platform
from .Database import *

class Pekerja_perpustakaan:
	__banner = """Selamat Datang Di Perpustakaan . . .
Ada Yang Bisa Saya Bantu ?
1 . Lihat Buku
2 . Tambah Buku
3 . Perbaharui Informasi Buku
4 . Buang Buku
5 . Keluar Program
	"""

	def __init__(self, masukan_nama):
		self.banner = Pekerja_perpustakaan.__banner
		self.nama = masukan_nama

	def clear(self):
		if (platform == "linux") or (platform == "linux2"): system("clear")
		elif (platform == "win32"): system("cls")
		else: pass
    
	def ada_yang_bisa_dibantu(self):
		while True:
			self.clear()
			print(f"Hallo Nama Saya {self.nama}\n{self.banner}")
			try:
				no_bantuan = int(input("> "))
				if (no_bantuan <= 0) or (no_bantuan > 5): continue  
				else: return no_bantuan
			except: continue

	def table_buku(self, message):
		self.clear()
		no = 0
		data_lihat_buku = lihat_buku()
		print(f"{message}\n\nTersedia {len(data_lihat_buku)} Buku")
		print('='*99)
		print(f"| {'No':<4}| {'Judul':<20} | {'Pengarang':<20} | {'Tahun Terbit':<20} | {'Jumlah Halaman':<20} |")
		print("|" + '~'*97 + "|")
		for i in data_lihat_buku:
			iSp = i.split("|")
			no += 1
			print(f"| {no:^4}| {iSp[0]:.20} | {iSp[1]:.20} | {iSp[2]:.20} | {iSp[3]:.20} |")
		print('='*99)

	def mau_lihat_buku(self):
		self.table_buku("Lihat Buku")
		input("Enter Untuk Melanjutkan ")

	def mau_tambah_buku(self):
		while True:
			while True:
				self.clear()
				print("Tambahkan Buku Baru")
				judul = str(input(f"{'Judul':<15}: "))
				if (len(judul.strip(" ")) > 0): break  
				else:
					input("Harap Masukan Judul ! ")
					continue
			while True:
				self.clear()
				print("Tambahkan Buku Baru")
				print(f"{'Judul':<15}: {judul}")
				pengarang = str(input(f"{'Pengarang':<15}: "))
				if (len(pengarang.strip(" ")) > 0): break  
				else:
					input("Harap Masukan Nama Pengarang  ! ")
					continue
			while True:
				self.clear()
				print("Tambahkan Buku Baru")
				print(f"{'Judul':<15}: {judul}")
				print(f"{'Pengarang':<15}: {pengarang}")
				try:
					tahun_terbit = int(input(f"{'Tahun Terbit':<15}: "))
					break
				except:
					input("Masukan Angka ! ")
					continue
			while True:
				self.clear()
				print("Tambahkan Buku Baru")
				print(f"{'Judul':<15}: {judul}")
				print(f"{'Pengarang':<15}: {pengarang}")
				print(f"{'Tahun Terbit':<15}: {tahun_terbit}")
				try:
					jumlah_halaman = int(input(f"{'Jumlah Halaman':<15}: "))
					break
				except:
					input("Masukan Angka ! ")
					continue 
			tambah_buku(judul, pengarang, tahun_terbit, jumlah_halaman)
			print("\nBuku Sudah Di Tambahkan")
			tambah_lagi = str(input("Tambah Buku Lagi ? [Y/n] : "))
			if (tambah_lagi == "y") or (tambah_lagi == "Y"): continue 
			else: break

	def mau_update_buku(self):
		while True:
			while True:
				data_lihat_buku = lihat_buku()
				self.table_buku("Update Buku")
				print("Input 0 Untuk Selesai\n")
				try:
					no_buku_yg_akan_diubah = int(input("No Buku Yang Akan Di Ubah\n> "))
					if (no_buku_yg_akan_diubah > len(data_lihat_buku)) or (no_buku_yg_akan_diubah < 0): continue
					elif (no_buku_yg_akan_diubah == 0): break
					else: break
				except: continue
			if (no_buku_yg_akan_diubah == 0): break
			while True:
				data_lihat_buku = lihat_buku()
				data_lihat_buku_list = data_lihat_buku[no_buku_yg_akan_diubah-1].split("|")
				self.clear()
				print(f"Ubah Buku No {no_buku_yg_akan_diubah}")
				print("="*21)
				print(f"1 . {'Judul':<15} : {data_lihat_buku_list[0]:.30} ")
				print(f"2 . {'Pengarang':<15} : {data_lihat_buku_list[1]:.30} ")
				print(f"3 . {'Tahun Terbit':<15} : {data_lihat_buku_list[2]:.30} ")
				print(f"4 . {'Halaman':<15} : {data_lihat_buku_list[3]:.30} ")
				print("5 . Ubah Selesai")
				print("="*21)

				try:
					bagian_yang_akan_di_ubah = int(input("Apa Yang Akan Di Ubah\n> "))
					if (bagian_yang_akan_di_ubah < 1) or (bagian_yang_akan_di_ubah > 6): continue 
					elif (bagian_yang_akan_di_ubah == 1):
						while True:
							self.clear()
							judul_baru = str(input("Masukan Judul Baru\n> "))
							if (len(judul_baru.strip(" ")) > 0):
								data_judul_baru = f"{judul_baru:<250}|"
								update_buku(no_buku=no_buku_yg_akan_diubah ,posisi=0 , data_baru=data_judul_baru)
								break
							else:
								input("Harap Masukan Judul ! ")
								continue
					elif (bagian_yang_akan_di_ubah == 2):
						while True:
							self.clear()
							pengarang_baru = str(input("Masukan Nama Pengarang Yang Baru\n> ")) 
							if (len(pengarang_baru.strip(" ")) > 0):
								data_pengarang_baru = f"{pengarang_baru:<250}|"
								update_buku(no_buku=no_buku_yg_akan_diubah ,posisi=251 , data_baru=data_pengarang_baru)
								break
							else:
								input("Harap Masukan Nama Pengarang ! ")
								continue
					elif (bagian_yang_akan_di_ubah == 3):
						while True:
							self.clear()
							try:
								tahun_terbit_baru = int(input("Tahun Terbit Baru\n> ")) 
								break
							except: 
								input("Masukan Angka ! ")
								continue
						data_tahun_terbit_baru = f"{tahun_terbit_baru:<250}|"
						update_buku(no_buku=no_buku_yg_akan_diubah ,posisi=502 , data_baru=data_tahun_terbit_baru) 
					elif (bagian_yang_akan_di_ubah == 4):
						while True:
							self.clear()
							try:
								halaman_baru = int(input("Masukan Jumlah Halaman Baru\n> "))
								break 
							except: 
								input("Masukan Angka ! ")
								continue
						data_halaman_baru = f"{halaman_baru:<250}\n"
						update_buku(no_buku=no_buku_yg_akan_diubah ,posisi=753 , data_baru=data_halaman_baru)
						continue
					elif (bagian_yang_akan_di_ubah == 5): break
					else: continue
				except: continue

	def mau_hapus_buku(self):
		while True:
			data_lihat_buku = lihat_buku()
			self.table_buku("Hapus Buku")
			print("Input 0 Untuk Selesai\n")
			try:
				no_buku_yang_akan_di_hapus = int(input("Pilih No Buku Yang Akan Di Hapus\n> "))
				if (no_buku_yang_akan_di_hapus > len(data_lihat_buku)): continue
				elif (no_buku_yang_akan_di_hapus == 0): break
				else:
					if hapus_buku(no_buku=no_buku_yang_akan_di_hapus): 
						input("Tidak Dapat Menghapus Buku Terakhir ! ")
					else: continue
			except: continue

	def bantuan(self, kode_bantuan):
		if (kode_bantuan == 1): self.mau_lihat_buku()
		elif (kode_bantuan == 2): self.mau_tambah_buku()
		elif (kode_bantuan == 3): self.mau_update_buku()
		elif (kode_bantuan == 4): self.mau_hapus_buku()
		elif (kode_bantuan == 5): return True
		else: pass

	def minta_bantuan(self):
		while True:
			kode_bantuan = self.ada_yang_bisa_dibantu()
			if (self.bantuan(kode_bantuan)): break