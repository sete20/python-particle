
import os
# print(os.getcwd())
# file = open(os.path.abspath(__file__) +'textt.text')

myFile=open(r"C:\Users\Administrator\Desktop\PythonCourse\textt.text","a")
# myFile.write('\sdfjkahfjkgsdghgafg new line')
myFile.writelines('sdfjkahfjkgsdghgafg new line')
myFile.close()
myFile = open(r"C:\Users\Administrator\Desktop\PythonCourse\textt.text")

print(myFile.read())