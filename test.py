n = int(input())
result = 0
if n >= 50000 :
    tmp = n // 50000
    n = n % 50000
    result += tmp

if n >= 10000 :
    tmp = n // 10000
    n = n % 10000
    result += tmp
    
if n >= 5000 :
    tmp = n // 5000
    n = n % 5000
    result += tmp
    
if n >= 1000 :
    tmp = n // 1000
    n = n % 1000
    result += tmp

if n >= 500 :
    tmp = n // 500
    n = n % 500
    result += tmp
    
if n >= 100 :
    tmp = n // 100
    n = n % 100
    result += tmp
    
if n >= 50 :
    tmp = n // 50
    n = n % 50
    result += tmp
    
if n >= 10 :
    tmp = n // 10
    n = n % 10
    result += tmp
    
print(result)