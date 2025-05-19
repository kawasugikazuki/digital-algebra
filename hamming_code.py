import numpy as np

# 行列なしに計算する方法
A = np.array([1, 0, 1, 0])

c1 = (A[0] + A[1] + A[2])%2
c2 = (A[0] + A[1]       + A[3])%2
c3 = (       A[1] + A[2]+ A[3])%2
# print(c1,c2,c3)
C = np.array([c1, c2, c3], dtype='int8')
W = np.concatenate([A, C])
print(W)

# 1bitのエラーを加える
E = np.array([0, 0, 1, 0, 0, 0, 0])
N = np.fmod(W + E, 2)
# print(N)

s1 = (N[0] + N[1] + N[2])%2
s2 = (N[0] + N[1]       + N[3])%2
s3 = (       N[1] + N[2]+ N[3])%2
print([s1, s2, s3])

# 生成行列
G = np.array([
  [1,0,0,0,1,1,0],
  [0,1,0,0,1,1,1],
  [0,0,1,0,1,0,1],
  [0,0,0,1,0,1,1],
],
dtype='int8')
# 行列計算でのw
w2 = np.fmod(A@G, 2)
print(w2)

# 検査行列
H = np.array([
  [1,1,1,0,1,0,0],
  [0,1,1,1,0,1,0],
  [1,1,0,1,0,0,1],
],
dtype='int8')
print(np.fmod(w2 @ H.T, 2))
print(np.fmod(N@H.T, 2))