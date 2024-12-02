# import cv2

# import mediapipe as mp
# import time
# cap = cv2.VideoCapture("PoseVideos/IMG_7578.mp4")
# pTime = 0
# cTime = 0
# mpPose = mp.solutions.pose
# pose = mpPose.Pose()
# mpDraw = mp.solutions.drawing_utils
# while True:
#     success, img = cap.read()

#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = pose.process(imgRGB)

#     if results.pose_landmarks:
#         mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

#     cTime = time.time()
#     fps = 1/(cTime- pTime)
#     pTime = cTime

#     cv2.putText(img,str(int(fps)),(70,50), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
#     cv2.imshow('Image', img)
#     cv2.waitKey(1) # 20 


# import cv2
# import mediapipe as mp
# import time
# import json

# cap = cv2.VideoCapture('PoseVideos/VIDEO-2024-12-01-13-20-42.mp4')

# pTime = 0

# data = []
# mpPose = mp.solutions.pose
# pose = mpPose.Pose()
# # mpDraw = mp.solutions.drawing_utils
# frame_count = 0
# # Specify landmarks to exclude (e.g., face landmarks with indices 0–10)
# excluded_landmarks = list(range(0, 11))  # Indices for face-related landmarks

# while True:
#     success, img = cap.read()
#     if not success:
#         break

#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = pose.process(imgRGB)

#     if results.pose_landmarks:
#         # Get the image dimensions
#         h, w, c = img.shape
#         frame_data = {
#             "frame": frame_count,
#             "landmarks": []
#         }

#         # Draw each landmark manually
#         for id, lm in enumerate(results.pose_landmarks.landmark):
#             if id not in excluded_landmarks:  # Only draw non-face landmarks
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
#                 landmark_data = {
#                     "id": id,  # ID comes from enumerate
#                     "x": lm.x,
#                     "y": lm.y,
#                     "z": lm.z,
#                     "visibility": lm.visibility
#                 }
#                 frame_data["landmarks"].append(landmark_data)

    
                
#                 # print(id,results.pose_landmarks)
#             data.append(frame_data)
#         frame_count += 1
#         # Draw only non-excluded connections
#         for connection in mpPose.POSE_CONNECTIONS:
#             if connection[0] not in excluded_landmarks and connection[1] not in excluded_landmarks:
#                 start = results.pose_landmarks.landmark[connection[0]]
#                 end = results.pose_landmarks.landmark[connection[1]]
#                 start_x, start_y = int(start.x * w), int(start.y * h)
#                 end_x, end_y = int(end.x * w), int(end.y * h)
#                 cv2.line(img, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

#     cTime = time.time()
#     fps = 1 / (cTime - pTime)
#     pTime = cTime
#     with open('pose_landmarks.json', 'w') as f:
#         json.dump(data, f, indent=4)

#     cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
#     cv2.imshow('Image', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# import cv2
# import mediapipe as mp
# import time
# import json

# # Initialize video capture and pose detection
# cap = cv2.VideoCapture('PoseVideos/climb0.mp4')

# pTime = 0
# data = []
# mpPose = mp.solutions.pose
# pose = mpPose.Pose()

# frame_count = 0
# frame_skip = 2  # Process every 2nd frame

# buffer = []
# buffer_size = 10  # Average every 5 frames
# # List of landmarks to exclude
# excluded_landmarks = list(range(0, 11))  # Exclude face landmarks

# while True:
#     success, img = cap.read()
#     if not success:
#         break

#     # Skip frames to speed up processing
#     if frame_count % frame_skip != 0:
#         frame_count += 1
#         continue

#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = pose.process(imgRGB)

#     if results.pose_landmarks:
#         h, w, c = img.shape
#         frame_data = {
#             "frame": frame_count,
#             "landmarks": []
#         }

#         for id, lm in enumerate(results.pose_landmarks.landmark):
#             if id not in excluded_landmarks:  # Only draw non-face landmarks
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
#                 if lm.visibility > .65:
#                     landmark_data = {
#                         "id": id,
#                         "x": lm.x,
#                         "y": lm.y,
#                         "z": lm.z,
#                         "visibility": lm.visibility
#                     }
#                     frame_data["landmarks"].append(landmark_data)

#         data.append(frame_data)

#         for connection in mpPose.POSE_CONNECTIONS:
#             if connection[0] not in excluded_landmarks and connection[1] not in excluded_landmarks:
#                 start = results.pose_landmarks.landmark[connection[0]]
#                 end = results.pose_landmarks.landmark[connection[1]]
#                 start_x, start_y = int(start.x * w), int(start.y * h)
#                 end_x, end_y = int(end.x * w), int(end.y * h)
#                 cv2.line(img, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

#     cTime = time.time()
#     fps = 1 / (cTime - pTime)
#     pTime = cTime

#     cv2.putText(img, f"FPS: {int(fps)}", (70, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
#     cv2.imshow('Image', img)

#     delay = max(1, int(1000 / 90))  # Simulate 90 FPS playback
#     if cv2.waitKey(delay) & 0xFF == ord('q'):
#         break

#     frame_count += 1

# # Write JSON data after processing all frames
# with open('pose_landmarks1.json', 'w') as f:
#     json.dump(data, f, indent=4)

# cap.release()
# cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import time
import json

# Initialize video capture and pose detection
cap = cv2.VideoCapture('PoseVideos/climb0.mp4')

pTime = 0
data = []
mpPose = mp.solutions.pose
pose = mpPose.Pose()

frame_count = 0
frame_skip = 2  # Process every 2nd frame

# Buffer for averaging
buffer = []
buffer_size = 10  # Average every 5 frames

# List of landmarks to exclude
excluded_landmarks = list(range(0, 11))  # Exclude face landmarks

while True:
    success, img = cap.read()
    if not success:
        break

    # Skip frames to speed up processing
    if frame_count % frame_skip != 0:
        frame_count += 1
        continue

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        h, w, c = img.shape
        frame_data = {
            "frame": frame_count,
            "landmarks": []
        }

        for id, lm in enumerate(results.pose_landmarks.landmark):
            if id not in excluded_landmarks and lm.visibility > 0.65:  # Exclude low-visibility landmarks
                landmark_data = {
                    "id": id,
                    "x": lm.x,
                    "y": lm.y,
                    "z": lm.z,
                    "visibility": lm.visibility
                }
                frame_data["landmarks"].append(landmark_data)

        # Add frame data to buffer
        buffer.append(frame_data)

        # If buffer is full, compute the average
        if len(buffer) == buffer_size:
            # Initialize averaged frame
            averaged_frame = {
                "frame": buffer[0]["frame"],  # Use the first frame's ID
                "landmarks": []
            }

            # Get all landmark IDs present in the buffer
            all_landmark_ids = set(
                lm["id"] for frame in buffer for lm in frame["landmarks"]
            )

            # Average the data for each landmark ID
            for landmark_id in all_landmark_ids:
                x_sum, y_sum, z_sum, visibility_sum, count = 0, 0, 0, 0, 0

                for frame in buffer:
                    for lm in frame["landmarks"]:
                        if lm["id"] == landmark_id:
                            x_sum += lm["x"]
                            y_sum += lm["y"]
                            z_sum += lm["z"]
                            visibility_sum += lm["visibility"]
                            count += 1

                # Append averaged landmark data
                if count > 0:
                    averaged_frame["landmarks"].append({
                        "id": landmark_id,
                        "x": x_sum / count,
                        "y": y_sum / count,
                        "z": z_sum / count,
                        "visibility": visibility_sum / count
                    })

            # Append averaged frame to the final data
            data.append(averaged_frame)

            # Clear the buffer
            buffer = []

    frame_count += 1

    # Display FPS and video
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (70, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow('Image', img)

    delay = max(1, int(1000 / 90))  # Simulate 90 FPS playback
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# Write JSON data after processing all frames
with open('pose_landmarks_averaged.json', 'w') as f:
    json.dump(data, f, indent=4)

cap.release()
cv2.destroyAllWindows()


# here average the hands
# then in separte script make this part that reduces the number of frames of data, basically takes in json, returns a shorter json