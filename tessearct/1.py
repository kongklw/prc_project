import pytesseract, os
from PIL import Image

path = os.path.abspath(os.path.dirname(__name__))
aim = str(path) + "/5.png"
print(aim)
# image = Image.open(aim)
# text = pytesseract.image_to_string(image,lang='chi_sim')
# print(text)

#
from PIL import Image
import subprocess

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    # 对图片进行阈值过滤（低于143的置为黑色，否则为白色）
    image = image.point(lambda x: 0 if x < 143 else 255)
    # 重新保存图片
    image.save(newFilePath)

    # 调用系统的tesseract命令对图片进行OCR识别
    subprocess.call(["tesseract", newFilePath, "output"])

    # 打开文件读取结果
    with open("output.txt", 'r') as f:
        print(f.read())

if __name__ == "__main__":
    cleanFile(aim, "text2clean.png")