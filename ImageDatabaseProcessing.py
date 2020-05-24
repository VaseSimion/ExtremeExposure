# Save pictures from src_folder into a folder named Processed at a size of 255x255
import os
import cv2
import ImageManipulation as Imp


src_folder = "C:/Users/sular/Desktop/DatasetMess/Portrait"
# loop through the subfolders
for root, folders, filenames in os.walk(src_folder, topdown=False):
    for file in sorted(filenames):
        file_path = os.path.join(root, file)
        print(file_path)
        image = cv2.imread(file_path)
        resized_image = Imp.resize_picture_to_square(picture=image, size=128)
        gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("screenshot", gray_image)
        cv2.imwrite(os.path.join(root, "Processed", file), gray_image)
        cv2.waitKey(10)


