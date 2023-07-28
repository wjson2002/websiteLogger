function getIPAddress() {
    fetch('https://api.ipify.org?format=json')
        .then(response => response.json())
        .then(data => {
            // Update the paragraph element with the IP address
            let ipAddress = data.ip;
            console.log('IP Address:', ipAddress);
            // Call the function to display the IP address and post it
            updateIPAndPost(ipAddress);
        })
        .catch(error => {
            console.error('Error fetching IP address:', error);
        });
}

function postIPAddress(ipAddress) {
    $.ajax({
        url: 'https://5asnqpgke4.execute-api.us-east-1.amazonaws.com/Live/',
        type: 'POST',
        data: JSON.stringify({
            ip: ipAddress
        }),
        contentType: 'application/json'
    });
}

function updateIPAndPost(ipAddress) {
    const formattedIP = "Your IP: " + ipAddress;
    document.getElementById('ip-address').textContent = formattedIP;
    postIPAddress(ipAddress);
}

// Call the function to update the visit count when the page loads
$(document).ready(function () {
    getIPAddress();
});

console.log("JS DONE RUNNING");

