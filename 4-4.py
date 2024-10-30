#52-祖嘉怡-P04-4
lis=list(map(float,input().split()))
print('{:.2f}'.format((sum(lis)-max(lis)-min(lis))/(len(lis)-2)))