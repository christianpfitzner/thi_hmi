#!/usr/bin/env python3

import os
import datetime

import rospy

from std_msgs.msg import String

from speech_recognition_msgs.msg import SpeechRecognitionCandidates

import pyttsx3

import numpy as np 

arr = np.array([('hello',       'I say Hello 1',            'beep'), 
                ('hello you',   'I say Hello 2',            'beep'), 
                ('How are you', 'Fine, thanks for asking',  'beep'), 
                ('go to sleep', 'shutting down',            'beep')],
       dtype=[('input',   (np.str_, 100)), 
               ('say',    (np.str_, 100)), 
               ('action', (np.str_, 100))]) 


def handle_output(msg):
    """Map out grammar recognized commands in speech to terminal commands"""


    data = msg.transcript[0]; 

    for x in arr: 

        engine = pyttsx3.init()
        # engine.startLoop()
        engine.setProperty('voice', 'english+f3')
        engine.setProperty('speed', '70')
        if(data.lower() == x[0].lower()):
            engine.say(x[1])
            engine.runAndWait()
        if(data.lower() == 'go to sleep'):
            exit()


        
    print(data)


    if "go to my workspace" in data.lower():
        engine = pyttsx3.init()
        engine.setProperty('voice', 'english+f3')
        engine.setProperty('speed', '70')

        engine.say("Right away, master!")
        engine.runAndWait()
        os.system("nautilus --browser /home/pankaj/catkin_ws/src/pocketsphinx")
    elif "where is avenger base" in data.lower():
        engine = pyttsx3.init()
        engine.setProperty('voice', 'english+f3')
        engine.say('I am sorry! That is classified information')
        engine.runAndWait()
    elif "what time is it" in data.lower():
        message = 'It is ' + datetime.datetime.now().strftime("%H:%M") + ' hours'
        print (message)
        engine = pyttsx3.init()
        engine.setProperty('speed', '70')
        engine.setProperty('voice', 'english+f3')
        engine.say(message)
        engine.runAndWait()
    elif "goodnight jarvis" in data.lower():
        message = 'good night, master!'
        engine = pyttsx3.init()
        engine.setProperty('voice', 'english+f3')
        engine.say(message)
        engine.runAndWait()

def shutdown():
    """This function is executed on node shutdown."""
    # command executed after Ctrl+C is pressed
    rospy.loginfo("Stop ASRControl")
    rospy.sleep(1)

def init():
    """Initialize node and subscribe to necessary topics"""

    # initialize node
    rospy.init_node("command_control")

    # Call custom function on node shutdown
    rospy.on_shutdown(shutdown)

    rospy.Subscriber("Tablet/voice", SpeechRecognitionCandidates, handle_output)
    rospy.spin()



if __name__ == "__main__":
    init()
