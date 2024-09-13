
# Artistic image generator based on selecting Color from a palette  - PyQt5 Art App

This is a simple PyQt5 application that allows you to create an artistic color palette and generate random shapes with the colors you choose. It uses `matplotlib` for rendering the artwork and PyQt5 for the graphical user interface.

## Features

- **Color Selection**: Select as many colors as you want using a color picker.
- **Artwork Generation**: Randomly generates a grid of circles and squares in the selected colors.
- **Interactive UI**: Simple user interface to pick colors and render the artwork.

## Requirements

To run the application, you need to have the following installed:

- Python 3.x
- PyQt5
- Matplotlib
- NumPy

You can install the dependencies via pip:

```bash
pip install PyQt5 matplotlib numpy
```

## How to Run

1. Clone the repository or download the script.
2. Run the script with Python:

```bash
python art_app.py
```

## Application Overview

### Color Picker
Click the "Pick Color" button to open the color dialog. Select colors and they will be added to your palette.

### Render Artwork
Once you have selected your colors, press the "Render" button to generate random shapes with your color palette. Each render will be unique!

## Example Output

The app generates an artistic pattern of circles and squares using the colors you've selected, similar to abstract modern art.

Enjoy creating your own random colorful art pieces!

## License
MIT License
