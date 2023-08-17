// jwt_sender/static/js/sender_script.js
function sendJWT() {
    fetch('/send_jwt/')  // Use the correct URL for the send_jwt view
    .then(response => response.json())
    .then(data => {
        const jwtToken = data.jwt_token;  // Extract the JWT token from the response
        console.log("JWT Token:", jwtToken);  // Print the extracted token for verification

        fetch('/receive_jwt/', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${jwtToken}`,
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({}),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
            console.log("CSRF Token:", csrfToken);
            receiveJWT(data.jwt_token);  // Call the receiveJWT function from receiver_script.js
        })
        .catch(error => {
            console.error(error);
        });
    })
    .catch(error => {
        console.error(error);
    });
}

sendJWT();
