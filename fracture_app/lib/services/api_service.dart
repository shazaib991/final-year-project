import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../utils/constants.dart';

class ApiService {
  static Future<Map<String, dynamic>> signup(String username, String password) async {
    try {
      final response = await http
          .post(
            Uri.parse(Constants.signupEndpoint),
            headers: {'Content-Type': 'application/json'},
            body: jsonEncode({
              'username': username,
              'password': password,
              're_password': password,
              'email': '', // Empty email - backend will auto-generate
            }),
          )
          .timeout(
            const Duration(seconds: 15),
            onTimeout: () => throw Exception('Request timeout'),
          );

      if (response.statusCode == 201) {
        return {'success': true};
      }
      
      // Parse error response
      print("Signup Error: ${response.statusCode} - ${response.body}");
      try {
        final errorData = jsonDecode(response.body);
        String errorMessage = '';
        
        // Extract error messages from Django validation response
        if (errorData is Map<String, dynamic>) {
          if (errorData.containsKey('password')) {
            errorMessage = errorData['password'][0];
          } else if (errorData.containsKey('username')) {
            errorMessage = errorData['username'][0];
          } else if (errorData.containsKey('non_field_errors')) {
            errorMessage = errorData['non_field_errors'][0];
          } else {
            errorMessage = 'Signup failed. Please check your input.';
          }
        }
        return {'success': false, 'error': errorMessage};
      } catch (e) {
        return {'success': false, 'error': 'Signup failed. Please try again.'};
      }
    } catch (e) {
      print("Signup Exception: $e");
      return {'success': false, 'error': 'Network error. Please check your connection.'};
    }
  }

  static Future<String?> login(String username, String password) async {
    try {
      final response = await http
          .post(
            Uri.parse(Constants.loginEndpoint),
            headers: {'Content-Type': 'application/json'},
            body: jsonEncode({'username': username, 'password': password}),
          )
          .timeout(
            const Duration(seconds: 15),
            onTimeout: () => throw Exception('Request timeout'),
          );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final token = data['auth_token'];
        // Save token
        final prefs = await SharedPreferences.getInstance();
        await prefs.setString('auth_token', token);
        return token;
      }
      print("Login Error: ${response.statusCode} - ${response.body}");
      return null;
    } catch (e) {
      print("Login Exception: $e");
      return null;
    }
  }

  static Future<void> logout() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('auth_token');
  }

  static Future<String?> getAuthToken() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString('auth_token');
  }

  static Future<Map<String, dynamic>?> predict(String imagePath) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final token = prefs.getString('auth_token');

      var request = http.MultipartRequest(
        'POST',
        Uri.parse(Constants.predictEndpoint),
      );

      if (token != null) {
        request.headers['Authorization'] = 'Token $token';
      }

      request.files.add(await http.MultipartFile.fromPath('image', imagePath));

      final streamedResponse = await request.send().timeout(
        const Duration(seconds: 30),
        onTimeout: () => throw Exception('Prediction request timeout'),
      );
      final response = await http.Response.fromStream(streamedResponse);

      if (response.statusCode == 200) {
        return jsonDecode(response.body);
      }
      print("Predict Error: ${response.statusCode} - ${response.body}");
      return null;
    } catch (e) {
      print("Predict Exception: $e");
      return null;
    }
  }
}
