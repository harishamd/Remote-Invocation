# import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# import SimpleXMLRPCRequestHandler

import threading

# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Buat server
with SimpleXMLRPCServer(('172.20.10.4', 8000), requestHandler = RequestHandler) as server :

    # buat data struktur dictionary untuk menampung nama_kandidat dan hasil voting
    data = [["Haris", 0],["Nissa", 0],["Lord", 0]]
    tidak_sah = [0]
    
    # kode setelah ini adalah critical section, menambahkan vote tidak boeh terjadi race condition
    # siapkan lock
    lock = threading.Lock()
    
    #  buat fungsi bernama vote_candidate()
    def vote_candidate(x):
        if (x == data [0][0]):
            data[0][1] = data[0][1] +1
        elif (x == data[1][0]):
            data[1][1] = data[1][1] +1
        elif (x == data [2][0]):
            data[2][1] = data[2][1] +1
        else :
            tidak_sah[0] +1
        print(data)
        
        # critical section dimulai harus dilock
        lock.acquire()
        # jika kandidat ada dalam dictionary maka tambahkan  nilai votenya
        
        
        # critical section berakhir, harus diunlock
        lock.release()
        return True
        
    
    # register fungsi vote_candidate() sebagai vote
    server.register_function(vote_candidate, "vote")

    # buat fungsi bernama querry_result
    def querry_result():
        persen_haris = (data[0][1]/(data[0][1]+data[1][1]+data[2][1]+tidak_sah[0]))*100
        persen_nisa = (data[1][1]/(data[0][1]+data[1][1]+data[2][1]+tidak_sah[0]))*100
        persen_lord = (data[2][1]/(data[0][1]+data[1][1]+data[2][1]+tidak_sah[0]))*100
        print("Nama : ", data[0][0])
        print("Hasil Vote : ", persen_haris, "%")
        print("Nama : ", data[1][0])
        print("Hasil Vote : ", persen_nisa, "%")
        print("Nama : ", data[2][0])
        print("Hasil Vote : ", persen_lord, "%")



        # critical section dimulai
        lock.acquire()
        
        # hitung total vote yang ada
        
        
        # hitung hasil persentase masing-masing kandidat
        
        
        # critical section berakhir
        lock.release()
        return True    
        
    # register querry_result sebagai querry
    server.register_function(querry_result,"result")


    print ("Server voting berjalan...")
    # Jalankan server
    server.serve_forever()
    
