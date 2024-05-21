# Hand Gesture Volume Control

## Description

Control your computer's volume with simple hand gestures! This project uses [OpenCV](https://opencv.org/) for real-time image processing and hand detection, [MediaPipe](https://developers.google.com/mediapipe) for robust hand landmark tracking, and [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) to simulate volume control actions based on hand movements.

## Getting Started

### Prerequisites
Ensure you have Python installed on your system. You can download it from Python's [official website](https://www.python.org/).

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AdityaKotkar47/hand-gesture-volume-control
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd hand-gesture-volume-control
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv volume_control_env
   ```
4. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate.bat
     ```

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
5. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. **Run this script**:
   ```bash
   python main.py
   ```
2. **Control Volume**:

   * **Raise your hand with palm facing the camera**: Increase volume.
   * **Lower your hand with palm facing the camera**: Decrease volume.
3. **Exit the Program**:
3. **Exit the Program:**
   * Press the 'Esc' key to close the camera window and stop volume control.
   * Alternatively, you can terminate the terminal to stop the script (Ctrl+C or Cmd+C).

