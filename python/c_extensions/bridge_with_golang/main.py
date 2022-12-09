#!/usr/bin/env python 
import ctypes
import json
library = ctypes.cdll.LoadLibrary('./library.so')

if __name__=="__main__":
    library.helloWorld()


    library.hello.argtypes = [ctypes.c_char_p]
    library.hello("everyone".encode('utf-8'))


    library.farewell.restype = ctypes.c_void_p

    # this is a pointer to our string
    farewell_output = library.farewell()

    # we dereference the pointer to a byte array
    farewell_bytes = ctypes.string_at(farewell_output)

    # convert our byte array to a string
    farewell_string = farewell_bytes.decode('utf-8')  

    print(farewell_output, farewell_bytes, farewell_string)

    library.fromJSON.argtypes = [ctypes.c_char_p]
    document = {
        "name": "john",
        "last_name": "smith"
    }
    library.fromJSON(json.dumps(document).encode('utf-8'))