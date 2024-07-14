import cv2
import numpy as np
from tensorflow.keras.models import load_model

class AuroraAxiomComputerVision:
    def __init__(self):
        self.model = load_model('object_detection_model.h5')

    def detect_objects(self, image_path):
        image = cv2.imread(image_path)
image = cv2.resize(image, (224, 224))
        image = image / 255.0
        image = np.expand_dims(image, axis=0)
        predictions = self.model.predict(image)
        return predictions

computer_vision = AuroraAxiomComputerVision()
