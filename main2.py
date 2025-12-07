import os
import numpy as np
import tensorflow as tf
from PIL import Image as PILImage

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image as KivyImage
from kivy.uix.filechooser import FileChooserIconView

# Path to your pretrained Keras model (.h5)
MODEL_PATH = './fracture_classification_model.h5'

# Preprocessing helper that adapts to model's input shape
def load_preprocessed_image(image_path, model):
    """
    Loads, resizes, normalizes the image according to model.input_shape.
    Returns a numpy array of shape (1, H, W, C).
    """
    input_shape = model.input_shape  # (None, H, W, C)
    if not (isinstance(input_shape, tuple) and len(input_shape) == 4):
        raise ValueError(f"Model input_shape must be 4D, got {input_shape}")
    _, H, W, C = input_shape

    img = PILImage.open(image_path)
    if C == 1:
        img = img.convert('L')
    else:
        img = img.convert('RGB')
    img = img.resize((W, H))

    arr = np.array(img, dtype=np.float32)
    if C == 1:
        arr = np.expand_dims(arr, axis=-1)
    arr /= 255.0
    return np.expand_dims(arr, axis=0)

class FractureDetectorApp(App):
    def build(self):
        # Load full model (architecture + weights)
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        self.model = tf.keras.models.load_model(MODEL_PATH)

        root = BoxLayout(orientation='vertical', spacing=10, padding=10)
        # File chooser
        self.filechooser = FileChooserIconView(size_hint=(1, 0.5))
        self.filechooser.bind(selection=self.on_file_select)
        root.add_widget(self.filechooser)
        # Image preview
        self.image = KivyImage(size_hint=(1, 0.35), allow_stretch=True)
        root.add_widget(self.image)
        # Footer
        footer = BoxLayout(size_hint=(1, 0.15), spacing=10)
        classify_btn = Button(text='Classify', size_hint=(0.3, 1))
        classify_btn.bind(on_release=self.classify_image)
        self.result_label = Label(text='Select an X-ray image.', halign='left', valign='middle')
        footer.add_widget(classify_btn)
        footer.add_widget(self.result_label)
        root.add_widget(footer)
        return root

    def on_file_select(self, chooser, selection):
        if selection:
            self.selected = selection[0]
            self.image.source = self.selected
            self.result_label.text = 'Ready to classify.'

    def classify_image(self, instance):
        if not hasattr(self, 'selected'):
            self.result_label.text = 'No image selected.'
            return
        try:
            img_array = load_preprocessed_image(self.selected, self.model)
            preds = self.model.predict(img_array)
            idx = int((preds > 0.5).astype('int32')[0][0])
            class_names = ['fractured', 'not fractured']
            label = class_names[idx]
            confidence = float(preds[0][0])
            self.result_label.text = f'{label} ({confidence:.2f})'
        except Exception as e:
            self.result_label.text = f'Error: {e}'

if __name__ == '__main__':
    FractureDetectorApp().run()