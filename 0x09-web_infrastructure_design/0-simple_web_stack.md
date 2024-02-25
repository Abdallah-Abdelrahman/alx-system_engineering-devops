# 0-simple_web_stack:

![First Infrastructure](https://i.imgur.com/FURoOD9.png)

**1. Server:**
A server is a robust computing device engineered to manage, store, send and process data 24/7.
It forms the backbone of network resources, offering a centralized system for data storage and application hosting.

**2. Domain Name:**
The domain name, in this case, foobar.com, serves as the unique digital address of your website on the internet.
It allows users to access your website without needing to remember the IP address.

**3. DNS Record:**
The 'www' in 'www.foobar.com' is a type of DNS record known as a CNAME (Canonical Name).
It is essentially an alias used to redirect multiple domain names to a single IP address.

**4. Web Server (Nginx):**
The web server, Nginx in this scenario, is responsible for accepting and processing requests from the
user's browser. It serves static content to the client and acts as a reverse proxy for dynamic content generation.

**5. Application Server:**
The application server is the heart of your web infrastructure. It hosts the business logic of the web applications,
processing requests from the web server, interacting with the database, and generating dynamic web content.

**6. Database (MySQL):**
The MySQL database is a relational database management system that stores, retrieves,
and manages data required by the application server to generate dynamic web content.

**7. Communication:**
The server communicates with the user's computer using the HTTP/HTTPS protocol, which is a set of rules for
transferring files (text, graphic images, sound, video, and other multimedia files) on the World Wide Web.

## Potential Issues with This Infrastructure:

**1. Single Point of Failure (SPOF):**
With all components hosted on a single server, any failure in the server hardware or software
would render the entire website unavailable, leading to a significant service disruption.

**2. Downtime for Maintenance:**
Maintenance activities, such as deploying new code or restarting the web server,
would necessitate some downtime, making the website temporarily inaccessible to users.

**3. Scalability Concerns:**
A single server may not be equipped to handle a surge in traffic, leading to potential performance
degradation or even downtime.
This infrastructure lacks the flexibility to scale resources up or down based on demand.
