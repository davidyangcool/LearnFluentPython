fruits = ['strawberry','fig', 'apple','cherry','raspberry','banana']
sorted_fruits = sorted(fruits,key=len)
print(sorted_fruits)
def reverse(word):
    return word[::-1]
# print(reverse('testing'))
rever_sort=sorted(fruits,key=reverse)
print(rever_sort)