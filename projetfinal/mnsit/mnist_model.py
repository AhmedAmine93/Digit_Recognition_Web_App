import os
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Obtenez le chemin absolu du répertoire du script en cours d'exécution
current_directory = os.path.dirname(os.path.abspath(__file__))

# Spécifiez le nom du fichier modèle
MODEL_FILENAME = "model_local.h5"

# Créez le chemin absolu complet du modèle
MODEL_PATH = os.path.join(current_directory, MODEL_FILENAME)

# Chargez le modèle à partir du chemin absolu
model = load_model(MODEL_PATH)


# Le reste de votre code de prédiction
def predict(image):
    image = Image.open(image)
    image = image.convert("L")
    image = image.resize((28, 28))
    image_array = np.array(image)

    image_array = image_array.astype("float32")
    image_array /= 255.0

    image_array = np.expand_dims(image_array, axis=0)
    image_array = np.expand_dims(image_array, axis=-1)

    predictions = model.predict(image_array)
    prediction = np.argmax(predictions, axis=1)[0]

    return prediction
