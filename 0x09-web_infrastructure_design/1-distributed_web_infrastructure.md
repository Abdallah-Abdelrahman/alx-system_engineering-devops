# 1-distributed_web_infrastructure:

![Udgrading with another server + load Balancer](https://i.imgur.com/OHVeiq1.png)

**1. Additional Servers:**
Incorporating two additional servers into the infrastructure facilitates load distribution and mitigates
the risk of a single point of failure (SPOF).
This enhancement bolsters the system's capacity to manage increased traffic and provides redundancy,
safeguarding against server failure.

**2. Load Balancer (HAproxy):**
The load balancer, HAproxy in this case, is tasked with evenly distributing incoming traffic across multiple
servers to prevent any single server from becoming overwhelmed.
This strategy optimizes resource utilization, minimizes response time, and bolsters the reliability of applications.

**3. Distribution Algorithm:**
The load balancer could be configured with a round-robin algorithm, which sequentially distributes requests
to servers in a cyclical order. This method ensures equitable load sharing among all servers.

**4. Active-Active vs Active-Passive Setup:**
In an active-active configuration, all servers are engaged in traffic handling, maximizing resource utilization.
Conversely, in an active-passive setup, one server is active while the others remain on standby,
serving as a backup should the active server fail.

**5. Database Primary-Replica Cluster:**
In a primary-replica setup, the primary node is responsible for write operations, while the replica
nodes manage read operations.
This division of responsibilities can enhance performance by enabling concurrent processing
of read and write operations.

**6. Primary Node vs Replica Node:**
The primary node is capable of handling both read and write operations,
while the replica node is restricted to read operations. This allows the primary node to concentrate
on processing write operations without being impeded by read requests.

## Potential Issues with This Infrastructure:

**1. Single Point of Failure (SPOF):**
Despite the presence of multiple servers, SPOFs may still exist. For instance, if the load balancer fails,
the entire system could become inaccessible.

**2. Security Issues:**
In the absence of a firewall or HTTPS, the system is susceptible to attacks. It is imperative to implement
appropriate security measures to safeguard the system and its data.

**3. Absence of Monitoring:**
Without monitoring, it becomes challenging to promptly identify and rectify issues.
Monitoring tools can offer valuable insights into system performance and facilitate early
detection of problems before they impact users.
