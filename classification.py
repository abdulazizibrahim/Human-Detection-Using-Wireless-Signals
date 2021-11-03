import cv2
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.models import load_model


class classification:

    def train(self):
        '''
        This fucntion trains the CNN model on the provided dataset and then saves it.
        '''
        train = ImageDataGenerator()
        validation = ImageDataGenerator()

        train_dataset = train.flow_from_directory('C:/Users/abdul/OneDrive/Desktop/New folder/FYP/final/data/backup/train',color_mode='grayscale')
        validate_dataset = validation.flow_from_directory('C:/Users/abdul/OneDrive/Desktop/New folder/FYP/final/data/backup/validate',color_mode='grayscale')

        model = tf.keras.models.Sequential([
        #convolutional layer
        tf.keras.layers.Conv2D(64,(3,3), activation ="relu"),
        #pooling layer
        tf.keras.layers.MaxPool2D(pool_size=(2,2)),
    
        tf.keras.layers.Conv2D(32,(3,3), activation ="relu"),
        tf.keras.layers.MaxPool2D(pool_size=(2,2)),    
    
        # Flatten units
        tf.keras.layers.Flatten(),

        # Add a hidden layer with dropout
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.5),

        # Add an output layer with output units for all 10 digits
        tf.keras.layers.Dense(2, activation="softmax")
        ])

        # Train neural network
        model.compile(
            optimizer="adam",
            loss="categorical_crossentropy",
            metrics=["accuracy"]
        )

        model.fit(train_dataset, epochs=10,validation_data = validate_dataset)

        model.save('model.h5')

    def predict(self,path):
        '''
        This function takes path of images as input, predicts the 
        labels of the images using the pre-trained model.
        '''
        #loading trained model
        model = load_model('model.h5')
        count = 0
        for i in os.listdir(path):
            #loading images
            img = image.load_img(path+'/'+str(i))
    
            #converting images to array
            X = image.img_to_array(img)
            X = np.expand_dims(X,axis=0)
            images = np.vstack([X])

            #predicting labels
            val =  model.predict(images)
            if val == 0:
                count += 1
            else:
                count -= 1
        if count >= 0:
            return 1
        else:
            return 0
