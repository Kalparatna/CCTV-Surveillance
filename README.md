
# CCTV SURVILLIENCE  ACIDENT DETECTION SYSTEM

## Project Description

Accident Detection System is a computer vision-based solution designed to automatically detect accidents in a video stream or file. The system utilizes the AccidentDetectionModel from the `detection` module, providing a reliable method for identifying accidents in real-time.

## Table of Contents
- [Overview](#overview)
- [Dependencies](#dependencies)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Overview

Accidents on the road can have severe consequences, and timely response is crucial for minimizing the impact.
This project aims to enhance road safety by leveraging computer vision techniques to detect accidents.
The script processes video frames, predicts whether an accident has occurred, and triggers an email alert in case of a significant event.

## Dependencies

Ensure the required dependencies are installed before running the script:

```bash
pip install opencv-python smtplib
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your_username/accident-detection-system.git
cd accident-detection-system
```

2. Download the model files (`model.json` and `model_weights.h5`) and place them in the project directory.

3. Open the script and configure the following variables:

   - `sender_email`: The Gmail account used to send the email alerts.
   - `sender_password`: The password for the sender's Gmail account.
   - `receiver_email`: The email address to receive the accident alerts.

## Usage

Run the script using the following command:

```bash
python accident_detection.py
```

By default, the script uses a video file (`cars5.mp4`). To use a webcam as the video source, set `use_webcam` to `True` in the script.

```python
use_webcam = True
startapplication(use_webcam)
```

Press 'q' to exit the video stream.

## Configuration

Ensure the following configurations are set correctly in the script:

- `url`: If using a webcam, replace it with the URL from the IP Webcam app.
- `video`: If using a local video file, set the file path.

## License

This project is licensed under the [MIT License](LICENSE).
```

Feel free to adjust the project description and other sections to provide more specific details about your Accident Detection System.
