while True:
    buf = input()
    if len(buf) >= 1: [print(x) for x in buf.split()]
    else: break