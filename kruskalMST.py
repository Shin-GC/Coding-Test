weights = [(0, 1, 9), (0, 2, 10), (1, 3, 10), (1, 4, 5),
           (1, 6, 3), (2, 3, 9), (2, 4, 7), (2, 5, 2),
           (3, 5, 4), (3, 6, 8), (4, 6, 1), (5, 6, 6)]

# 1. 가중치의 오름차순으로 간선들을 정렬 : L = 정렬된 간선 리스트
weights.sort(key=lambda w: w[2])  # lambda 를 이용하여 가중치인 [2]을 기준으로 정렬
mst = []  # 2. 트리 초기화
N = 7  # 그래프의 정점 수
p = [x for x in range(N+1)]  # 3. 그래프의 모든 정점을 집합으로 만든다. [ 루트 ]


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1


tree_edges = 0
mst_cost = 0
while True:
    if tree_edges == N-1:
        break
    u, v, wt = weights.pop(0)  # 다음 최소 가중치 간선 가져오기
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v))  # 트리에 (u, v) 추가
        mst_cost += wt
        tree_edges += 1

print('최소신장트리: ', end='')
print(mst)
print('최소신장트리 가중치:', mst_cost)
