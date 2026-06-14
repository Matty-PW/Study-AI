# Study-AI
A python app that uses AI to detect when you pick up your phone while revising and alerts you to put it down.

# Features
- Live webcam feed displayed in the app
- Real time AI phone detection using YOLO26
- Red box drawn around detected phone
- Alarm sound that plays when phone is detected
- Popup windows telling you to lock in
- Activate / Deactivate button

# How it works
1. Press the activate button to start the AI
2. The app opens your webcam and displays a live feed
3. Every frame is analysed by a YOLO26 AI model looking for a phone
4. If a phone is detected:
   - A red box is drawn around it on the live feed
   - An alarm sound plays
   - Popup windows appear telling you to put it down
5. When you put the phone down everything stops automatically
6. Press deactivate to turn the AI off

# Requirements
- Python 3.10 or higher
- A webcam
- The following libraries (installed via requirements.txt):
  - Pillow
  - OpenCV
  - Ultralytics
  - playsound3
  
# Installation
1. Clone the repository:
   - git clone https://github.com/Matty-PW/Study-AI

2. Navigate to the project folder:
   - cd Study-AI

3. Install the required libraries:
   - pip install -r requirements.txt

4. Run the app:
   - python study_ai.py

Note: Python 3.10 or higher is required

Note: The YOLO model will download automatically the first time you run the app

# Credits
BS Fire Alarm (Sweeping - 1 Hz) by AdamWeeden -- https://freesound.org/s/255181/ -- License: Attribution 3.0
