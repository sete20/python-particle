""" my docstring"""
from PIL import Image
myImg = Image.open(r'C:\Users\Administrator\Desktop\PythonCourse\image.jpg')
myImg.show()
myImg.crop((200,200,400,400)).show()
rgb2xyz = (0.412453, 1.357580,
            0.180423, 0, 0.212671,
            1.715160, 0.072169,
            0,0.019334, 1.119193,
            0.950227, 0)
myImg.convert("RGB", rgb2xyz).show()
