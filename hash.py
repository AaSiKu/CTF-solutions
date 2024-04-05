def hash(long_value):
    value = long_value & 0xFFFFFFFFFFFFFFFF
    # value = long_value
    value = ((value & 0xaaaaaaaaaaaaaaaa) >> 1) | ((value & 0x5555555555555555) << 1)
    value = ((value & 0xcccccccccccccccc) >> 2) | ((value & 0x3333333333333333) << 2)
    value = ((value & 0xf0f0f0f0f0f0f0f0) >> 4) | ((value & 0x0f0f0f0f0f0f0f0f) << 4)
    value = ((value & 0xff00ff00ff00ff00) >> 8) | ((value & 0x00ff00ff00ff00ff) << 8)
    value = ((value >> 16) | (value << 16)) & 0xFFFFFFFFFFFFFFFF
    # print(value)
    return value
def reverseHash(long_value):
    value = long_value
    value = value//2**16
    value = ((value & 0xff00ff00ff00ff00) >> 8) | ((value & 0x00ff00ff00ff00ff) << 8)
    value = ((value & 0xf0f0f0f0f0f0f0f0) >> 4) | ((value & 0x0f0f0f0f0f0f0f0f) << 4)
    value = ((value & 0xcccccccccccccccc) >> 2) | ((value & 0x3333333333333333) << 2)
    value = ((value & 0xaaaaaaaaaaaaaaaa) >> 1) | ((value & 0x5555555555555555) << 1)
    value = value & 0xFFFFFFFFFFFFFFFF
    
    return value
value = 10

value = reverseHash(240658437888736)
print(value)
print(hash(value))
# print(hash(100085988678407))
# print(hash(100085988678407))
# 240658437888736
# 100085988678407