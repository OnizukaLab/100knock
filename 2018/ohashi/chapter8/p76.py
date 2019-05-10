import pickle
from p74 import Predictor

def read_data(file_name):
    with open(file_name) as f:
        data = [line.replace('\n', '').split(' ', 1) for line in f]

    return [d[1] for d in data], [d[0] for d in data]

def main():
    text, label = read_data('sentiment.txt')
    model = Predictor(model_file='lr.model', bow_file='bow.model')
    preds = [model.predict(t) for t in text]

    with open('preds_76.txt', 'w') as f:
        [f.write('{}\t{}\t{}\n'.format(l, '+1' if p >= 0.5 else '-1', str(p))) for l, p in zip(label, preds)]

if __name__ == '__main__':
    main()