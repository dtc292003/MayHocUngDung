#Bài 3.1
import math
a = [1, 2]
b = [1, 3]
tong_hieu_2_bp = 0
print(len(a))
for i in range(len(a)):
    tong_hieu_2_bp += (a[i] - b[i]) ** 2
eucilde = tong_hieu_2_bp ** 0.5
print(eucilde)
cosine = (1 * 1 + 2 * 3) / (math.sqrt(1 ** 2 + 2 ** 2) * math.sqrt(1 ** 2 + 3 ** 2))
print(cosine)
d_cosine = 1 - cosine
print(d_cosine)
#Bài 3.2
a = [1,2,2]
b = [1,3,4]
tong_hieu_2_bp = 0
print(len(a))
for i in range(len(a)):
    tong_hieu_2_bp += (a[i] - b[i]) ** 2
eucilde = tong_hieu_2_bp ** 0.5
print(eucilde)
cosine = (1 * 1 + 2 * 3 + 2 * 4) / (math.sqrt(1 ** 2 + 2 ** 2 + 2 ** 2) * math.sqrt(1 ** 2 + 3 ** 2 + 4 ** 2))
print(cosine)
d_cosine = 1 - cosine
print(d_cosine)