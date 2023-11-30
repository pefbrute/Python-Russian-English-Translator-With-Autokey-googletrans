import pyperclip
import pyautogui
import time
from googletrans import Translator
import subprocess  # Used to open gedit
import tempfile  # Used to create a temporary file

translator = Translator()

def translate_to_english():
    pyautogui.hotkey('ctrl', 'c')  # Use 'command' instead of 'ctrl' on macOS
    
    time.sleep(0.1)  # Wait a bit for the clipboard to update with the selected text
    
    # Get the text from the clipboard
    input_text = pyperclip.paste()
    
    # Translate the text
    translated = translator.translate(input_text, dest='ru').text
    
    # Write the translated text to a temporary file and open it with gedit
    write_to_temp_file_and_open_with_gedit(translated)

def write_to_temp_file_and_open_with_gedit(translated_text):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as temp_file:
        temp_file.write(translated_text)
        temp_file_path = temp_file.name

    # Open the temporary file with gedit
    subprocess.Popen(['gedit', temp_file_path])

# Trigger the translation
translate_to_english()
