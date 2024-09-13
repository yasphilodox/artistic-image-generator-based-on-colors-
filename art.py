import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QColorDialog, QLabel, QVBoxLayout, QWidget
import matplotlib.pyplot as plt
import numpy as np

class ArtApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.colors = []

        # Setting up the window
        self.setWindowTitle("Artistic Color Palette")
        self.setGeometry(100, 100, 300, 200)

        # Layout
        layout = QVBoxLayout()
        self.label = QLabel("Select colors, then press 'Render'!")
        layout.addWidget(self.label)

        # Button to select colors
        self.color_button = QPushButton("Pick Color", self)
        self.color_button.clicked.connect(self.open_color_dialog)
        layout.addWidget(self.color_button)

        # Button to render the artwork
        self.render_button = QPushButton("Render", self)
        self.render_button.clicked.connect(self.render_artwork)
        layout.addWidget(self.render_button)

        # Setting the layout for the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_color_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.colors.append(color.name())  # Save the selected color as hex
            self.label.setText(f"{len(self.colors)} colors selected.")

    def render_artwork(self):
        if not self.colors:
            self.label.setText("No colors selected!")
            return

        # Create an artistic representation
        plt.figure(figsize=(6, 6))

        for i in range(100):
            # Randomize the shape, position, and size of the objects
            x, y = random.uniform(0, 1), random.uniform(0, 1)
            size = random.uniform(50, 500)
            color = random.choice(self.colors)

            shape_type = random.choice(['circle', 'square'])

            if shape_type == 'circle':
                circle = plt.Circle((x, y), size / 1000, color=color, alpha=0.7)
                plt.gca().add_artist(circle)
            else:
                plt.gca().add_patch(plt.Rectangle((x, y), size / 1000, size / 1000, color=color, alpha=0.7))

        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.axis('off')  # Remove axes for a cleaner look
        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ArtApp()
    window.show()
    sys.exit(app.exec_())
