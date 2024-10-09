#02-毛子煜-p04-2
l=[]
def out():
    print(l,len(l))
def ipt():
    return input().split()
l=ipt()
out()
l.append(ipt())
out()
l.extend(ipt())
out()
