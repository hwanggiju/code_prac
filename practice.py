year = int(input()) # 년도 입력

year_re = ((year % 4 == 0) & (year % 100 != 0 )) |  (year % 400 == 0)

if year_re == 1 :
    print(1)

else :
    print(0)