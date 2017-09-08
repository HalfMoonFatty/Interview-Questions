def convertByte(byte):
    unit = ['B','KB','MB','GB','TB']
    i = 0
    while byte > 1000:
        byte = float(byte)/1000
        i += 1
    return str(byte) + unit[i]

s = 1100
s = 11100
s = 12345678

print convertByte(s)




def convertByte2(byte):
    unit = ['B','KB','MB','GB','TB']
    i = 0
    res = ''
    while byte > 0:
        res = str(byte%1000) + unit[i] + res 
        byte = byte/1000
        i += 1
    return res


s = 1100
s = 11100
s = 12345678
#s = 1
print convertByte2(s)
