for ch in input():
    print(chr(ord(ch) - 32) if 97 <= ord(ch) <= 122 else ch, end="")
print()
