from flask import Flask, render_template, jsonify, request
from music21 import note, stream
import base64

app = Flask(__name__)

def generate_jianpu_svg(notes_string):
    """
    Translates a string of notes (e.g., "C4 D4 E4") into a Jianpu SVG image.
    """
    # SVG parameters
    font_size = 36
    note_spacing = 50
    start_x = 30
    y_baseline = 60
    octave_dot_radius = 2.5
    octave_dot_spacing = 8

    # Parse notes using music21
    try:
        s = stream.Stream()
        note_names = notes_string.strip().split()
        if not note_names:
            return None # Handle empty input
        for note_name in note_names:
            s.append(note.Note(note_name))
    except Exception as e:
        print(f"Music21 parsing error: {e}")
        return "Error: Invalid note string"

    # SVG generation
    jianpu_map = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7}
    svg_elements = []
    current_x = start_x

    for i, n in enumerate(s.notes):
        # Draw note number
        jianpu_num = jianpu_map.get(n.pitch.step, '?') # Use .get for safety
        svg_elements.append(f'<text x="{current_x}" y="{y_baseline}" font-size="{font_size}" text-anchor="middle">{jianpu_num}</text>')

        # Draw octave dots
        octave = n.pitch.octave
        if octave > 4:
            for j in range(octave - 4):
                dot_y = y_baseline - font_size + 5 - (j * octave_dot_spacing)
                svg_elements.append(f'<circle cx="{current_x}" cy="{dot_y}" r="{octave_dot_radius}" fill="black" />')
        elif octave < 4:
            for j in range(4 - octave):
                dot_y = y_baseline + 10 + (j * octave_dot_spacing)
                svg_elements.append(f'<circle cx="{current_x}" cy="{dot_y}" r="{octave_dot_radius}" fill="black" />')

        current_x += note_spacing

    # Assemble the final SVG
    svg_width = current_x
    svg_height = 120
    svg_content = f'<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">{"".join(svg_elements)}</svg>'

    return svg_content


@app.route('/')
def index():
    """
    Serves the main HTML page.
    """
    return render_template('index.html')

@app.route('/api/translate', methods=['POST'])
def api_translate():
    """
    API endpoint to handle the translation request.
    Returns a Jianpu SVG image.
    """
    data = request.get_json()
    if not data or 'notes' not in data:
        return jsonify({'error': 'Invalid request: "notes" key missing'}), 400

    notes_string = data['notes']
    svg_output = generate_jianpu_svg(notes_string)

    if "Error:" in svg_output:
        return jsonify({'error': svg_output}), 400

    if svg_output is None:
        return jsonify({'svg': ''}) # Return empty SVG for empty input

    # It's good practice to encode SVG for JSON transfer, though not strictly required
    # For this implementation, we will return the raw SVG string.
    return jsonify({'svg': svg_output})

if __name__ == '__main__':
    app.run(debug=True)
