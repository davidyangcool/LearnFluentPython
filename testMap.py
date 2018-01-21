from functions import factorial,fact

# print(factorial(5))
# print(list(map(factorial,range(6))))#map 高阶函数
# print([fact(n) for n in range(6)]) # 列表推导式

filter_list=filter(lambda x:x%2,list(range(6)))
# print(list(filter_list))

# print(list(map(factorial,filter(lambda n:n%2,list(range(6))))))
print([factorial(n) for n in range(6) if n%2]) # 列表推导式
