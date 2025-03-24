import os
from googletrans import Translator

# Initialize the translator
translator = Translator()

def translate_text(text, src_lang='en', dest_lang='es'):
    """ Translate text from src_lang to dest_lang """
    try:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text

def translate_file(input_file, output_file, src_lang='en', dest_lang='es'):
    """ Read, translate content and write to output file """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Translate content
        translated_content = translate_text(content, src_lang, dest_lang)

        # Save the translated content to a new file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translated_content)
        
        print(f"Translated file saved: {output_file}")
    except Exception as e:
        print(f"Error processing file {input_file}: {e}")

def translate_folder(input_folder, output_folder, src_lang, dest_lang):
    """ Translate all .md files in the input folder and save to output folder """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        # Create the corresponding directory in the output folder
        relative_path = os.path.relpath(root, input_folder)
        output_root = os.path.join(output_folder, relative_path)
        if not os.path.exists(output_root):
            os.makedirs(output_root)

        for file in files:
            if file.endswith('.md'):
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_root, file)
                translate_file(input_file, output_file, src_lang, dest_lang)

if __name__ == "__main__":
    # Define the input and output folder paths
    input_folder = "./en"  # Replace with your input folder path
    es_output_folder = "./es"  # Replace with your desired output folder path
    he_output_folder = "./he"
    translate_folder(input_folder, es_output_folder, src_lang='en', dest_lang='es')
    translate_folder(input_folder, he_output_folder, src_lang='en', dest_lang='he')
