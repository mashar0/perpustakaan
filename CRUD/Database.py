from os import rename, system
Nama_database = "DATA/KumpulanBuku.txt"
Nama_sample_start = "DATA/Sample.html"
Nama_html = "DATA/KumpulanBuku.html"

def Initialize(): 
	with open(Nama_database, mode="a", encoding="utf-8") as buku: buku.write("")

def lihat_buku_console():
	with open(Nama_database, mode="r", encoding='utf-8') as lihat_buku: return lihat_buku.readlines()

def tambah_buku_console(judul, pengarang, tahun_terbit, halaman):
	with open(Nama_database, mode="a", encoding="utf-8") as tambah_file:
		info_buku = f"{judul:<250}|{pengarang:<250}|{tahun_terbit:<250}|{halaman:<250}\n"
		tambah_file.write(info_buku)

def update_buku_console(no_buku, posisi, data_baru):
	posisi_sebenarnya = ((no_buku-1)*1004)+posisi
	with open(Nama_database, mode="r+", encoding="utf-8") as update_file:
		update_file.seek(posisi_sebenarnya)
		update_file.write(data_baru)

def hapus_buku_console(no_buku):
	with open(Nama_database, mode="r", encoding="utf-8") as file:
		isi = file.readlines()
		if (len(isi) == 1): return True
		else:
			for i in range(len(isi)):
				if (i == (no_buku-1)): continue
				with open("CRUD/temp.txt", mode="a", encoding="utf-8") as files: files.write(isi[i])
			rename("CRUD/temp.txt", Nama_database)

def open_sample_start():
	with open(Nama_sample_start, mode="r") as read_sample:
		return read_sample.read()

def tulis_html():
	sample_start, data_buku_table, no = open_sample_start(), lihat_buku_console(), 0
	with open(Nama_html, mode="w", encoding="utf-8") as table:
		table.write(sample_start)
		table.seek(473)
		for i in data_buku_table:
			no += 1
			data_buku_berbentuk_list = i.split("|")
			text_html_baru = f"""			
		<tr>
            <td>{no}</td>
            <td>{data_buku_berbentuk_list[0]}</td>
            <td>{data_buku_berbentuk_list[1]}</td>
            <td>{data_buku_berbentuk_list[2]}</td>
			<td>{data_buku_berbentuk_list[3]}</td>
        </tr>
			"""
			table.write(text_html_baru)
		sample_end = """
	</table>
	</body>
</html>"""
		table.write(sample_end)
		lanjut = str(input("Membuka Browser ? [Y/n] : "))
		if (lanjut == "y") or (lanjut == "Y"):
			system("xdg-open DATA/KumpulanBuku.html")
		else:
			pass
