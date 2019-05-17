"""
課題 52. ステミング

51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ．
Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．

しかし,stemmingライブラリについての簡単な検証の結果,porter.pyがpython2形式なので動きません。
from stemming import porter
print(help(porter)) # これでエラーがでる

```error
Traceback (most recent call last):
  File "/Users/reiven/Documents/Python/100knock/2019/nakamachi/chapter6/q52.py", line 4, in <module>
    from stemming import porter
  File "/usr/local/lib/python3.7/site-packages/stemming/porter.py", line 176
    print stem("fundamentally")
             ^
SyntaxError: invalid syntax
```

なので別案としてsnowballstemmerを使う
"""
import sys
from os import path
import snowballstemmer

sys.path.append(path.abspath(path.curdir))
from q51 import main as solution


def steming_ops(word_list):
    stemmer = snowballstemmer.stemmer("english")
    return [stemmer.stemWord(word) for word in word_list]


def main():
    solution_51 = solution()
    return steming_ops(solution_51)


if __name__ == '__main__':
    print(main())
