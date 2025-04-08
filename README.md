# Vegetable Image Classifier with Raspberry Pi, ESP32 and Weight Sensor

This project combines image classification and weight measurement to predict vegetables based on images captured by a camera. The system uses an **ESP32** weight sensor for detecting changes in weight and triggering the image capture and prediction process.

## Overview

The project integrates the following components:

- **Raspberry Pi**: Running the overall system and managing the processes.
- **ESP32 Weight Sensor (HX711)**: Used for measuring weight changes. It triggers image capture when a significant change in weight is detected.
- **Camera**: Captures an image of the object when triggered by the weight sensor.
- **Machine Learning Model**: Classifies the captured image to predict the vegetable based on predefined categories (Carrot, Cucumber, Tomato, etc.).

## Components

1. **Raspberry Pi (Raspberry Pi OS)**: This serves as the primary processing unit for the system. The system is programmed to run on the Raspberry Pi and utilizes the camera and ESP32 for interacting with the external environment.
   
2. **ESP32 HX711**: The ESP32 is connected to a weight sensor, which is used to measure weight. When a significant change in weight is detected, the system triggers an image capture process.

3. **Camera**: A camera is connected to the Raspberry Pi to capture an image when a significant weight change is detected. The image is then processed and classified using a machine learning model.

4. **Machine Learning Model**: This model uses image data to classify the object in the captured image into one of several vegetable categories.

## Requirements

### Hardware

- **Raspberry Pi** (any version that supports RPi OS)
- **ESP32** with **HX711 weight sensor** for measuring weight
- **Camera module** for Raspberry Pi (e.g., Raspberry Pi Camera Module v2)

### Software

- **Python 3.x**
- **Raspberry Pi OS** (installed on your Raspberry Pi)
- **Libraries**:
  - `opencv-python` for image capture
  - `tensorflow` for the machine learning model (image classification)
  - `subprocess` for managing subprocesses
  - `time` for timing-related functions

### Setup Instructions

1. **Install Raspberry Pi OS**: Ensure that Raspberry Pi OS is installed and properly configured on your Raspberry Pi.

2. **Set up ESP32**:
   - Connect the ESP32 with the HX711 sensor to your Raspberry Pi via GPIO pins.
   - Ensure that the ESP32 is correctly configured and able to transmit data.

3. **Install Dependencies**:
   On your Raspberry Pi, install the required Python libraries by running:

   ```bash
   pip install opencv-python tensorflow
   ```

4. **Configure the Environment**:
   - Set up your virtual environment (optional but recommended for isolating dependencies):
     ```bash
     python3 -m venv /path/to/your/venv
     source /path/to/your/venv/bin/activate
     ```
   - Install the necessary dependencies inside the virtual environment.

5. **Run the System**:
   - Run the `sync.py` script to start the system. This will initialize the ESP32, capture an image when weight change is detected, and classify the image using the trained machine learning model.
   
   ```bash
   python sync.py
   ```

6. **Test the System**:
   Once everything is set up, the system should be ready. Test it by placing objects on the weight sensor, and the system will automatically capture the image and predict the vegetable.

## Workflow

1. **Weight Measurement**: The ESP32 continuously monitors the weight through the HX711 sensor. When a significant weight change (e.g., more than 1000 units) is detected, the system will proceed to capture an image.
   
2. **Image Capture**: The Raspberry Pi triggers the camera to take a snapshot of the object placed on the scale.

3. **Image Classification**: The captured image is passed through a pre-trained machine learning model that predicts the object’s category (Carrot, Cucumber, Tomato, etc.).

4. **Prediction Output**: The system displays the predicted label and the top three closest matches, along with their confidence scores.

## How to Use

1. **Start the Process**: Run the `sync.py` script, which coordinates the entire process.
   ```bash
   python sync.py
   ```

2. **Interaction**:
   - Place a vegetable or object on the weight sensor to trigger the process.
   - The system will automatically capture an image and predict the vegetable.

3. **Prediction Output**: The system will show the predicted vegetable and the top 3 closest matches.

## Troubleshooting

- **ESP32 Not Responding**: Ensure the ESP32 is correctly connected to the Raspberry Pi via the GPIO pins and that the firmware is functioning correctly.
- **Camera Issues**: Verify that the camera is properly connected and that the Raspberry Pi recognizes it.
- **Machine Learning Model Errors**: Ensure that the model is trained correctly and that all required dependencies are installed.

## Future Improvements

- **Model Improvement**: Train the machine learning model with a larger dataset of vegetables to increase classification accuracy.
- **Real-time Feedback**: Provide real-time feedback on the system’s predictions, such as a GUI or web interface.
- **Automation**: Automate the entire workflow with additional sensors and functionalities.

