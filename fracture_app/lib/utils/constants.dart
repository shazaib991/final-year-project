
import 'dart:io';
import 'package:flutter/foundation.dart';

class Constants {
  // Use 10.0.2.2 for Android Emulator, localhost for iOS/Web/Windows
  // If using a physical device, use your machine's LAN IP (e.g., 192.168.1.x)
  static String get baseUrl {
    if (kIsWeb || Platform.isWindows || Platform.isMacOS || Platform.isLinux) {
      return "http://127.0.0.1:8000";
    } else if (Platform.isAndroid) {
       return "http://10.0.2.2:8000";
    } else {
      return "http://localhost:8000";
    }
  }

  static String get loginEndpoint => "$baseUrl/auth/token/login/";
  static String get signupEndpoint => "$baseUrl/auth/users/";
  static String get predictEndpoint => "$baseUrl/api/predict/";
}
