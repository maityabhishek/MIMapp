"""performs continuous speech recognition with input from an audio file"""
# <SpeechContinuousRecognitionWithFile>
import azure.cognitiveservices.speech as speechsdk
import time
filename = "azure_recording.wav"
speech_key, service_region = "f0262d94aa2e4f378d2d65d34fbfefb1", "centralindia"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.audio.AudioConfig(filename=filename)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

done = False
text = ''
def stop_cb(evt):
    """callback that signals to stop continuous recognition upon receiving an event `evt`"""
    print('CLOSING on {}'.format(evt))
    global done
    done = True

all_results = []
def handle_final_result(evt):
    all_results.append(evt.result.text)

speech_recognizer.recognized.connect(handle_final_result)
# Connect callbacks to the events fired by the speech recognizer
speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
# stop continuous recognition on either session stopped or canceled events
speech_recognizer.session_stopped.connect(stop_cb)
speech_recognizer.canceled.connect(stop_cb)

# Start continuous speech recognition
speech_recognizer.start_continuous_recognition()
while not done:
    time.sleep(.5)

speech_recognizer.stop_continuous_recognition()
print("Printing all results:")
print(all_results)
# </SpeechContinuousRecognitionWithFile>