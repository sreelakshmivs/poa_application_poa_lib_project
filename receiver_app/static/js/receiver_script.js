// Your JavaScript code here to receive and display the JWT token data
// jwt_receiver/static/js/receiver_script.js

function receiveJWT(jwtToken) {
    const targetURL = 'http://localhost:8001/receiver_template/';

    fetch(targetURL, {
        headers: {
            'Authorization': `Bearer ${jwtToken}`,
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error(error);
    });
}

// You can call the receiveJWT function here if needed
