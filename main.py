from CRUD import *

if __name__ == "__main__":
	Initialize()
	pekerja = Pekerja_perpustakaan(masukan_nama="Tatang") 
	pekerja.minta_bantuan()
	print("Program Berakhir Terima Kasih")