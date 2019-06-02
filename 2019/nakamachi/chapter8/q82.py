"""
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語c
のペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．

- ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
- 単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める
"""
from utils import load_data, save_word_context_tab
from random import randint
from q81 import main as q81main

def generate_context_word_pair(word_list, word_idx, d):
    word = word_list[word_idx]
    context = word_list[word_idx - d: word_idx + d + 1]
    context.pop(d)
    return word, context


def generate_context_word_pair_from_data():
    data = q81main()
    result = []
    for idx in range(len(data)):
        try:
            key, context = generate_context_word_pair(data, idx, randint(1, 5))
            result.append((key, context))
        except:
            pass
    return result

def main():
    data = generate_context_word_pair_from_data()
    text = ""
    for item in data:
        for c in item[1]:
            text += item[0] + "\t" + c + "\n"
    save_word_context_tab(text)


if __name__ == '__main__':
    word_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(generate_context_word_pair(word_list, 5, 2))
    main()


