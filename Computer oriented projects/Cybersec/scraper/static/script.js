function scrapeInfo() {
    const username = document.getElementById('username').value;
    fetch('/scrape', {
        method: 'POST',
        body: new URLSearchParams({ 'username': username }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
        .then(response => response.json())
        .then(data => {
            let resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            for (let platform in data) {
                resultsDiv.innerHTML += `<h2>${platform}</h2>`;
                resultsDiv.innerHTML += `<p>Username: ${data[platform].username}</p>`;
                resultsDiv.innerHTML += `<p>Profile Picture: ${data[platform].profile_picture}</p>`;
                resultsDiv.innerHTML += `<p>Personal Info: ${data[platform].personal_info}</p>`;
                resultsDiv.innerHTML += '<hr>';
            }
            resultsDiv.innerHTML += '👍 If you want more professional AI prompts and free tools, please visit: <a href="https://digitalprofits7.com/">https://digitalprofits7.com/</a> 🤖';
        });
}
