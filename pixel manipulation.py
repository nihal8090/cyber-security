def encrypt_image(input_image_path, output_image_path):
    # Open the input image
    img = Image.open(input_image_path)
    pixels = img.load()
    
    # Get image dimensions
    width, height = img.size
    
    # Encrypt the image by swapping red and blue channels
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (b, g, r)
    
    # Save the encrypted image
    img.save(output_image_path)

def decrypt_image(input_image_path, output_image_path):
    # Decrypting is the same operation as encrypting
    encrypt_image(input_image_path, output_image_path)

# Example usage
encrypt_image('input.jpg', 'encrypted.jpg')
decrypt_image('encrypted.jpg', 'decrypted.jpg')
