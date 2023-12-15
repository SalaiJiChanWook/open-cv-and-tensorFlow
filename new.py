import cv2
import pyttsx3

# Load the object detection model
model = cv2.dnn.readNet("object_detection_model.pb")

# Create a text-to-speech engine
engine = pyttsx3.init()

# Set the voice
engine.setProperty("voice", "english-us")

# Create a function to detect objects and speak their names
def detect_and_speak(frame):
  # Convert the frame to grayscale
  grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Detect objects in the frame
  objects = model.detectMultiScale(grayscale_frame, 1.3, 5)

  # Loop over the detected objects
  for object in objects:
    # Get the object's name
    object_name = object[0]

    # Speak the object's name
    engine.say(object_name)

# Create a video capture object
cap = cv2.VideoCapture(0)

while True:
  # Capture a frame
  frame = cap.read()[1]

  # Detect and speak the objects in the frame
  detect_and_speak(frame)

  # Display the frame
  cv2.imshow("Object Detection", frame)

  # Wait for a key press
  key = cv2.waitKey(1) & 0xFF

  # If the key is ESC, quit
  if key == 27:
    break

# Close the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
