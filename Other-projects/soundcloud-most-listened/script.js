const generateBtn = document.getElementById('generateBtn');
const downloadLink = document.getElementById('downloadLink');
const codeInput = document.getElementById('codeInput');

generateBtn.addEventListener('click', async () => {
    const userQuery = codeInput.value;

    try {
        const documentation = await getDocumentationFromAPI(userQuery);
        const pdfURL = await generatePDF(documentation);

        downloadLink.style.display = 'block';
        downloadLink.href = pdfURL;
    } catch (error) {
        console.error("An error occurred:", error);
    }
});

async function getDocumentationFromAPI(query) {
    const response = await fetch('/getDocumentation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            prompt: query
        })
    });

    const data = await response.json();
    return data.documentation;
}

async function generatePDF(documentation) {
    const response = await fetch('/generatePDF', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            htmlContent: documentation
        })
    });

    const data = await response.json();
    return data.pdfUrl;
}
