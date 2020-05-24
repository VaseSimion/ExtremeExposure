# Save pictures from src_folder into a folder named Processed at a size of 255x255
import os
import cv2
import ImageManipulation as Imp


src_folder = "C:/Users/sular/Desktop/DatasetMess/Anythingelse"
# loop through the subfolders
for root, folders, filenames in os.walk(src_folder, topdown=False):
    for file in sorted(filenames):
        file_path = os.path.join(root, file)
        print(file_path)
        image = cv2.imread(file_path)
        resized_image = Imp.resize_picture_to_square(picture=image, size=255)
        cv2.imshow("screenshot", resized_image)
        cv2.imwrite(os.path.join(root, "Processed", file), resized_image)
        cv2.waitKey(50)


