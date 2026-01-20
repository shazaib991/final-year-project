
<img width="1365" height="717" alt="Screenshot 2025-12-23 150219" src="https://github.com/user-attachments/assets/f5677844-7f97-4169-badf-4817b844d5b6" />

<img width="1363" height="716" alt="Screenshot 2025-12-23 150317" src="https://github.com/user-attachments/assets/f12eb40d-4137-4e91-9aab-ed41acf75167" />

<img width="1365" height="720" alt="Screenshot 2025-12-23 150416" src="https://github.com/user-attachments/assets/9ac3c000-9888-4403-9e9b-7cd28a3e62f4" />

<img width="1365" height="715" alt="Screenshot 2025-12-23 150444" src="https://github.com/user-attachments/assets/16516185-a05c-4edf-a2a8-26e0bc86ad3b" />

<img width="1364" height="716" alt="Screenshot 2025-12-23 150505" src="https://github.com/user-attachments/assets/98874762-03b0-47f6-ace4-6802b15f5f54" />

<img width="1599" height="762" alt="Screenshot 2026-01-18 141111" src="https://github.com/user-attachments/assets/e7b5b578-f36d-492b-bad0-c8f5557873ba" />

<img width="1599" height="763" alt="Screenshot 2026-01-18 141141" src="https://github.com/user-attachments/assets/7ba618ce-6f9f-4521-9f15-b3ae11f38bfb" />

<img width="1599" height="763" alt="Screenshot 2026-01-18 141354" src="https://github.com/user-attachments/assets/a483bbbf-1538-41d2-b375-91813c312b82" />

<img width="441" height="753" alt="Screenshot 2026-01-20 221256" src="https://github.com/user-attachments/assets/2c4026e9-fffd-4e00-b7cc-e9e12c7a3fff" />

-   Bone Fracture Detection & Classification System
    An intelligent medical imaging system designed to automate the detection and classification of bone fractures from X-ray images. This project aims to assist medical professionals by providing a fast, reliable "second opinion" to reduce diagnostic errors and improve patient outcomes.

-   Overview
    Bone fractures are a common yet critical medical issue requiring precise and timely diagnosis. This project leverages Convolutional Neural Networks (CNN) to analyze radiographic images and categorize them as either fractured or healthy. The system includes a user management backend for secure access and data handling.

Key Features
Automated Detection: Real-time classification of bone fractures from uploaded X-ray images.

User Authentication: Secure Login and Registration system managed via a local SQLite database.

Pre-trained Model: Utilizes a highly optimized .h5 model for accurate predictions.

Dataset Integration: Built and tested using a comprehensive Bone Fracture Dataset.

Results Tracking: (Optional feature) Logs and manages patient/user diagnostic history.

-   Tech Stack
    Language: Python 3.x, react, django

Deep Learning: TensorFlow, Keras

Image Processing: OpenCV, PIL (Pillow), NumPy

Database: SQLite3

Frontend/GUI: kivy, react

Version Control: Git & GitHub

-   Project Structure
    Bash

├── BoneFractureDataset/ # Training and validation image data
├── backend/ # backend for api
├── frontend/ # frontend web
├── database.py # SQLite database logic and schema
├── users.db # Local storage for user credentials
├── fracture_classification_model.h5 # Pre-trained CNN model
├── main2.py # Main application entry point
├── .gitignore # Files to ignore in version control
└── README.md # Project documentation

-   Installation & Setup
    Follow these steps to set up the project on your local machine:

1. Clone the Repository
   Bash

# for kivy app:

git clone https://github.com/shazaib991/final-year-project.git
1. cd final-year-project
2. Create a Virtual Environment python -m venv venv or conda activate "environment name"
3. python main2.py

# or for frontend web:

git clone https://github.com/shazaib991/final-year-project.git
1. cd final-year-project frontend/
2. create react app and npm install to install all dependencies
3. npm run dev

# or for backend web api:
git clone https://github.com/shazaib991/final-year-project.git
1. cd final-year-project backend/
2. python -m venv venv or conda activate "environment name" and install packages it shows missing
3. python manage.py runserver

# Windows

venv\Scripts\activate

# Linux/Mac

source venv/bin/activate 3. Install Dependencies
Bash

pip install tensorflow opencv-python numpy pillow kivy sqlite3

-   Usage
    Initialize the Database: Run the database script to set up the user tables.

Bash

python database.py
Launch the Application: Run the main script to start the interface.

Bash

# If using standard Python:

python main2.py
Classification Process:

Log in or Register a new account.

Upload an X-ray image (JPG/PNG).

View the prediction result (Fractured / Non-Fractured) and confidence score.

-   Model Information
    The core of this project is a Convolutional Neural Network (CNN).

Input Shape: [Assuming 224x224 or 150x150]

Architecture: Multiple layers of Convolution, Max-Pooling, and Dropout for regularization.

Accuracy: 96%

Loss Function: Binary Cross-entropy

-   Contributing
    Contributions are what make the open-source community such an amazing place to learn, inspire, and create.

Fork the Project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your Changes (git commit -m 'Add some AmazingFeature').

Push to the Branch (git push origin feature/AmazingFeature).

Open a Pull Request.

-   License
    Distributed under the MIT License. See LICENSE for more information.

-   Contact
    Shazaib - @shazaib991

Project Link: https://github.com/shazaib991/final-year-project
