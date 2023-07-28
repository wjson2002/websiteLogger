// script.js
import $ from 'jquery';

function getIPAddress() {
    fetch('https://api.ipify.org?format=json')
        .then(response => response.json())
        .then(data => {
            // Update the paragraph element with the IP address
            const ipAddress = data.ip;
            // Resolve the Promise with the IP address
            console.log('IP Address:', ipAddress);
            resolve(ipAddress);

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

// Call the function to update the visit count when the page loads
$(document).ready(function () {
    let ip = getIPAddress();
    document.getElementById('ip-address').textContent = ipAddress;
    postIPAddress(ip);
});
