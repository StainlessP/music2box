# Music Notation Translator

A simple web application that translates staff notation into Jianpu (numbered musical notation) and renders it as an SVG image.

This project is the Minimum Viable Product (MVP) and serves as a foundation for more advanced features.

## Features

*   Accepts text-based note input (e.g., `C4 D4 E5`).
*   Translates notes into Jianpu numerical representation.
*   Renders the Jianpu score as a scalable SVG image, including octave indicators.

## Technology Stack

*   **Backend:** Python 3, Flask, music21
*   **Frontend:** HTML, CSS, vanilla JavaScript

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Start the Flask server:**
    ```bash
    python3 app.py
    ```

2.  **Open the application in your browser:**
    Navigate to `http://127.0.0.1:5000`.

## How to Use

1.  Enter notes into the text area. Use standard pitch notation where the letter is the note name and the number is the octave (e.g., `C4` is Middle C). Separate notes with spaces.
2.  Example input: `C4 G4 A4 G4 E4 D4 C4`
3.  Click the **Translate** button.
4.  The generated Jianpu score image will appear below the button.
