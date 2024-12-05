# Pose Estimation and Landmark Processing

![Landmarks detection with MediaPipe and OpenCV](https://github.com/ivancabrilo/PoseEstimationProject/blob/main/readme.gif?raw=true)

This project demonstrates how to use **MediaPipe's Pose module** with **OpenCV** to process pose landmarks and analyze overreliance on certain limbs or joints during climbing. It processes video frames, detects body landmarks, excludes specific landmarks (e.g., face landmarks), computes averages over frames, and saves the data in a JSON file.

---

## Features

- **Pose Detection**: Detect body pose landmarks using MediaPipe.
- **Landmark Filtering**: Exclude low-visibility landmarks and specific unwanted landmarks (e.g., face landmarks).
- **Frame Skipping**: Process every Nth frame for efficiency.
- **Landmark Averaging**: Smooth landmark positions by averaging data over multiple frames.
- **FPS Display**: Show real-time frame processing speed (FPS) on video.
- **JSON Export**: Save processed landmarks into a structured JSON file for further analysis.

---

## Body Landmark IDs

The following numbers represent IDs for each part of the body, as defined in `pose.py` (MediaPipe library):

| Landmark Name         | ID  | Landmark Name         | ID  |
|-----------------------|------|-----------------------|------|
| NOSE                  | 0    | LEFT_HIP             | 23   |
| LEFT_EYE_INNER        | 1    | RIGHT_HIP            | 24   |
| LEFT_EYE              | 2    | LEFT_KNEE            | 25   |
| LEFT_EYE_OUTER        | 3    | RIGHT_KNEE           | 26   |
| RIGHT_EYE_INNER       | 4    | LEFT_ANKLE           | 27   |
| RIGHT_EYE             | 5    | RIGHT_ANKLE          | 28   |
| RIGHT_EYE_OUTER       | 6    | LEFT_HEEL            | 29   |
| LEFT_EAR              | 7    | RIGHT_HEEL           | 30   |
| RIGHT_EAR             | 8    | LEFT_FOOT_INDEX      | 31   |
| MOUTH_LEFT            | 9    | RIGHT_FOOT_INDEX     | 32   |
| MOUTH_RIGHT           | 10   |                     

> **Note:** Some landmarks, such as the hands, are averaged to account for missing or low-visibility data. Example:
> 
> ```json
> {
>   "id": 15,
>   "x": 0.2337,
>   "y": 0.9412,
>   "z": -0.1070,
>   "visibility": 0.6834
> },
> {
>   "id": 19,
>   "x": 0.2442,
>   "y": 0.9607,
>   "z": -0.1970,
>   "visibility": 0.6510
> }
> ```

---

## Prerequisites

### Required Libraries

Ensure you have the following Python libraries installed:

- **OpenCV**: For video processing
- **MediaPipe**: For pose estimation
- **JSON**: For data serialization

Install them using pip:
```bash
pip install opencv-python mediapipe
```

---

## Configuration

### Frame Skipping
Adjust `frame_skip` to process every Nth frame (default: 2):
```python
frame_skip = 2
```

### Excluded Landmarks
Update `excluded_landmarks` to filter out unwanted pose landmarks (default: face landmarks, indices 0–10):
```python
excluded_landmarks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

## How It Works

1. **Pose Detection**: Detects pose landmarks in each video frame using MediaPipe.
2. **Filtering**: Excludes landmarks below a visibility threshold (e.g., `visibility < 0.65`).
3. **Landmark Averaging**: Computes averages for missing or low-visibility landmarks (e.g., hands).
4. **JSON Export**: Saves processed pose landmarks into a JSON file for analysis.

---

## Currently working on calculating overrealiance on specific joints/limbs

## Contributing

Contributions are welcome! If you have suggestions for improving this project, feel free to fork the repository and submit a pull request.

---

