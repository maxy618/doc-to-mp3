
---

# DOC to MP3 Converter 🎧

*doc_to_mp3.py* is a Python script that converts text from `.txt`, `.pdf`, or `.docx` files into an MP3 audio file using Google Text-to-Speech (gTTS).

```
      .-.                                         .----.
      : :              .-   .-                    `--  ;
    .-' : .--.  .--.   `.`. `.`.   ,-.,-.,-..---.  .' ' 
   ' .; :' .; :'  ..'   ,',' ,','  : ,. ,. :: .; ` _`,`.
   `.__.'`.__.'`.__.'  :_,  :_,    :_;:_;:_;: ._.'`.__.'
                                            : :         
                                            :_;         
```

## ✨ Features

- Extracts text from `.txt`, `.pdf`, and `.docx` files.  
- Converts extracted text into an MP3 audio file.  
- Supports multiple languages for text-to-speech conversion.  
- Customizable output file name.  
- Supports processing multiple files concurrently using threads.  
- Avoids overwriting existing files, prompting the user before overwriting.  

---

## 📋 Requirements

- **Python**: Version 3.8 or higher  
- **Dependencies**: Installed via `requirements.txt`  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maxy618/doc-to-mp3.git
   cd doc-to-mp3
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

Run the script from the command line:  
```bash
python doc_to_mp3.py --files <file_paths> --lang <language_code>
```

### **Arguments**
- `--files` (required): Paths to the input files (absolute or relative). Multiple files can be processed by providing space-separated paths.  
- `--lang` (required): Language code for text-to-speech (e.g., `en` for English, `ru` for Russian).    

### **Example**
Convert a `.pdf` file to an MP3 in English and save as `.mp3`:
```bash
python doc_to_mp3.py --files document.pdf --lang en
```

Convert multiple files at once:
```bash
python doc_to_mp3.py --files document.pdf document.docx --lang en
```

---

## 🌍 Supported Languages

The script supports all languages provided by Google Text-to-Speech (gTTS).  
For the full list of available languages and their codes, refer to the [gTTS documentation](https://gtts.readthedocs.io/en/latest/module.html#languages).  

Some common examples:
- English: `en`  
- Russian: `ru`  
- Spanish: `es`  
- French: `fr`  

---

## 🛠 Troubleshooting

If you encounter issues, ensure that:
1. The input file exists and is accessible.  
2. The file format is one of the supported types (`.txt`, `.pdf`, `.docx`).  
3. The language code is valid and supported by gTTS.  
4. Ensure there are no conflicts with file names if processing multiple files simultaneously.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.  

---

## 🤝 Contributing

Contributions are always welcome! Feel free to:  
- Open an issue to report bugs or request features.  
- Submit a pull request with your improvements.  

---

## 💡 Tips

- The script uses threading to process multiple files concurrently. This improves performance but be mindful of system resources.  
- You can customize the ASCII art logo in the `prepare_console` function.  
- If your document contains sensitive text, ensure it is secure before sharing the generated audio file.  

---
