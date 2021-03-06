# import SimpleXMLRPCServer bagian server
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# buat fungsi bernama file_upload()
def file_upload(filedata):
    
    # buka file 
    with open("hasil_upload.txt",'wb') as handle:
        #convert from byte to binary IMPORTANT!
        data1=filedata.data
        
        # tulis file tersebut
        handle.write(data1)
        return True  #IMPORTANT
        
# must have return value
# else error messsage: "cannot marshal None unless allow_none is enabled"

# buat server
server = SimpleXMLRPCServer(("172.20.10.4", 8001))

# tulis pesan server telah berjalan
print ("Listening on port 8001")

# register fungsi 
server.register_function(file_upload, "upload")

# jalankan server
server.serve_forever()