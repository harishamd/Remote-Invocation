# import xmlrpc bagian client saja
import xmlrpc.client

# buat stub (proxy) untuk client
s = xmlrpc.client.ServerProxy('172.20.10.3:8000')

# lakukan pemanggilan fungsi vote("nama_kandidat") yang ada di server
s.vote("Haris")
s.vote("Nissa")
s.vote("Nissa")
s.vote("Lord")
s.vote("Haris")
s.vote("Haris")
s.vote("Lord")
s.vote("Haris")
# lakukan pemanggilan fungsi querry() untuk mengetahui hasil persentase dari masing-masing kandidat
s.result()

# lakukan pemanggilan fungsi lain terserah Anda