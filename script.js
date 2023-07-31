
function getCounter() {
    fetch('https://5asnqpgke4.execute-api.us-east-1.amazonaws.com/Live/')
        .then(response => response.json())
        .then(data => {
            // Update the paragraph element with the IP address
            let curCount = data.count;
            console.log('Count:', curCount);
            // Call the function to display the IP address and post it
            updateCount(curCount);
        })
        .catch(error => {
            console.error('Error fetching count:', error);
        });
}


function updateYourCount(yCount){
    const currentYCount = "Your Total Visits: " + yCount;
    document.getElementById('yourCount').textContent = currentYCount;
    
}

function updateCount(count){
    const currentCount = "Total Unique Visitors: " + count;
    document.getElementById('count').textContent = currentCount;
    
}


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
        success: function(response) {
            let curYCount = response.yourIP[0].count.N;
            updateYourCount(curYCount);
            console.log(curYCount);
            console.log(response);
        },
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
    getCounter();

});

console.log("JS DONE RUNNING");

