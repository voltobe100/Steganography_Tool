# Steganography Tool – Hide Text Inside Images using PIL and LSB

## Overview

This Python-based steganography tool allows users to hide secret text messages inside images using the Least Significant Bit (LSB) technique. It provides an easy way to encode and decode messages within image files without noticeable changes in image quality.

## Features

- Hide a secret text message inside an image.
- Retrieve hidden text from a modified image.
- Supports PNG format for lossless encoding.
- Simple CLI interface for encoding and decoding.

## Installation

Ensure Python is installed, then install the required dependencies:

```bash
pip install pillow
```

## Usage

### Encoding a Message

To hide a message inside an image:

```bash
python steganography.py --encode --image input.png --message "Secret Message" --output output.png
```

### Decoding a Message

To retrieve a hidden message from an image:

```bash
python steganography.py --decode --image output.png
```

## Example Output

```bash
[+] Encoding message into image...
[+] Successfully saved encoded image as output.png

[+] Decoding hidden message...
[+] Hidden message: "Secret Message"
```

## Limitations

- Works best with PNG images to avoid quality loss.
- Message size is limited by the number of pixels in the image.

## Legal Disclaimer

This tool is intended for ethical and legal use only. The creator is not responsible for any misuse.
