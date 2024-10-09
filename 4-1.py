#02-毛子煜-p04-1
l1=list(range(0,10))
l2=['a','b','c','d','e','f','g','h','i','j']
a,b=map(int,input().split())
l1[a%10],l2[b%10]=l2[b%10],l1[a%10]
print(l1)
print(l2)
