import tensorflow as tf
import cv2
import ImageManipulation as Imp
import numpy as np
import os

model = tf.keras.models.load_model("ModelLocal.h5")
file_path = "C:/Users/sular/PycharmProjects/ExtremeExposure/Dataset/Uncategorised"


for root, folders, filenames in os.walk(file_path, topdown=False):
    for file in sorted(filenames):
        file_path2 = os.path.join(root, file)
        image = cv2.imread(file_path2)
        prepared_image = Imp.resize_picture_to_square(image, 224)
        prepared_image = prepared_image[np.newaxis, ...]
        predictionlist = model.predict([prepared_image])[0]
        print(file_path2 + " " + str([round(x, 2) for x in predictionlist]))
        if Imp.decode(predictionlist) == "Animal":   # first folder
            cv2.imwrite(os.path.join(root, "Animal", file), image)
        elif Imp.decode(predictionlist) == "Flower":  # second folder
            cv2.imwrite(os.path.join(root, "Flower", file), image)
        else:
            cv2.imwrite(os.path.join(root, "Unknown", file), image)
