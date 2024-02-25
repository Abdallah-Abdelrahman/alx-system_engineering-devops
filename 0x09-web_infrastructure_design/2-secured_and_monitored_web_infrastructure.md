# 2-secured_and_monitored_web_infrastructure:

![Add More Security](https://i.imgur.com/t00ALOR.png)

**1. Firewalls:**
The incorporation of a firewall for each server significantly enhances the security of the system.
Firewalls meticulously control the inflow and outflow of network traffic based on an established set of security rules,
thereby permitting only authorized traffic and blocking any potential threats.

**2. SSL Certificate:**
The implementation of an SSL certificate allows the server to serve traffic over HTTPS.
This protocol ensures the encryption of data transmitted between the user's browser and the server,
safeguarding any sensitive information from potential security breaches.

**3. Monitoring Clients:**
The addition of monitoring clients to each server facilitates the collection and analysis of data pertaining
to the server's performance. This aids in promptly identifying any potential issues or bottlenecks,
thereby ensuring the smooth and efficient operation of the servers.

**4. Monitoring Web Server QPS:**
To monitor the web server's Queries Per Second (QPS), one can utilize a monitoring tool such as
Sumologic or Datadog. These tools collect data from the server logs, providing valuable insights
into the web server's performance.

## Potential Issues with This Infrastructure:

**1. Terminating SSL at the Load Balancer:**
If SSL termination occurs at the load balancer, the traffic between the load balancer and the servers is
not encrypted. This could potentially expose sensitive data if the internal network is compromised.

**2. Single MySQL Server for Writes:**
Having only one MySQL server capable of accepting writes poses a potential bottleneck. If that server fails
or becomes overwhelmed, it could adversely affect the entire system.

**3. Same Components on All Servers:**
Deploying the same components (database, web server, and application server) on all servers can lead
to inefficient resource utilization. It is generally more efficient to allocate separate servers for
distinct tasks.
