# StegoSeal

**StegoSeal** is a Python-based desktop application for secure message hiding using **LSB steganography** and a custom encryption algorithm. Built with a user-friendly Tkinter GUI, it allows users to encode secret messages into images and decode them securely with a 5-character key. Ideal for cybersecurity enthusiasts exploring steganography, secure communication, and GUI development.

## 🌟 Features
- **Dual-Panel GUI**: Intuitive interface with separate sections for encoding and decoding messages.
- **Secure Encoding**: Combines a custom encryption algorithm, base64 encoding, and LSB steganography to hide messages in images.
- **Decoding**: Retrieves hidden messages from encoded images using the correct 5-character key.
- **Input Validation**: Enforces 5-character keys and message length limits with user-friendly error messages.
- **Cross-Platform**: Runs on Windows, macOS, and Linux with a non-resizable 600x600 window.
- **Output Management**: Saves encoded images as PNG files in a designated directory (`encoded_images`).

## 🛠️ Technologies Used
- **Python 3.x**: Core programming language.
- **Tkinter**: For the GUI framework.
- **Stegano**: For LSB steganography implementation.
- **Base64**: For message encoding before steganography.
- **OS & Pathlib**: For file and directory management.

## 📋 Prerequisites
- Python 3.6 or higher
- Required Python libraries: `stegano`, `pillow` (for image processing)

## 🚀 Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Nal19/StegoSeal.git
   cd StegoSeal
2. **Install Dependencies**:
   ```bash
   pip install stegano pillow
3. **Verify Python Installation: Ensure Python 3.x is installed by running**:
   ```bash
   python --version

## 🖥️ Usage
1. **Run the application**:
   ```bashbash
   python stegoseal.py
2. **Encode a Message**:
   In the "Encode" panel, enter a message and a 5-character key.
   Select an input image (e.g., PNG or JPEG).
   Click "Encode" to hide the message and save the output as a PNG in the encoded_images directory.
3. **Decode a Message**:
   In the "Decode" panel, select an encoded image.
   Enter the 5-character key used during encoding.
   Click "Decode" to retrieve and display the hidden message.
4. **Error Handling**:
   Invalid keys or message lengths trigger clear error messages.
   Missing files or incorrect keys result in appropriate alerts.
**Example**:
   Encode: Input message "Hello, World!" with key "abcde" into image.png. Output saved as encoded_images/encoded_image.png.
   Decode: Upload encoded_image.png, enter key "abcde", and retrieve "Hello, World!".
   
## 📝 Example Interface
   [StegoSeal GUI - 600x600 Window]
   [Encode Panel]                   [Decode Panel]
   Message: [____________]          Image: [Browse...]
   Key: [_____]                    Key: [_____]
   Image: [Browse...]              [Decode Button]
   [Encode Button]

## 🛡️ Limitations
   Only supports PNG and JPEG input images (PNG output recommended for lossless steganography).
   Key must be exactly 5 characters; longer messages may be truncated based on image capacity.
   Not suitable for large-scale data hiding due to steganography constraints.

## 🔮 Future Improvements
   Add support for stronger encryption algorithms (e.g., AES).
   Implement batch processing for multiple images.
   Enhance GUI with themes or resizable windows.
   Add exportable logs for encoding/decoding operations.

## 🤝 Contributing
   Contributions are welcome! You can:
     Report bugs or suggest features via Issues.
     Fork the repo, make improvements, and submit a pull request.
     Ideas: Add new encryption methods, improve GUI responsiveness, or support additional image formats.

## 📫 Contact
   Author: Nal (@Nal19)
   Email: nalthehcaker@gmail.com
   GitHub: Nal19
