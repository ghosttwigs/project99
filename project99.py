# ask the name = anki
# total no of letters = 4

#     0 1 2 3
# 0   a * * *
# 1   * n * *
# 2   * * k *
# 3   * * * i

# a - [0][0]
# n - [1][1]
# k - [2][2]

name = input("Enter your name : ")
times = len(name)

for i in range(0,times):
    for j in range(0,times):
        if i==j :
            print(name[j] , sep = " " , end = " ")
        else :
            print("*" , sep = " " , end = " ")

    print()















