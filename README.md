# Smart Warehouse Management System with Raspberry Pi, ESP32, and Weight Sensor

<a href="https://www.youtube.com/watch?v=yazTxDFBqBg">
  <img src="Photos_demo/thumbnail.PNG" width="75%" alt="Video Thumbnail">
</a>


## Project Overview

This project implements a **Smart Warehouse Management System** utilizing **Raspberry Pi**, **ESP32**, and a **weight sensor**. The system is designed to automatically monitor and classify inventory, specifically vegetables, based on weight measurements and image capture. By leveraging a weight sensor connected to an ESP32 microcontroller, the system triggers image capture for machine learning-based classification. This intelligent solution can be scaled to handle inventory management in warehouses, optimizing the process of tracking and categorizing items in real time.

## Key Features

- **Smart Warehouse Management**: The system automates the process of tracking inventory items in a warehouse, providing real-time data and classification of goods based on weight and visual recognition.
  
- **Integration of Raspberry Pi & ESP32**: The ESP32 is used to read weight measurements, and the Raspberry Pi handles image processing and machine learning tasks.
  
- **Weight-Triggered Image Capture**: The ESP32 reads weight changes, and when a significant change is detected, it triggers the capture of an image using the Raspberry Pi camera.
  
- **Vegetable Classification**: Using a pre-trained machine learning model, the captured images are analyzed to classify the vegetable stored based on its visual features.

- **Real-Time Predictions**: Once an image is captured, it is sent to a machine learning model running in a virtual environment on the Raspberry Pi for classification. The predicted label and probability of classification are then displayed.

## Technologies Used

- **Raspberry Pi**: Used for image capture, processing, and running machine learning models.
- **ESP32**: A microcontroller that reads weight data from the weight sensor and triggers image capture.
- **HX711 Weight Sensor**: Used to measure the weight of the items in the warehouse.
- **Python**: Programming language used for backend development, including image processing, machine learning, and sensor integration.
- **TensorFlow**: Framework for machine learning, used to classify the vegetables based on captured images.
- **OpenCV**: Library for image processing and camera interaction.
- **subprocess module**: Used for managing and running separate scripts and processes for sensor reading, image capturing, and machine learning predictions.

## Project Structure

- **capture_image.py**: Script that interfaces with the Raspberry Pi camera to capture images when triggered by a weight change.
- **esp32_hx711_reader.py**: Script that reads weight data from the ESP32 and communicates weight changes to the Raspberry Pi.
- **predict_image.py**: Script that takes the captured image, processes it, and uses a trained machine learning model to predict the type of vegetable.
- **sync.py**: Main script that coordinates the entire process, starting from the weight sensor reading, through image capture, to prediction.

## How It Works

1. **Weight Sensor Activation**: The ESP32 reads the weight data from the connected HX711 weight sensor. If a significant weight change is detected, it triggers the image capture process.
   
2. **Image Capture**: The Raspberry Pi camera captures an image of the item whose weight has changed. The image is saved for processing.
   
3. **Prediction**: The captured image is sent to a machine learning model running on the Raspberry Pi, which classifies the item (in this case, vegetables). The top predicted labels and their probabilities are displayed.

4. **Warehouse Management**: The system can be scaled to handle a wide variety of items in a warehouse, offering an efficient method for tracking and classifying goods.

## Requirements

- **Raspberry Pi** with Raspberry Pi OS
- **ESP32** with HX711 weight sensor connected
- **Python 3** and required libraries:
  - `tensorflow`
  - `opencv-python`
  - `subprocess`
  - `time`
  - `os`
  - `Raspberry Pi camera module setup (libcamera, PiCamera)`

## Installation

1. **Set up the environment**:
   - Ensure your Raspberry Pi is set up with Raspberry Pi OS and has the camera module enabled.
   - Install required libraries:
     ```bash
     pip install tensorflow opencv-python
     ```

2. **Clone the repository**:
   - Clone the project repository to your Raspberry Pi:
     ```bash
     git clone https://github.com/yourusername/smart-warehouse-management-system.git
     cd smart-warehouse-management-system
     ```

3. **Connect ESP32 and Weight Sensor**:
   - Connect the ESP32 to the Raspberry Pi and wire the HX711 weight sensor to the ESP32.

4. **Run the system**:
   - Start the synchronization process by running the `sync.py` script:
     ```bash
     python3 sync.py
     ```

5. **Monitor Outputs**:
   - The system will start reading weight data from the ESP32, capturing images, and making predictions about the items in the warehouse. The predicted labels and probabilities will be displayed in the terminal.

## Future Improvements

- **Scalability**: This system can be expanded to handle a larger number of items, providing detailed inventory management for diverse warehouse applications.
- **Data Logging**: Implement functionality to log data for tracking item quantities, predictions, and weight changes over time.
- **Web Interface**: Develop a simple web interface to visualize real-time data and manage warehouse items remotely.
- **Enhanced Classification Models**: Improve the machine learning model by training it with more diverse data to better classify different vegetable types and other warehouse items.

