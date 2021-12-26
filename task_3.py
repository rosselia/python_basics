# 1
import os
import shutil

os.mkdir("değiştirilmiş")

for i in range(2, 310):
    os.rename("C:\\Users\\terzi\Desktop\\Yeni klasör\\multiplex_" + str(i) + ".jpg",
              "C:\\Users\\terzi\Desktop\\Yeni klasör\\" + str(i - 1) + ".jpg")
    shutil.move("C:\\Users\\terzi\Desktop\\Yeni klasör\\" + str(i - 1) + ".jpg",
                "C:\\Users\\terzi\\PycharmProjects\\AAD_Egıtım\\değiştirilmiş\\{0}.jpg".format(str(i - 1)))

for i in range(0, 305):
    os.rename("C:\\Users\\terzi\Desktop\\Yeni klasör\\ranger_" + str(i) + ".jpg",
              "C:\\Users\\terzi\Desktop\\Yeni klasör\\" + str(i - 1) + ".jpg")
    shutil.move("C:\\Users\\terzi\Desktop\\Yeni klasör\\" + str(i - 1) + ".jpg",
                "C:\\Users\\terzi\\PycharmProjects\\AAD_Egıtım\\değiştirilmiş\\{0}.jpg".format(str(i - 1)))

for i in range(0, 304):
    os.rename("C:\\Users\\terzi\Desktop\\Yeni klasör\\talon_" + str(i) + ".jpg",
              "C:\\Users\\terzi\Desktop\\Yeni klasör\\" + str(i - 1) + ".jpg")
    shutil.move("C:\\Users\\terzi\Desktop\\Yeni klasör\\" + str(i - 1) + ".jpg",
                "C:\\Users\\terzi\\PycharmProjects\\AAD_Egıtım\\değiştirilmiş\\{0}.jpg".format(str(i - 1)))

for i in range(0, 328):
    os.rename("C:\\Users\\terzi\Desktop\\Yeni klasör\\unknown_" + str(i) + ".jpg",
              "C:\\Users\\terzi\Desktop\\Yeni klasör\\" + str(i - 1) + ".jpg")
    shutil.move("C:\\Users\\terzi\Desktop\\Yeni klasör\\" + str(i - 1) + ".jpg",
                "C:\\Users\\terzi\\PycharmProjects\\AAD_Egıtım\\değiştirilmiş\\{0}.jpg".format(str(i - 1)))

for i in range(2, 309):
    os.rename("C:\\Users\\terzi\\Desktop\\Yeni klasör\\labels\\multiplex_" + str(i) + ".txt",
              "C:\\Users\\terzi\\Desktop\\Yeni klasör\\labels\\" + str(i - 1) + ".txt")
    shutil.move("C:\\Users\\terzi\Desktop\\Yeni klasör\\labels\\" + str(i - 1) + ".txt",
            "C:\\Users\\terzi\\PycharmProjects\\AAD_Egıtım\\değiştirilmiş\\{0}.txt".format(str(i - 1)))

for i in range(14, 305):
    os.rename("C:\\Users\\terzi\\Desktop\\Yeni klasör\\labels\\ranger_" + str(i) + ".txt",
              "C:\\Users\\terzi\\Desktop\\Yeni klasör\\labels\\" + str(i - 1) + ".txt")
    shutil.move("C:\\Users\\terzi\Desktop\\Yeni klasör\\labels\\" + str(i - 1) + ".txt",
            "C:\\Users\\terzi\\PycharmProjects\\AAD_Egıtım\\değiştirilmiş\\{0}.txt".format(str(i - 1)))

for i in range(1, 304):
    os.rename("C:\\Users\\terzi\\Desktop\\Yeni klasör\\labels\\talon_" + str(i) + ".txt",
              "C:\\Users\\terzi\\Desktop\\Yeni klasör\\labels\\" + str(i - 1) + ".txt")
    shutil.move("C:\\Users\\terzi\Desktop\\Yeni klasör\\labels\\" + str(i - 1) + ".txt",
            "C:\\Users\\terzi\\PycharmProjects\\AAD_Egıtım\\değiştirilmiş\\{0}.txt".format(str(i - 1)))

for i in range(8, 328):
    os.rename("C:\\Users\\terzi\\Desktop\\Yeni klasör\\labels\\unknown_" + str(i) + ".txt",
              "C:\\Users\\terzi\\Desktop\\Yeni klasör\\labels\\" + str(i - 1) + ".txt")
    shutil.move("C:\\Users\\terzi\Desktop\\Yeni klasör\\labels\\" + str(i - 1) + ".txt",
            "C:\\Users\\terzi\\PycharmProjects\\AAD_Egıtım\\değiştirilmiş\\{0}.txt".format(str(i - 1)))