# websiteLogger

About:
The goal of this project is to learn about how to setup and connect AWS infrastructure. We used HTML, CSS, and JS for frontend combined with AWS API Gateway, AWS Lambda, and DynamoDB for backend. Each component creates a microservice architecture, which allows for a highly reliable and scalable solution.

Each time someone visits the website, their IP address will be grabbed by JS and sent through the API Gateway. Then AWS Lambda will process this request by storing the IP address in DynamoDB and some data back to to the website. Finally the website will display some metrics (total visits by IP, total unique vistors) about the IP address to the user.

Sample site:

<img width="736" alt="Screenshot 2023-08-01 at 10 01 26 AM" src="https://github.com/wjson2002/websiteLogger/assets/61726454/a77976f9-bca4-4146-8a57-265256d3482e">


