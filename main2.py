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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

import database

# Path to your pretrained Keras model (.h5)
MODEL_PATH = './fracture_classification_model.h5'

# Preprocessing helper
def load_preprocessed_image(image_path, model):
    input_shape = model.input_shape
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

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        
        layout.add_widget(Label(text='Fracture Detector Login', font_size=24, size_hint=(1, 0.2)))
        
        self.username = TextInput(hint_text='Username', multiline=False, size_hint=(1, 0.15))
        layout.add_widget(self.username)
        
        self.password = TextInput(hint_text='Password', password=True, multiline=False, size_hint=(1, 0.15))
        layout.add_widget(self.password)
        
        layout.add_widget(Label(size_hint=(1, 0.1))) # Spacer
        
        btn_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)
        login_btn = Button(text='Login')
        login_btn.bind(on_release=self.do_login)
        btn_layout.add_widget(login_btn)
        
        signup_btn = Button(text='Go to Signup')
        signup_btn.bind(on_release=self.go_signup)
        btn_layout.add_widget(signup_btn)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
        
    def do_login(self, instance):
        username = self.username.text
        password = self.password.text
        
        if database.authenticate_user(username, password):
            self.manager.current = 'main'
            self.username.text = ''
            self.password.text = ''
        else:
            self.show_popup("Login Failed", "Invalid username or password")
            
    def go_signup(self, instance):
        self.manager.current = 'signup'
        
    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text=message))
        btn = Button(text='Close', size_hint=(1, 0.25))
        content.add_widget(btn)
        popup = Popup(title=title, content=content, size_hint=(0.6, 0.4))
        btn.bind(on_release=popup.dismiss)
        popup.open()

class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        
        layout.add_widget(Label(text='Create Account', font_size=24, size_hint=(1, 0.2)))
        
        self.username = TextInput(hint_text='Choose Username', multiline=False, size_hint=(1, 0.15))
        layout.add_widget(self.username)
        
        self.password = TextInput(hint_text='Choose Password', password=True, multiline=False, size_hint=(1, 0.15))
        layout.add_widget(self.password)
        
        layout.add_widget(Label(size_hint=(1, 0.1))) # Spacer
        
        btn_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)
        register_btn = Button(text='Register')
        register_btn.bind(on_release=self.do_register)
        btn_layout.add_widget(register_btn)
        
        back_btn = Button(text='Back to Login')
        back_btn.bind(on_release=self.go_login)
        btn_layout.add_widget(back_btn)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
        
    def do_register(self, instance):
        username = self.username.text
        password = self.password.text
        
        if not username or not password:
            self.show_popup("Error", "All fields are required")
            return
            
        if database.register_user(username, password):
            self.show_popup("Success", "Account created! Please login.")
            self.manager.current = 'login'
            self.username.text = ''
            self.password.text = ''
        else:
            self.show_popup("Error", "Username already exists")
            
    def go_login(self, instance):
        self.manager.current = 'login'

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text=message))
        btn = Button(text='Close', size_hint=(1, 0.25))
        content.add_widget(btn)
        popup = Popup(title=title, content=content, size_hint=(0.6, 0.4))
        btn.bind(on_release=popup.dismiss)
        popup.open()

class MainScreen(Screen):
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.app = app_instance
        
        root = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Header with Logout
        header = BoxLayout(size_hint=(1, 0.1))
        header.add_widget(Label(text="Bone Fracture Detector", size_hint=(0.7, 1), font_size=20))
        logout_btn = Button(text="Logout", size_hint=(0.3, 1))
        logout_btn.bind(on_release=self.logout)
        header.add_widget(logout_btn)
        root.add_widget(header)

        # File chooser
        self.filechooser = FileChooserIconView(size_hint=(1, 0.45))
        self.filechooser.bind(selection=self.on_file_select)
        root.add_widget(self.filechooser)
        
        # Image preview
        self.image = KivyImage(size_hint=(1, 0.35), allow_stretch=True)
        root.add_widget(self.image)
        
        # Footer
        footer = BoxLayout(size_hint=(1, 0.1), spacing=10)
        classify_btn = Button(text='Classify', size_hint=(0.3, 1))
        classify_btn.bind(on_release=self.classify_image)
        self.result_label = Label(text='Select an X-ray image.', halign='left', valign='middle')
        footer.add_widget(classify_btn)
        footer.add_widget(self.result_label)
        root.add_widget(footer)
        
        self.add_widget(root)

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
            # Re-using the model loaded in the App instance
            img_array = load_preprocessed_image(self.selected, self.app.model)
            preds = self.app.model.predict(img_array)
            idx = int((preds > 0.5).astype('int32')[0][0])
            class_names = ['fractured', 'not fractured']
            label = class_names[idx]
            confidence = float(preds[0][0])
            self.result_label.text = f'{label} ({confidence:.2f})'
        except Exception as e:
            self.result_label.text = f'Error: {e}'
            
    def logout(self, instance):
        self.manager.current = 'login'
        self.image.source = ''
        self.result_label.text = 'Select an X-ray image.'
        # Optional: clear selection in filechooser if possible

class FractureDetectorApp(App):
    def build(self):
        # Load full model (architecture + weights)
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        self.model = tf.keras.models.load_model(MODEL_PATH)

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(MainScreen(name='main', app_instance=self))
        
        return sm

if __name__ == '__main__':
    FractureDetectorApp().run()