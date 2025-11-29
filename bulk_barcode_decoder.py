import os
import pyzbar.pyzbar as pyzbar
from PIL import Image

# Directory containing the barcode images
barcodes_folder = './Barcode_World'

# List for storing decoded fragments of the hidden message
hidden_message = []

# Iterate through files named 1.png ... 9374.png (sorted numerically)
for i in range(1, 9375):

    # Construct full path to the image file
    image_path = os.path.join(barcodes_folder, f'{i}.png')

    # Skip if the file does not exist
    if not os.path.exists(image_path):
        continue

    try:
        # Load the image using Pillow
        image_pillow_object = Image.open(image_path)

        # Attempt to decode any barcodes present in the image
        data_reading = pyzbar.decode(image_pillow_object)

        # If decoding returned data, extract the text content
        if data_reading:
            hidden_text = data_reading[0].data.decode('utf-8')

            # Debug output
            print(hidden_text)

            # Append decoded fragment to the message list
            hidden_message.append(hidden_text)

    except Exception as error:
        # Log any issues encountered during processing
        print(f"Error decoding {image_path}: {error}")
        continue

# Combine all decoded fragments into the final message
print("".join(hidden_message))
