# TODO#1 - Import the necessary libraries
from TTS.api import TTS
import os
# TODO#2: Load the TTS model
model_name = TTS.list_models()[0]
tts = TTS(model_name)
# TODO#3 - Select the speaker and language
selected_speaker = tts.speakers[0]
selected_language = tts.languages[0]
# TODO#4 - Set output folder and input text
os.makedirs('output', exist_ok=True)
text = (
    "First, solve the problem. Then write the code. Step 5 Extending Your Knowledge, "
    "Now that you’ve created a basic TTS script, try experimenting with different parameters:\n\n"
    "Change the Text: Modify the text variable to test how the TTS model handles various sentences.\n"
    "Select a Different Speaker: Adjust the selected_speaker variable to use other speakers available in the model by replacing 0 with other index numbers.\n"
    "Change the Language: Modify the selected_language to explore how localization affects the output.\n"
    "Vary Output File Names: Set different file_path values to save outputs with different names."
)
# TODO#5 Generate the speech and save it to a WAV file
tts.tts_to_file(
    text=text,
    speaker=selected_speaker,
    language=selected_language,
    file_path="output/output/output.wav"
)
print("TTS complete! Check the output folder for the audio file.")