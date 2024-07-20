document.getElementById('summarizeForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);

    fetch('/summarize', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        let summaryResultHTML = `<div class="article-summary">`;

        if (data.image) {
            summaryResultHTML += `
                <img src="${data.image}" alt="Article Image">
                <p class="image-credit">Image source: <a href="${data.url}" target="_blank">${data.url}</a></p>
            `;
        }

        summaryResultHTML += `
            <h3>Summary:</h3>
            <p>${data.summary}</p>
            <h3>Generated Response:</h3>
            <p>${data.response}</p>
        </div>`;

        document.getElementById('summaryResult').innerHTML = summaryResultHTML;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
