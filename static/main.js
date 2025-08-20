document.addEventListener('DOMContentLoaded', () => {
    const translateButton = document.getElementById('translate-button');
    const notesInput = document.getElementById('notes-input');
    const outputContainer = document.getElementById('output-container');

    translateButton.addEventListener('click', () => {
        const notes = notesInput.value;

        // Clear previous output and show loading message
        outputContainer.innerHTML = 'Translating...';

        // Make the API call to the backend
        fetch('/api/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ notes: notes }),
        })
        .then(response => response.json())
        .then(data => {
            // Clear the loading message
            outputContainer.innerHTML = '';

            if (data.error) {
                // Display error message if something went wrong
                outputContainer.innerHTML = `<p style="color: red;">${data.error}</p>`;
            } else if (data.svg && data.svg.length > 0) {
                // The backend sends an SVG string. We can embed it directly
                // or use a data URL. Embedding directly is simpler and safer.
                outputContainer.innerHTML = data.svg;
            } else {
                // Handle case for empty input or no svg returned
                outputContainer.innerHTML = '<p>No output generated. Try entering some notes.</p>';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            outputContainer.innerHTML = '<p style="color: red;">An unexpected error occurred. Please check the console.</p>';
        });
    });
});
