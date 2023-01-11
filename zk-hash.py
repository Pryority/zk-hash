import hashlib

def hashy():
    default_sha256 = '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 61'
    print('\n DEFAULT SHA-256 BYTES - copy & paste below\n',default_sha256)
    print('_____________________________________________________________________________¬|')
    x = str(input('\nEnter your bytes:\n') or default_sha256)  
    hash = bytearray(hashlib.sha256(bytes.fromhex(x)).digest())
    # print(int.from_bytes(bytes(hash), 'big'))
    i1 = hash[:16]
    # print(i1)
    i2 = hash[16:]
    # print(i2)
    print('1st HALF HASH {}'.format((int.from_bytes(i1, 'big'))))
    print('HEXIDECIMAL SHARD #1 {}'.format(hex(int.from_bytes(i1, 'big'))),'\n')
    print('2nd HALF HASH {}'.format((int.from_bytes(i2, 'big'))))
    print('HEXIDECIMAL SHARD #2',hex(int.from_bytes(i2, 'big')))
hashy()
