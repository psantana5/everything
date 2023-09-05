document.getElementById('password-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var website = document.getElementById('website').value;
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var passwordItem = document.createElement('div');
    passwordItem.innerHTML = '<h2>' + website + '</h2><p>Username: ' + username + '</p><p>Password: ' + password + '</p>';
    document.getElementById('password-list').appendChild(passwordItem);
    document.getElementById('website').value = '';
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
});
document.getElementById('add-password-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from being submitted normally

    var website = document.getElementById('website-input').value;
    var username = document.getElementById('username-input').value;
    var password = document.getElementById('password-input').value;

    fetch('/api/passwords', { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ website: website, username: username, password: password }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Password added:', data);
        window.location.href = 'index.html';  // Redirect to the index page
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

