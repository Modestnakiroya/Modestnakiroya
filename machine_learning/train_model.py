import os
import warnings
import numpy as np
import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt

# Suppress harmless warnings
warnings.filterwarnings('ignore', category=UserWarning)

# Set random seed for reproducibility
tf.random.set_seed(42)
np.random.seed(42) 

# Constants
IMAGE_SIZE = (256, 256) 
BATCH_SIZE = 32
EPOCHS = 20
NUM_CLASSES = 2 
ANIMAL_CLASSES = 3
DATASET_DIR = '.'
CROP_MODEL_PATH = 'crop_model.keras'  
ANIMAL_MODEL_PATH = 'animal_model.keras'

def create_model(input_shape, num_classes):
    model = Sequential([
        Input(shape=input_shape),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(256, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dropout(0.5),
        Dense(512, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer=Adam(learning_rate=0.0001), 
                 loss='categorical_crossentropy',
                 metrics=['accuracy'])
    return model

def train_crop_model():
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split=0.2
    )

    train_generator = train_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "crops"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training'
    )

    validation_generator = train_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "crops"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )

    model = create_model(IMAGE_SIZE + (3,), NUM_CLASSES)

    callbacks = [
        ModelCheckpoint(CROP_MODEL_PATH, save_best_only=True, monitor='val_accuracy'),
        EarlyStopping(patience=5, restore_best_weights=True, monitor='val_accuracy')
    ]

    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // BATCH_SIZE,
        epochs=EPOCHS,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // BATCH_SIZE,
        callbacks=callbacks
    )

    plot_training_history(history)
    return model

def train_animal_filter():
    animal_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.1  # 10% of 6 images = 0.6 → rounds to 1 validation image
    )

    train_generator = animal_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "animals"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training'
    )

    validation_generator = animal_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "animals"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )

    print(f"\nAnimal training samples: {train_generator.samples}")
    print(f"Animal validation samples: {validation_generator.samples}")

    model = create_model(IMAGE_SIZE + (3,), ANIMAL_CLASSES)

    try:
        history = model.fit(
            train_generator,
            steps_per_epoch=train_generator.samples // BATCH_SIZE,
            epochs=30,  # More epochs for small dataset
            validation_data=validation_generator if validation_generator.samples > 0 else None,
            validation_steps=validation_generator.samples // BATCH_SIZE if validation_generator.samples > 0 else None
        )
    except Exception as e:
        print(f"\nWarning: Animal training encountered an issue: {str(e)}")
        print("Proceeding with untrained weights - consider adding more training data")

    model.save(ANIMAL_MODEL_PATH)
    print(f"\nAnimal model saved to {ANIMAL_MODEL_PATH}")
    return model

def plot_training_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy'] if 'val_accuracy' in history.history else None
    loss = history.history['loss']
    val_loss = history.history['val_loss'] if 'val_loss' in history.history else None

    epochs_range = range(len(acc))

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    if val_acc:
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    if val_loss:
        plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')

    plt.savefig('training_history.png')
    plt.close()

if __name__ == "__main__":
    # Check both models exist
    models_exist = all(os.path.exists(p) for p in [CROP_MODEL_PATH, ANIMAL_MODEL_PATH])
    
    if not models_exist:
        print("Training required models...")
        
        # Train crop model if needed
        if not os.path.exists(CROP_MODEL_PATH):
            print("\nTraining crop model...")
            crop_model = train_crop_model()
        
        # Train animal model if needed
        if not os.path.exists(ANIMAL_MODEL_PATH):
            print("\nTraining animal model...")
            animal_model = train_animal_filter()
    else:
        print("Loading existing models...")
        crop_model = tf.keras.models.load_model(CROP_MODEL_PATH)
        animal_model = tf.keras.models.load_model(ANIMAL_MODEL_PATH)

    # Test prediction
    test_image = "test_image.jpg"
    if os.path.exists(test_image):
        prediction = predict_image(crop_model, animal_model, test_image)
        print("\nPrediction Results:")
        print(f"Type: {prediction['type']}")
        print(f"Class: {prediction['class']}")
        print(f"Confidence: {prediction['confidence']:.2%}")
    else:
        print(f"\nTest image {test_image} not found - using random image for demo")
        # Add demo prediction code if you want