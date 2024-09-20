import json
import itertools
from sklearn.metrics import accuracy_score, normalized_mutual_info_score
from scipy.optimize import linear_sum_assignment
import numpy as np


# Hungarian algorithm을 이용해 클러스터링 라벨과 실제 라벨을 정렬하는 함수
def calculate_acc(y_true, y_pred):
    nums = [0, 1, 2, 3, 4, 5]
    perms = itertools.permutations(nums)

    accs = []
    for perm in perms:
        truth = [perm[nums.index(x)] for x in y_true]
        accs.append(sum(1 for a, b in zip(truth, y_pred) if a == b))

    return max(accs) / len(y_pred)
    
    # y_true와 y_pred의 유일한 값들로 행렬을 만들어 Hungarian Algorithm을 적용
    # D = max(y_pred.max(), y_true.max()) + 1
    # cost_matrix = np.zeros((D, D), dtype=np.int64)

    # for i in range(len(y_true)):
    #     cost_matrix[y_pred[i], y_true[i]] += 1
    
    # # Linear assignment 문제를 풀어서 최대 일치를 찾음
    # row_ind, col_ind = linear_sum_assignment(cost_matrix.max() - cost_matrix)
    
    # return cost_matrix[row_ind, col_ind].sum() / len(y_true)


input_txt = '/home/hbp5148/Desktop/orchid/nc/citeseer.json'
ground_truth = '/home/hbp5148/Desktop/orchid/data/citeseer_group.txt'

with open(input_txt, 'r', encoding='utf-8') as file:
    data = json.load(file)
    
truth = []

with open(ground_truth, 'r', encoding='utf-8') as file:
    for line in file:
        _, value = line.split()
        truth.append(int(value))

accs = []
nmis = []
        
for clustering in data:
    labels = clustering['labels']
    # Accuracy (ACC)
    acc = calculate_acc(np.array(truth), np.array(labels))
    print(f'ACC (Accuracy): {acc:.4f}')
    accs.append(acc)

    # NMI (Normalized Mutual Information)
    nmi = normalized_mutual_info_score(truth, labels)
    print(f'NMI (Normalized Mutual Information): {nmi:.4f}')
    nmis.append(nmi)
    
print(max(accs), max(nmis))