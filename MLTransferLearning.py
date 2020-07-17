import os
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from keras import applications
from keras import Model
from keras.layers import Flatten, Dense
from keras import optimizers
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

# The images are in a folder named 'shapes/training'
training_folder_name = "C:/Users/sular/PycharmProjects/ExtremeExposure/Dataset"

# The folder contains a subfolder for each class of shape
classes = sorted(os.listdir(training_folder_name))
print(classes)

pretrained_size = (224, 224)
batch_size = 10

print("Getting Data...")
datagen = ImageDataGenerator(rescale=1./255, # normalize pixel values
                             validation_split=0.3,
                             horizontal_flip=True,
                             fill_mode='nearest') # hold back 30% of the images for validation

print("Preparing training dataset...")
train_generator = datagen.flow_from_directory(
    training_folder_name,
    target_size=pretrained_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='training') # set as training data

print("Preparing validation dataset...")
validation_generator = datagen.flow_from_directory(
    training_folder_name,
    target_size=pretrained_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation') # set as validation data


start_from_Imnet = False  # This will change between locally trained model or start with the one from Imnet Database
if start_from_Imnet:
    #Load the base model, not including its final connected layer, and set the input shape to match our images
    base_model = applications.vgg16.VGG16(weights='imagenet', include_top=False, input_shape=train_generator.image_shape)

    # Freeze the already-trained layers in the base model
    for layer in base_model.layers:
        layer.trainable = False

    # Create layers for classification of our images
    x = base_model.output
    x = Flatten()(x)
    prediction_layer = Dense(len(classes), activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=prediction_layer)
else:
    # load model saved locally in previous run
    model = tf.keras.models.load_model("ModelLocal.h5")
    for layer in model.layers[:-2]:
        layer.trainable = False

# Compile the model
opt = tf.keras.optimizers.Adam(lr=0.001)
model.compile(loss='categorical_crossentropy',
              optimizer="adam",
              metrics=['accuracy'])

print(model.summary())

num_epochs = 2
history = model.fit_generator(
    train_generator,
    steps_per_epoch = train_generator.samples // batch_size,
    validation_data = validation_generator,
    validation_steps = validation_generator.samples // batch_size,
    epochs = num_epochs)

model.save("ModelLocal.h5")

epoch_nums = range(1,num_epochs+1)
training_loss = history.history["loss"]
validation_loss = history.history["val_loss"]
plt.plot(epoch_nums, training_loss)
plt.plot(epoch_nums, validation_loss)
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['training', 'validation'], loc='upper right')
plt.show()

print("Generating predictions from validation data...")
x_test = validation_generator[0][0]
y_test = validation_generator[0][1]

print(len(validation_generator))
class_probabilities = model.predict(x_test)
predictions = np.argmax(class_probabilities, axis=1)
true_labels = np.argmax(y_test, axis=1)
cm = confusion_matrix(true_labels, predictions)

plt.imshow(cm, interpolation="nearest", cmap='gray')
plt.colorbar()
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes, rotation=85)
plt.yticks(tick_marks, classes)
plt.xlabel("Predicted Class")
plt.ylabel("True Class")
plt.show()

try:
    for i in range(5):
        x_test = validation_generator[i][0]
        y_test = validation_generator[i][1]
        print(len(validation_generator))
        class_probabilities = model.predict(x_test)
        predictions = np.argmax(class_probabilities, axis=1)
        true_labels = np.argmax(y_test, axis=1)
        cm = confusion_matrix(true_labels, predictions)

        plt.imshow(cm, interpolation="nearest", cmap='gray')
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=85)
        plt.yticks(tick_marks, classes)
        plt.xlabel("Predicted Class")
        plt.ylabel("True Class")
        plt.show()
except:
    pass
