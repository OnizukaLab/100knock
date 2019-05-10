
if __name__ == '__main__':
    count = [0, 0, 0, 0]  # TN, FP, FN, TP
    with open('q_76.out') as f:
        for line in f:
            col = line.strip().split('\t')
            count[int(col[0]+col[1] ,2)] += 1
    print('accuracy : {}'.format((count[0]+count[3])/sum(count)))
    precision = count[3]/(count[1]+count[3])
    print('precision : {}'.format(precision))
    recall = count[3]/(count[2]+count[3])
    print('recall : {}'.format(recall))
    print('f1-score : {}'.format(2*recall*precision/(recall+precision)))
