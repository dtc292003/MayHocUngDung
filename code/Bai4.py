import math
vt1 = []
vt2 = []
def khoang_cach_euclide(vt1,vt2):
    khoang_cach = 0.0
    for i in range(len(vt1)):
        khoang_cach += (vt1[i] - vt2[i]) ** 2
    khoang_cach = math.sqrt(khoang_cach)
    return round(khoang_cach,4)

def khoang_cach_cosine(vt1,vt2):
    khoang_cach = 0.0
    tich_vo_huong = 0.0
    do_dai_vt1 = 0.0
    do_dai_vt2 = 0.0
    for i in range(len(vt1)):
        tich_vo_huong += (vt1[i]*vt2[i])
        do_dai_vt1 += vt1[i]**2
        do_dai_vt2 += vt2[i] **2
    do_dai_vt1 = do_dai_vt1**0.5
    do_dai_vt2 = do_dai_vt2 **0.5
    khoang_cach = tich_vo_huong/(do_dai_vt1*do_dai_vt2)
    return round( 1- khoang_cach,4)
print("Khoảng cách euclide: ", khoang_cach_euclide([1,2],[1,3]))
print("Khoảng cách cosine: ", khoang_cach_cosine([1,2],[1,3]))
print("---------------------------------------------------------")
print("Khoảng cách euclide: ", khoang_cach_euclide([1,2,2],[1,3,4]))
print("Khoảng cách cosine: ", khoang_cach_cosine([1,2,2],[1,3,4]))
print("---------------------------------------------------------")
print("Khoảng cách euclide: ", khoang_cach_euclide([1,2,2,1],[1,3,4,2]))
print("Khoảng cách cosine: ", khoang_cach_cosine([1,2,2,1],[1,3,4,2]))
print("---------------------------------------------------------")
print("Khoảng cách euclide: ", khoang_cach_euclide([1,2,2,1,4],[1,3,4,2,6]))
print("Khoảng cách cosine: ", khoang_cach_cosine([1,2,2,1,4],[1,3,4,2,6]))