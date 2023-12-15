import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox #Object Dtetection project
from gtts import gTTS
from playsound import playsound
import speech_recognition
import pyttsx3
#from googletrans import Translator

def speech(text):
    print(text)
    # translator = Translator()
    # # txt_translated = translator.translate(text, dest='en').text1
    # final_translated = translator.translate(text, dest='my').text1 
    language = "en"
    out_put = gTTS(text=text, lang=language, slow=False)
    out_put.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")

video = cv2.VideoCapture(0)
labels = []

while True:
    ret, frame = video.read()
    bbox, label, conf = cv.detect_gender(frame)
    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("My second object detection", output_image)

    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

i = 0
j = 0
new_sentence = []
for label in labels:
    if i == 0:
        new_sentence.append(f"hello sir, I found a {label}, and")

    else:
        new_sentence.append(f"the {label} ,and ")
        
        
        if j != 0 :
                
            
                if label in ["knife", "scissors", "bottle"]:
                   new_sentence.append(f"please put it down your {label}, it is so dangerous.")
                
            #  if i == len(new_sentence)  :
             
            #      new_sentence.append(f"a {label} , on my screen;")

            #      if "scissors" in label or "knife" in label:
            #         new_sentence.append(f"please put it down your {label}, it is so dangerous.")
                 

                 

                else:
                     continue
                    
        
            
               
    i+=1
    j+=1
speech(" ".join(new_sentence))

#Speech recongnition

# recognizer = speech_recognition.Recognizer()

# while True:

#     try:

#         with speech_recognition.Microphone() as mic:
            
#             recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#             audio = recognizer.listen(mic)

#             text1 = recognizer.recognize_google(audio)
#             text1 = text1.lower()

#             print(f"you said: {text1}")

#     except speech_recognition.UnknownValueError():

#         recognizer = speech_recognition.Recognizer()
#         continue

#     if  text1 == "hello friday":
#          athan = "hello, sir friday is ready"
#          sound = gTTS(athan, lang="en")
#          sound.save("welcome.mp3")
#          playsound("welcome.mp3")

#     else:
#         speech(" ".join(new_sentence))