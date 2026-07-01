import cv2
from ultralytics import YOLO

# 1. Load the pre-trained YOLOv8 model
model = YOLO('yolov8n.pt') 

# 2. Open the downloaded video source
input_path = 'sample_input.mp4'
cap = cv2.VideoCapture(input_path)

# Get video properties for the output file writer
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 3. Initialize Video Writer to save the output file
output_path = 'output_processed.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

print("Processing video frames... Please wait.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # 4. Run inference (Classes: 0=person, 2=car, 67=cell phone)
    results = model(frame, classes=[0, 2, 67], verbose=False) 

    # 5. Extract the frame containing drawn bounding boxes
    annotated_frame = results[0].plot()

    # 6. Write the annotated frame to the output file
    out.write(annotated_frame)

# Clean up resources
cap.release()
out.release()
print(f"Processing complete! Saved to: {output_path}")
