# 問題50からパイプなどで入力してくる
# python3 q50.py | python3 q51.py

import sys

if __name__ == '__main__':
    for line in sys.stdin:
        print("\n".join(line.strip().split(" ")) + "\n")
