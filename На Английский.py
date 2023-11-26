import pyperclip
import pyautogui
import time
from googletrans import Translator

translator = Translator()

def translate_to_russian():
    pyautogui.hotkey('ctrl', 'c')  # Use 'command' instead of 'ctrl' on macOS
    
    time.sleep(0.1)  # Wait a bit for the clipboard to update with the selected text
    
    # Get the text from the clipboard
    input_text = pyperclip.paste()
    
    translated = translator.translate(input_text, dest = 'en').text
    
    pyperclip.copy(translated)
    
    pyautogui.hotkey('ctrl', 'v')

translate_to_russian()
