# Color-Detection-Application

## Description
This application allows users to upload images and detect the most dominant color present in the image. It utilizes KMeans clustering to analyze the image and identify the color that appears most frequently.

## Features
- User-friendly GUI built with Tkinter.
- Upload images in JPG, PNG, or JPEG formats.
- Displays the uploaded image and the detected dominant color.
- Real-time color detection using KMeans clustering.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dominant-color-detection.git
   ```
2. Navigate to the project directory:
   ```bash
    cd dominant-color-detection
   ```
3. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
   ```
## Usage
1. Run the application:
  ```bash
      python main.py
  ````
2. Click on the "Upload Image" button to select an image file.
3. The application will display the uploaded image and the detected dominant color.

## Implementation
The application is structured as follows:

* main.py: Initializes the Tkinter GUI and runs the application.
* ui.py: Contains the user interface logic, including image upload and color detection.
* color_detector.py: Implements the color detection logic using KMeans clustering.
