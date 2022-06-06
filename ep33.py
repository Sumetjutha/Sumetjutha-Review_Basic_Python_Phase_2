### SET

##############################################################################
## Subset
fish = {"ปลาดุก","ปลาหมอ","ปลาวาฬ","ปลาโลมา","ปลาฉลาม","ปลาตะเพียน"}
print("fish => ",fish)
x = {"ปลาหมอ","ปลาซิว"}

# อยากรู้ว่า x เป็น subset ของ fish หรือเปล่า
x.issubset(fish)
print(x.issubset(fish))

y = {"ปลาดุก","ปลาฉลาม"}
y.issubset(fish)
print(y.issubset(fish))

z = {"ปลาโลมา","ปลาตะเพียน","ปลาวาฬ"}
z.issubset(fish)
print(z.issubset(fish))
##############################################################################