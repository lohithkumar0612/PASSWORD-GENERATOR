document.getElementById('password-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const favoriteThing = document.getElementById('favorite-thing').value;

    fetch('/generate_password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ favoriteThing }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('password-output').textContent = data.password;
    });
});
