# Blue Team Labs Online (BTLO) - Challenge Write-up: "Barcode World"

**Category:** Scripting / Malware Analysis / Forensics  
**Author:** Krystian Węcławiak  
**Date:** 29.11.2025  
**Platform:** [Blue Team Labs Online](https://blueteamlabs.online/)
---

## Challenge Overview
The "Barcode World" challenge presents a scenario where the analyst is provided with a folder containing **9,374 PNG images**. Each image contains a fragment of a barcode. The objective is to extract the hidden information and retrieve the flag.

Manual analysis was unfeasible due to the volume of data. The task required developing an automated Python script to iterate through the dataset, decode the visual data, and reconstruct the message.

## Repository Contents

This repository contains two Python scripts demonstrating the full cycle of the analysis:

### 1. `barcode_world_solver.py` 
This is the main script used to solve the challenge.
- **Function:** Iterates through the images in strict numerical order (`1.png` to `9374.png`), decodes the barcode using `pyzbar`, and reconstructs the hidden ASCII stream.
- **Key Logic:** It addresses the file sorting issue (alphanumeric vs numerical) and converts the decoded decimal ASCII values back into a readable string to reveal the flag.

### 2. `challenge_reconstruction.py` 
This script was created as a "Proof of Concept" to reverse-engineer the challenge creator's logic.
- **Function:** It demonstrates how the original dataset was likely generated.
- **Logic:** It takes a plaintext string, converts characters to split ASCII digits (using `enumerate` and `ord`), and generates individual Code128 barcodes for each digit.
  
## Installation & Usage

### Prerequisites
To run these scripts, you need **Python 3.x** and the following external libraries.

1. **Install dependencies:**

```bash
pip install pyzbar pillow python-barcode
```

*(Note: On Linux, you may also need to install the zbar shared library, e.g., `sudo apt-get install libzbar0`)*

### Running the Solver

Ensure the dataset images are in a folder named `./Barcode_World`.

```bash
python barcode_world_solver.py
```

## Technical Analysis

### Why strict numerical iteration?

Standard file system iteration (like `os.listdir`) often sorts files alphanumerically:
`1.png`, `10.png`, `100.png`, `2.png`...
Running the decoder in this order would scramble the message. The solver forces a numerical loop (`range(1, 9375)`) to maintain the integrity of the data stream.

### Decoding Logic

The raw output from the barcodes appeared as a sequence of numbers (e.g., `['6', '5', ' ', '3', '2']`).

  * **6, 5** → `65` → ASCII **'A'**
  * **3, 2** → `32` → ASCII **'Space'**

The solver reconstructs these pairs into integers and converts them using `chr()` to retrieve the plaintext history of barcodes, which contained the flag.
-----


## Disclaimer

*This repository is for educational purposes only. It is intended to demonstrate scripting and analysis skills in the context of a cybersecurity Capture The Flag (CTF) challenge.*
