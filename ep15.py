### Assignment 6 กลุ่มสมาชิกเลขยกกำลัง

##############################################################################
number_1 = [1,2,3,4,5,6,7]
print("list of number_1 ก่อนที่จะทำการยกกำลังสอง => ",number_1)
## แปลงให้เป็นค่ายกกำลัง

## เขียนแบบปกติ
for i in range(len(number_1)):
    number_1[i] = number_1[i]*number_1[i]
    
print("ผลลัพธ์ที่เกิดขึ้น => ",number_1)
print("End")

## เขียนแบบลดรูป เอาไปประยุกต์ใช้ได้  แต่มันเขียนลดรูปแบบนี้ได้
number_2 = [1,2,3,4,5,6,7]
print("list of number_2 ก่อนที่จะทำการยกกำลังสอง => ",number_2)

number_2 = [x*x for x in number_2]
print("ผลลัพธ์ที่เกิดขึ้นจากการเขียนแบบลดรูป => ",number_2)
##############################################################################