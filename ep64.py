## ฟังก์ชันเช็๋คจำนวนตัวอักษร พิมพ์เล็ก/พิมพ์ใหญ่
 

########################################################################################################################
# ABcDEfg

def checkString(message):
    result = {"UPPER":0,"LOWER":0}
    for c in message:
        if c.isupper():
            result["UPPER"] += 1
        elif c.islower():
            result["LOWER"] += 1
        else:
            pass
        # print(c," = ")
    return result

message = input("input your message : ")

x = checkString(message)
print(x)

########################################################################################################################