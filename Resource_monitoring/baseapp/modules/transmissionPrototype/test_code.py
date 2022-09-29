def readData(test):
    return "4f4b3"

serialData = "123456"
NEW_DATA = readData(serialData)

[ print(readData("asas"))  for _ in range(2)  ] 

# loop = 5
# while loop>=0:
#     print("Try ", loop)
#     if NEW_DATA != "4f4b03":
#         NEW_DATA = readData(serialData)
#     else:
#         print("got it")
#     loop = loop - 1
#     if loop == 0:
#         repeat = input("Transmit device ID failed, do you want to try again ?(y/n)")
#         if repeat == "n":
#             break
#         else:
#             loop = 5


def func1(stop):
    x = 0
    while True:
        x+=x
        print(x)

func1(False)