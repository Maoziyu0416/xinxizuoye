#52-祖嘉怡-P02-5
age=int(input("年龄："))
s=int(input("安静心率："))
mx=220-age
print("范围：",int((mx-s)*0.6+s),int((mx-s)*0.8+s))