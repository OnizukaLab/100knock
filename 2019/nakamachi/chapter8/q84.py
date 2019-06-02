"""
84. 単語文脈行列の作成
83の出力を利用し，単語文脈行列Xを作成せよ．ただし，行列Xの各要素X_{tc}は次のように定義する．

f(t,c)≥10ならば，X_{tc}=PPMI(t,c)=max{logN×f(t,c)f(t,∗)×f(∗,c),0}
f(t,c)<10ならば，X_{tc}=0
ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．
なお，行列Xの行数・列数は数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので注意すること．
幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
"""
from math import log

from scipy import sparse
from datetime import datetime as dt
from q83 import Count
from utils import load_counter, save_matrix, load_matrix


class WordContextMatrixGenerator:
    def __init__(self, counter):
        self.counter = counter
        self.term_list = counter.all_main_word_list()
        self.context_list = counter.all_context_word_list()
        self.matrix = sparse.lil_matrix((len(self.term_list), len(self.context_list)))


    def ppmi(self, f_t_c, f_t, f_c, N):
        if f_t_c < 10:
            return 0
        ppmi = log(N * f_t_c / (f_t * f_c))
        return max(ppmi, 0)

    def generate(self):
        print("term length:", len(self.term_list))
        print("context length:", len(self.context_list))
        N = self.counter.n()
        count = 0
        # TODO: IDEA: f_t_cを2重リストにしてアクセス処理を減らす
        # TODO: IDEA: Orderedにすることで探索時間を減らす
        print(len(self.counter.word_context_counter))
        for t_c, f_t_c in self.counter.word_context_counter.items():
            if count % 3000000 == 0:
                print(count, dt.now())
            count += 1
            if f_t_c >= 10:
                t, c = t_c.split("\t")
                f_t = self.counter.f_t(t)
                f_c = self.counter.f_c(c)
                ppmi = self.ppmi(f_t_c, f_c, f_t, N)
                t_idx = self.term_list.index(t)
                c_idx = self.context_list.index(c)
                self.matrix[t_idx, c_idx] = ppmi


if __name__ == '__main__':
    print("begin main")
    counter = load_counter()
    print("loaded count")
    matrix = WordContextMatrixGenerator(counter)
    print("begin matrix.generation()")
    matrix.generate()
    save_matrix(matrix)
    matrix = load_matrix()

"""
begin main
loaded count
begin matrix.generation()
term length: 276861
context length: 276861
21598257
3000000 2019-05-30 00:11:44.581912
6000000 2019-05-30 00:31:08.442457
9000000 2019-05-30 00:36:53.750519
12000000 2019-05-30 00:38:59.905210
15000000 2019-05-30 00:40:06.249467
18000000 2019-05-30 00:40:54.544913
21000000 2019-05-30 00:41:33.884784
"""