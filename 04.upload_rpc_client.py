# import xmlrpc bagian client
import xmlrpc.client

# buat stub proxy client
proxy = xmlrpc.client.ServerProxy("172.20.10.4:8001/")

# buka file yang akan diupload
with open("file_diupload.txt",'rb') as handle:
    # baca file dan ubah menjadi biner dengan xmlrpc.client.Binary
    upload = xmlrpc.client.Binary(handle.read())

# panggil fungsi untuk upload yang ada di server
proxy.upload(upload)
