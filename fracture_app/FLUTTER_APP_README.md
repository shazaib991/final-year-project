# Bone Fracture Detection Flutter App

A comprehensive Flutter application for detecting bone fractures from X-ray images using AI/ML. The app features user authentication, image upload capabilities, and real-time prediction with confidence scores.

## Features

### 1. **User Authentication**

- **Sign Up**: Create a new account with username and password
- **Login**: Authenticate existing users with token-based authentication
- **Logout**: Secure logout with token cleanup
- Session persistence using SharedPreferences

### 2. **Image Analysis**

- Upload X-ray images from gallery or camera
- Real-time prediction using the backend Django API
- Display prediction results with confidence scores
- Support for both fractured and non-fractured bones

### 3. **Results Display**

- Clear indication if bone is fractured or not
- Confidence percentage with visual progress indicator
- Color-coded confidence levels (Red/Orange/Green)
- Medical disclaimer for user awareness
- Options to perform new analysis or go back

## Setup Instructions

### Prerequisites

- Flutter SDK 3.10.4 or higher
- Backend Django server running (see backend folder)
- Android/iOS device or emulator
- Internet connection

### Installation

1. **Install Dependencies**

    ```bash
    cd fracture_app
    flutter pub get
    ```

2. **Configure Backend URL**
    - Edit `lib/utils/constants.dart`
    - Update `baseUrl` if needed:
        - Android Emulator: `http://10.0.2.2:8000`
        - iOS/Web/Windows/macOS: `http://127.0.0.1:8000`
        - Physical device: Use your machine's LAN IP (e.g., `http://192.168.1.x:8000`)

3. **Run the App**
    ```bash
    flutter run
    ```

## Project Structure

```
lib/
├── main.dart                          # App entry point & auth check
├── pages/
│   ├── login_page.dart               # Login UI & logic
│   ├── signup_page.dart              # Sign up UI & logic
│   ├── home_page.dart                # Main image upload page
│   └── prediction_result_page.dart   # Results display page
├── services/
│   └── api_service.dart              # Backend API communication
└── utils/
    └── constants.dart                # API endpoints & base URL
```

## API Integration

### Backend Endpoints

1. **Sign Up**: `POST /auth/users/`
    - Body: `{"username": "...", "password": "...", "email": "..."}`
    - Response: User created

2. **Login**: `POST /auth/token/login/`
    - Body: `{"username": "...", "password": "..."}`
    - Response: `{"auth_token": "..."}`

3. **Predict**: `POST /api/predict/`
    - Headers: `Authorization: Token <token>`
    - Body: Multipart form with `image` file
    - Response:
        ```json
        {
        	"label": "fractured|not fractured",
        	"confidence": 0.85,
        	"raw_prediction": 0.15
        }
        ```

## Dependencies

- **http**: HTTP client for API calls
- **shared_preferences**: Local token storage
- **image_picker**: Camera/gallery image selection
- **fluttertoast**: Toast notifications
- **google_fonts**: Custom fonts (optional)

## Usage Flow

1. **First Time Users**
    - Click "Sign up" on login page
    - Enter username and password
    - Account created successfully
    - Return to login page and sign in

2. **Existing Users**
    - Enter credentials on login page
    - Click "Login"
    - Redirected to home page if successful

3. **Image Analysis**
    - Click "Gallery" to select existing image or "Camera" to capture new one
    - Image displayed in preview area
    - Click "Analyze Image" to send to backend
    - Wait for processing
    - View results with confidence score

4. **Logout**
    - Click logout button (top right of AppBar)
    - Redirected to login page
    - Auth token cleared from device

## Important Notes

⚠️ **Medical Disclaimer**: This application is for educational and demonstration purposes only. Results should not be used for clinical diagnosis. Always consult with qualified medical professionals.

## Troubleshooting

### Connection Issues

- Ensure backend server is running on configured URL
- Check firewall settings
- Verify network connectivity
- Use correct IP for physical devices

### Image Upload Fails

- Ensure image file is not corrupted
- Check file size (should be reasonable for ML model)
- Verify camera/gallery permissions granted

### Authentication Issues

- Clear app cache: `flutter clean`
- Rebuild app: `flutter run`
- Check backend authentication configuration
- Verify token format in API responses

## Future Enhancements

- [ ] Support for multiple image formats
- [ ] Batch prediction capabilities
- [ ] Prediction history/records
- [ ] User profile management
- [ ] Dark mode support
- [ ] Offline mode
- [ ] Multiple language support

## License

This project is part of the Final Year Project for Bone Fracture Detection System.

## Support

For issues or questions, please refer to the backend documentation or contact the development team.
