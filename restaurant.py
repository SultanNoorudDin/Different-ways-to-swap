# a[::-1]       --------------  sort

#   -----------------   Reverse list of calories using 3 different approaches   ------------------------------
user_list = list(map(int, input('give calories: ').split()))
print(user_list[::-1])
l = list(reversed(user_list))
print(l)
# j = len(user_list)
for i in range(len(user_list)//2):
    user_list[i], user_list[len(user_list)-i-1] =user_list[len(user_list)-i-1], user_list[i]

print(user_list)