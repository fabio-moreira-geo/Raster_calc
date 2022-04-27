import os
import shutil
import sys
import time
import gdal


src = 'C:\\Users\\Usuario\\Desktop\\Imagens\\B3_B4\\'
# dst3 = r'C:\Users\Usuario\Desktop\Imagens\B3'
# dst4 = r'C:\Users\Usuario\Desktop\Imagens\B4'
listB3 = []
listB4 = []

for img in os.listdir(src):
    if '_B03' in img:
        listB3.append(img)
    if '_B04' in img:
        listB4.append(img)


for uniao in range(len(listB3)):
    dirb3 = src + listB3[uniao]
    dirb4 = src + listB4[uniao]

    band_green = QgsRasterLayer(dirb3)
    band_red = QgsRasterLayer(dirb4)

    saida = src + 'Comp_' + str(listB3[uniao][2:34]+'.tiff')
    entradas = []

    green = QgsRasterCalculatorEntry()
    green.ref = 'green@1'
    green.raster = band_green
    green.bandNumber = 1
    entradas.append(green)

    red = QgsRasterCalculatorEntry()
    red.ref = 'red@1'
    red.raster = band_red
    red.bandNumber = 1
    entradas.append(red)

    calc = QgsRasterCalculator("('green@1')/('red@1')", saida, 'GTiff',
                               band_red.extent(), band_red.width(), band_red.height(), entradas)
