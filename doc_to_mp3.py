#      .-.                                         .----.
#      : :              .-   .-                    `--  ;
#    .-' : .--.  .--.   `.`. `.`.   ,-.,-.,-..---.  .' ' 
#   ' .; :' .; :'  ..'   ,',' ,','  : ,. ,. :: .; ` _`,`.
#   `.__.'`.__.'`.__.'  :_,  :_,    :_;:_;:_;: ._.'`.__.'
#                                            : :         
#                                            :_;          

"""
doc-to-mp3: A script to convert text from documents (txt, pdf, docx) into MP3 audio files.
Author: maxy618
Version: 1.0
"""

import argparse
import os
from pathlib import Path

import fitz  # PyMuPDF
from docx import Document
from pyfiglet import figlet_format
from gtts import gTTS
from gtts.lang import tts_langs
from termcolor import colored


SUPPORTED_TYPES = ('txt', 'pdf', 'docx')

success = colored('[+] SUCCESS', color='green', attrs=['bold'])
error = colored('[-] ERROR', color='red', attrs=['bold'])


def prepare_console(logo_text: str, logo_font: str, logo_color: str) -> None:
    """
    Clear the console and display the application logo.

    Args:
        logo_text (str): The text to display as the logo.
        logo_font (str): The font style for the logo text.
        logo_color (str): The color of the logo text.
    """
    os.system('cls' if os.name == 'nt' else 'clear')    

    logo = figlet_format(text=logo_text, font=logo_font)
    print(
        colored(
            logo,
            color=logo_color,
            attrs=['bold']
        )
    )


def validate_file(file_path: str, supported_types: list[str]) -> str:
    """
    Validate the file path and ensure the file type is supported.

    Args:
        file_path (str): The path to the file to validate.
        supported_types (list): A list of supported file extensions.

    Returns:
        str: The file type if valid, or None if invalid.
    """
    if not Path(file_path).exists():
        print(f'{error}: File does not exist')
        return
    
    document_type = Path(file_path).suffix[1:].lower()
    if document_type not in supported_types:
        print(f'{error}: Unsupported file type: {document_type}')
        return
    
    print(f'{success} Selected path: {file_path}')
    return document_type


def extract_text(file_path: str, document_type: str) -> str:
    """
    Extract text from the specified file based on its type.

    Args:
        file_path (str): The path to the file to extract text from.
        document_type (str): The type of the document (e.g., txt, pdf, docx).

    Returns:
        str: The extracted text.
    """
    text = ''
    print(f'{success} Fetching text from: {document_type}')
    try:
        if document_type == 'txt':
            with open(file_path, 'r', encoding='utf-8') as txt_file:
                text = txt_file.read().replace('\n', ' ')
        elif document_type == 'pdf':
            pdf_file = fitz.open(file_path)
            for page in pdf_file:
                text += page.get_text().replace('\n', ' ')
        elif document_type == 'docx':
            doc = Document(file_path)
            text = ' '.join([p.text for p in doc.paragraphs])
    except Exception as e:
        print(f'{error}: Failed to extract text: {e}')
    return text


def convert_to_mp3(text: str, language: str, output_file: str = 'result.mp3'):
    """
    Convert the given text to an MP3 audio file using the specified language.

    Args:
        text (str): The text to convert to audio.
        language (str): The language code for text-to-speech.
        output_file (str, optional): The name of the output MP3 file. Defaults to 'result.mp3'.
    """
    supported_languages = tts_langs()
    if language not in supported_languages:
        print(f'{error} This language is not supported')
        return
    if Path(output_file).exists():
        os.remove(output_file)
    if not output_file.endswith('.mp3'):
        output_file += '.mp3'

    audio = gTTS(text=text, lang=language)
    audio.save(output_file)
    print(f'{success} Audio "{output_file}" has been saved')


def main(file_path: str, language: str) -> None:
    prepare_console(
        logo_text='doc >> mp3',
        logo_font='fuzzy',
        logo_color='light_cyan'
        )

    document_type = validate_file(file_path, SUPPORTED_TYPES)
    if not document_type:
        return

    text = extract_text(file_path, document_type)
    if not text.strip():
        print(f'{error}: File is empty or contains no readable text')
        return
    print(f'{success} Text fetched successfully. Length: {len(text)} symbols')

    print(f'{success} Conversion started')
    convert_to_mp3(text, language, args.name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert text from a document file to an MP3 audio file.")

    parser.add_argument('--file', type=str, required=True, help='Path to the input file. Supported formats: txt, pdf, docx.')
    parser.add_argument('--lang', type=str, required=True, help='Language code for text-to-speech (e.g., en for English, ru for Russian).')
    parser.add_argument('--name', type=str, default='result.mp3', help='Name of the output MP3 file (default: result.mp3, .mp3 extension will be added if missing).')

    args = parser.parse_args()
    main(args.file, args.lang)