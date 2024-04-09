import cv2, os
import numpy as np
from PIL import Image
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def createRecolor(original_tilesheet_name, maped_tilesheet_name, changed_tilesheet_name, result_tilesheet_name):

    img1_path = os.path.join(__location__, original_tilesheet_name)
    img2_path = os.path.join(__location__, maped_tilesheet_name)
    img3_path = os.path.join(__location__, changed_tilesheet_name)

    img1 = Image.open(img1_path)
    width, height = img1.size
    pixel_values_1 = list(img1.getdata())

    img2 = Image.open(img2_path)
    pixel_values_2 = list(img2.getdata())

    img3 = Image.open(img3_path)

    match_pixel = {}

    for i in range(len(pixel_values_1)):
        try:
            if pixel_values_1[i] == (0, 0, 0, 0) or pixel_values_2[i] == (0, 0, 0, 0):
                continue
            if pixel_values_1[i] == (255, 255, 255, 0) or pixel_values_2[i] == (255, 255, 255, 0):
                continue
            if pixel_values_1[i] not in match_pixel:
                match_pixel[pixel_values_1[i]] = pixel_values_2[i]
        except:
            break
        # if pixel_values_1[i] not in match_pixel:
        #     match_pixel[pixel_values_1[i]] = pixel_values_2[i]
    #print(match_pixel)
    pixelMap = img3.load()
    img = Image.new(img3.mode, img3.size)
    pixelsNew = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            try:
                if pixelMap[i,j] in match_pixel:
                    #print(pixelMap[i,j], ' co mat')
                    pixelsNew[i,j] = match_pixel[pixelMap[i,j]]
                else:
                    pixelsNew[i,j] = pixelMap[i,j]
            except:
                break
    testname = 'test' + result_tilesheet_name
    #img3.save(os.path.join(__location__, testname))

    img.save(os.path.join(__location__, result_tilesheet_name))
# myInputList = ['farmhouse_tiles.png']
# myOGList = ['farmhouse_tiles.png']
# myInputList = ['map_spring.png', 'map_summer.png', 'map_fall.png', 'map_winter.png']
# myOGList = ['map_spring.png', 'map_summer.png', 'map_fall.png', 'map_winter.png']
# myInputList = ['tree1_greenRain.png', 'tree1_greenRain_fall.png', 'tree1_greenRain_winter.png']
# myOGList = ['spring_island_tilesheet_1.png', 'fall_island_tilesheet_1.png', 'winter_island_tilesheet_1.png']
# myInputList = ['island_tilesheet_1.png']
myInputList = ['spring_mod_lumisteria_tilesheetsoutdoor_decorations.png', 'summer_mod_lumisteria_tilesheetsoutdoor_decorations.png', 'fall_mod_lumisteria_tilesheetsoutdoor_decorations.png', 'winter_mod_lumisteria_tilesheetsoutdoor_decorations.png']
myOGList = ['spring_outdoorsTileSheet2.png', 'summer_outdoorsTileSheet2.png', 'fall_outdoorsTileSheet2.png', 'winter_outdoorsTileSheet2.png']
myVPRList = ['spring_outdoorsTileSheet2.png', 'summer_outdoorsTileSheet2.png', 'fall_outdoorsTileSheet2.png', 'winter_outdoorsTileSheet2.png']

# myOGList = ['spring_island_tilesheet_1.png', 'summer_island_tilesheet_1.png', 'fall_island_tilesheet_1.png', 'winter_island_tilesheet_1.png']
# myInputList = ['spring_outdoorsTileSheet2.png', 'summer_outdoorsTileSheet2.png', 'fall_outdoorsTileSheet2.png', 'winter_outdoorsTileSheet2.png']
# myOGList = ['spring_island_tilesheet_1.png', 'summer_island_tilesheet_1.png', 'fall_island_tilesheet_1.png', 'winter_island_tilesheet_1.png']

# myOGList = ['spring_outdoorsTileSheet.png', 'summer_outdoorsTileSheet.png', 'fall_outdoorsTileSheet.png', 'winter_outdoorsTileSheet.png']
for i in range(len(myInputList)):
    createRecolor(os.path.join('OG', myOGList[i]), os.path.join('VPR', myVPRList[i]), os.path.join('Input', myInputList[i]), myInputList[i])

# for i in range(len(myInputList)):
#     createRecolor(os.path.join('OG', myOGList[i]), os.path.join('VPR', myOGList[i]), os.path.join('Input', myInputList[i]), myInputList[i])
# createRecolor(os.path.join('OG', 'tree1_greenRain_spring.png'), os.path.join('VPR', 'tree1_greenRain_summer.png'), os.path.join('Input', 'tree1_greenRain_spring.png'), 'tree1_greenRain_spring.png')
#myInputList = ['spring_outdoorTileSheet_extra.png', 'summer_outdoorTileSheet_extra.png', 'fall_outdoorTileSheet_extra.png', 'winter_outdoorTileSheet_extra.png']

# myInputList = ['spring_island_tilesheet_1.png', 'summer_island_tilesheet_1.png', 'fall_island_tilesheet_1.png', 'winter_island_tilesheet_1.png']
# myOGList = ['spring_island_tilesheet_1.png', 'summer_island_tilesheet_1.png', 'fall_island_tilesheet_1.png', 'winter_island_tilesheet_1.png']




# myInputList = ['spring_island_tilesheet_1.png', 'summer_island_tilesheet_1.png', 'fall_island_tilesheet_1.png', 'winter_island_tilesheet_1.png']
# myOGList = ['spring_town.png', 'summer_town.png', 'fall_town.png', 'winter_town.png']
# for i in range(len(myInputList)):
#     createRecolor(os.path.join('OG', myOGList[i]), os.path.join('VPR', myOGList[i]), os.path.join(__location__, myInputList[i]), os.path.join('Result', myInputList[i]))

# def fix(original_tilesheet_name, maped_tilesheet_name, changed_tilesheet_name, result_tilesheet_name):
#     img1_path = os.path.join(__location__, original_tilesheet_name)
#     img2_path = os.path.join(__location__, maped_tilesheet_name)
#     img3_path = os.path.join(__location__, changed_tilesheet_name)

#     img1 = Image.open(img1_path)
#     width, height = img1.size
#     pixel_values_1 = list(img1.getdata())

#     img2 = Image.open(img2_path)
#     pixel_values_2 = list(img2.getdata())
#     img3_path = os.path.join(__location__, changed_tilesheet_name)
#     img3 = Image.open(img3_path)

#     match_pixel = {}
#     # match_pixel[(255, 186, 44, 255)] = (197, 160, 98, 255)
#     # match_pixel[(255, 198, 43, 255)] = (197, 160, 98, 255)
#     for i in range(len(pixel_values_1)):
#         if pixel_values_1[i] == (0, 0, 0, 0) or pixel_values_2[i] == (0, 0, 0, 0):
#             continue
#         if pixel_values_1[i] == (255, 255, 255, 0) or pixel_values_2[i] == (255, 255, 255, 0):
#             continue
#         match_pixel[pixel_values_1[i]] = pixel_values_2[i]
#     # print(match_pixel)
#     pixelMap = img3.load()
#     img = Image.new(img3.mode, img3.size)
#     pixelsNew = img.load()
#     for i in range(img.size[0]):
#         for j in range(img.size[1]):
#             if pixelMap[i,j] in match_pixel:
#                 print(pixelMap[i,j], ' co mat')
#                 pixelsNew[i,j] = match_pixel[pixelMap[i,j]]
#             else:
#                 pixelsNew[i,j] = pixelMap[i,j]
#     img.save(os.path.join(__location__, result_tilesheet_name))

# for i in range(len(myInputList)):
#     fix(os.path.join(__location__, 'colormapOG.png'), os.path.join(__location__, 'colormapVPR.png'), os.path.join('Result', myInputList[i]), os.path.join('Result', myInputList[i]))