#!/usr/bin/env python3

import rospy 
from std_msgs.msg import String
from gtts import gTTS
import os

def text_to_speech_callback(data):
    text = data.data
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

    os.system("mpg321 output.mp3")

if __name__ == '__main__':
    rospy.init_node('gTTS_node', anonymous=True)
    rospy.Subscriber("text_to_speech", String, text_to_speech_callback)
    rospy.spin()

