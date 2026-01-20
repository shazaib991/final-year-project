import 'package:flutter/material.dart';

class PredictionResultPage extends StatelessWidget {
  final Map<String, dynamic> result;

  const PredictionResultPage({Key? key, required this.result})
    : super(key: key);

  @override
  Widget build(BuildContext context) {
    final label = result['label'] ?? 'Unknown';
    final confidence = (result['confidence'] ?? 0.0) as num;
    final isFractured =
        label.toString().toLowerCase().contains('fractured') &&
        !label.toString().toLowerCase().contains('not');

    // Calculate percentage and confidence for display
    double confidencePercentage;
    if (isFractured) {
      // If fractured, confidence is 1 - raw_prediction
      confidencePercentage = ((1 - confidence) * 100).clamp(0, 100).toDouble();
    } else {
      // If not fractured, confidence is raw_prediction
      confidencePercentage = (confidence * 100).clamp(0, 100).toDouble();
    }

    return Scaffold(
      appBar: AppBar(
        title: const Text('Analysis Result'),
        backgroundColor: Colors.blue,
        elevation: 0,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 30),
              Container(
                padding: const EdgeInsets.all(30),
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: isFractured
                      ? Colors.red.shade100
                      : Colors.green.shade100,
                ),
                child: Icon(
                  isFractured
                      ? Icons.warning_rounded
                      : Icons.check_circle_rounded,
                  size: 100,
                  color: isFractured ? Colors.red : Colors.green,
                ),
              ),
              const SizedBox(height: 30),
              Text(
                isFractured ? 'Fracture Detected' : 'No Fracture Detected',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: isFractured ? Colors.red : Colors.green,
                ),
              ),
              const SizedBox(height: 10),
              Text(
                'Result: $label',
                textAlign: TextAlign.center,
                style: const TextStyle(
                  fontSize: 18,
                  color: Colors.black87,
                  fontWeight: FontWeight.w500,
                ),
              ),
              const SizedBox(height: 40),
              Card(
                elevation: 4,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Padding(
                  padding: const EdgeInsets.all(20.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      const Text(
                        'Confidence Level',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: Colors.black87,
                        ),
                      ),
                      const SizedBox(height: 16),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            '${confidencePercentage.toStringAsFixed(1)}%',
                            style: TextStyle(
                              fontSize: 32,
                              fontWeight: FontWeight.bold,
                              color: _getConfidenceColor(confidencePercentage),
                            ),
                          ),
                          Text(
                            _getConfidenceLabel(confidencePercentage),
                            style: TextStyle(
                              fontSize: 14,
                              color: Colors.grey.shade600,
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 16),
                      ClipRRect(
                        borderRadius: BorderRadius.circular(8),
                        child: LinearProgressIndicator(
                          value: confidencePercentage / 100,
                          minHeight: 8,
                          backgroundColor: Colors.grey.shade200,
                          valueColor: AlwaysStoppedAnimation<Color>(
                            _getConfidenceColor(confidencePercentage),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 30),
              Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.blue.shade50,
                  border: Border.all(color: Colors.blue.shade200),
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Icon(Icons.info_outline, color: Colors.blue.shade700),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Text(
                            'Medical Disclaimer',
                            style: TextStyle(
                              fontSize: 14,
                              fontWeight: FontWeight.bold,
                              color: Colors.blue.shade700,
                            ),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 12),
                    Text(
                      'This analysis is AI-powered and should not replace professional medical diagnosis. Please consult with a qualified radiologist or medical professional for accurate diagnosis and treatment.',
                      style: TextStyle(
                        fontSize: 12,
                        color: Colors.blue.shade600,
                        height: 1.5,
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 30),
              Row(
                children: [
                  Expanded(
                    child: ElevatedButton(
                      onPressed: () {
                        Navigator.pop(context);
                      },
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.grey,
                        padding: const EdgeInsets.symmetric(vertical: 12),
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(12),
                        ),
                      ),
                      child: const Text(
                        'Back',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: ElevatedButton(
                      onPressed: () {
                        Navigator.popUntil(context, (route) => route.isFirst);
                      },
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.blue,
                        padding: const EdgeInsets.symmetric(vertical: 12),
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(12),
                        ),
                      ),
                      child: const Text(
                        'New Analysis',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ),
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 20),
            ],
          ),
        ),
      ),
    );
  }

  Color _getConfidenceColor(double percentage) {
    if (percentage >= 80) {
      return Colors.green;
    } else if (percentage >= 60) {
      return Colors.orange;
    } else {
      return Colors.red;
    }
  }

  String _getConfidenceLabel(double percentage) {
    if (percentage >= 80) {
      return 'Very High';
    } else if (percentage >= 60) {
      return 'Good';
    } else if (percentage >= 40) {
      return 'Fair';
    } else {
      return 'Low';
    }
  }
}
