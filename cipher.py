message = input('Enter your message: ')
while True:
    shift = input('Enter a shift value between 1 and 25: ')
    try:
        shift = int(shift)
        if shift > 0 and shift <= 25:
            break
    except ValueError:
        continue

encrypted = ''
for ch in message:
    tmp = ord(ch)
    if tmp >= 65 and tmp <= 90:
        tmp += shift
        if tmp > 90:
            tmp -= 26
        encrypted += chr(tmp)
    elif tmp >= 97 and tmp <= 122:
        tmp += shift
        if tmp > 122:
            tmp -= 26
        encrypted += chr(tmp)
    else:
        encrypted += ch

print(encrypted)
