// script.js
import $ from 'jquery';


function updateVisitCount() {
    $.ajax({
        url: 'https://y36d9igl7f.execute-api.us-west-1.amazonaws.com/Peer_Live/peer?ip=0.0.0.0',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            // Update the visit count on the web page
            $('#visitCount').text(data.visitCount);
        },
        error: function (error) {
            console.error('Failed to update visit count:', error);
        }
        
    });
}

// Call the function to update the visit count when the page loads
$(document).ready(function () {
    updateVisitCount();
});


