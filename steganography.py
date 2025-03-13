from PIL import Image
import argparse


def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'
    
    if len(binary_message) > len(pixels) * 3:
        raise ValueError("Message is too large for the given image.")
    
    new_pixels = []
    binary_index = 0
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):
            if binary_index < len(binary_message):
                new_pixel[i] = (new_pixel[i] & ~1) | int(binary_message[binary_index])
                binary_index += 1
        new_pixels.append(tuple(new_pixel))
    
    img.putdata(new_pixels)
    img.save(output_path)
    print("[+] Successfully saved encoded image as", output_path)


def decode_image(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    binary_message = ''
    
    for pixel in pixels:
        for i in range(3):
            binary_message += str(pixel[i] & 1)
    
    message_bits = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ''
    for byte in message_bits:
        if byte == '11111111':
            break
        message += chr(int(byte, 2))
    print("[+] Hidden message:", message)


def main():
    parser = argparse.ArgumentParser(description="Steganography Tool - Hide or Retrieve Messages in Images")
    parser.add_argument("--encode", action="store_true", help="Encode a message into an image")
    parser.add_argument("--decode", action="store_true", help="Decode a message from an image")
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--message", help="Message to encode (only required for encoding)")
    parser.add_argument("--output", help="Path to save encoded image (only required for encoding)")
    
    args = parser.parse_args()
    
    if args.encode:
        if not args.message or not args.output:
            print("[-] Encoding requires --message and --output")
            return
        encode_image(args.image, args.message, args.output)
    elif args.decode:
        decode_image(args.image)
    else:
        print("[-] Please specify either --encode or --decode")

if __name__ == "__main__":
    main()
