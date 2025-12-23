-project image1
<img width="1365" height="717" alt="Screenshot 2025-12-23 150219" src="https://github.com/user-attachments/assets/bf0a7deb-ac9f-411c-87aa-42908289ba0b" />
-project image2
<img width="1363" height="716" alt="Screenshot 2025-12-23 150317" src="https://github.com/user-attachments/assets/0c685da5-5f4e-4565-a7f9-5731e1203781" />
-project image3
<img width="1365" height="720" alt="Screenshot 2025-12-23 150416" src="https://github.com/user-attachments/assets/142f92e4-2b67-45a2-baed-88aea9d6ac09" />
-project image4
<img width="1365" height="715" alt="Screenshot 2025-12-23 150444" src="https://github.com/user-attachments/assets/39113076-aa4c-4e75-b74f-e36b32f6d469" />
-project image5
<img width="1364" height="716" alt="Screenshot 2025-12-23 150505" src="https://github.com/user-attachments/assets/e64c4ecf-06b1-4f10-b8f3-c76d1f3e753d" />


- Bone Fracture Detection & Classification System
An intelligent medical imaging system designed to automate the detection and classification of bone fractures from X-ray images. This project aims to assist medical professionals by providing a fast, reliable "second opinion" to reduce diagnostic errors and improve patient outcomes.

- Overview
Bone fractures are a common yet critical medical issue requiring precise and timely diagnosis. This project leverages Convolutional Neural Networks (CNN) to analyze radiographic images and categorize them as either fractured or healthy. The system includes a user management backend for secure access and data handling.

Key Features
Automated Detection: Real-time classification of bone fractures from uploaded X-ray images.

User Authentication: Secure Login and Registration system managed via a local SQLite database.

Pre-trained Model: Utilizes a highly optimized .h5 model for accurate predictions.

Dataset Integration: Built and tested using a comprehensive Bone Fracture Dataset.

Results Tracking: (Optional feature) Logs and manages patient/user diagnostic history.

- Tech Stack
Language: Python 3.x

Deep Learning: TensorFlow, Keras

Image Processing: OpenCV, PIL (Pillow), NumPy

Database: SQLite3

Frontend/GUI: Streamlit / Flask (likely used in main2.py)

Version Control: Git & GitHub

- Project Structure
Bash

├── BoneFractureDataset/        # Training and validation image data
├── database.py                 # SQLite database logic and schema
├── users.db                    # Local storage for user credentials
├── fracture_classification_model.h5  # Pre-trained CNN model
├── main2.py                    # Main application entry point
├── .gitignore                  # Files to ignore in version control
└── README.md                   # Project documentation
- Installation & Setup
Follow these steps to set up the project on your local machine:

1. Clone the Repository
Bash

git clone https://github.com/shazaib991/final-year-project.git
cd final-year-project
2. Create a Virtual Environment
Bash

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
3. Install Dependencies
Bash

pip install tensorflow opencv-python numpy pillow streamlit sqlite3
(Note: Replace streamlit with the appropriate framework if you used Flask or Tkinter).

- Usage
Initialize the Database: Run the database script to set up the user tables.

Bash

python database.py
Launch the Application: Run the main script to start the interface.

Bash

# If using Streamlit:
streamlit run main2.py

# If using standard Python:
python main2.py
Classification Process:

Log in or Register a new account.

Upload an X-ray image (JPG/PNG).

View the prediction result (Fractured / Non-Fractured) and confidence score.

- Model Information
The core of this project is a Convolutional Neural Network (CNN).

Input Shape: [Assuming 224x224 or 150x150]

Architecture: Multiple layers of Convolution, Max-Pooling, and Dropout for regularization.

Accuracy: [Insert your model's accuracy, e.g., 92%]

Loss Function: Binary Cross-entropy

- Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create.

Fork the Project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your Changes (git commit -m 'Add some AmazingFeature').

Push to the Branch (git push origin feature/AmazingFeature).

Open a Pull Request.

- License
Distributed under the MIT License. See LICENSE for more information.

- Contact
Shazaib - @shazaib991

Project Link: https://github.com/shazaib991/final-year-project
