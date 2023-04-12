import base64
file_base64 = "SzNwd3FCcmVYZVViVDI2"
base64_bytes = file_base64.encode('ascii')
file_bytes = base64.b64decode(base64_bytes)
newFileByteArray = bytearray(file_bytes)
open("pakan.txt","wb").write(newFileByteArray)