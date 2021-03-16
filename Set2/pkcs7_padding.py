inp = b'YELLOW SUBMARINE'
expect = b"YELLOW SUBMARINE\x04\x04\x04\x04"
lenpad = 20
out = inp + bytes([lenpad %len(inp)])*(lenpad %len(inp))
# print(out)
assert expect ==out,'failed'