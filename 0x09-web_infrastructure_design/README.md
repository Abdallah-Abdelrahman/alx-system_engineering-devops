# 0x09. Web Infrastructure Design

This project is part of the Alx - SE curriculum of software engineering. The main objective is to understand and implement the concepts of web infrastructure design.

By: Sylvain Kalache, co-founder at Holberton School


## Learning Objectives

- Understand what a database is and its purpose in web infrastructure.
- Learn the difference between a web server and an app server.
- Understand DNS record types and their roles in web infrastructure.
- Learn about the concept of a single point of failure and its implications.
- Understand how to avoid downtime when deploying new code.
- Learn about high availability clusters (active-active/active-passive) and their role in maintaining uptime.
- Understand what HTTPS is and its importance in web infrastructure.
- Learn what a firewall is and its role in securing web infrastructure.

## Tasks:

#### First infrastructure:

First infratructure consists of simple webserver(Nginx), application server to manage dynamic contents, Mysql server and.
refere to task [0-simple_web_stack](https://github.com/Mohabdo21/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.md) for more info.

#### Second infrastructure:

Here we have leveled up the our infratructure a little by adding anohter server/cluster to comprises the different components (webserver, application server, DB server and HAproxy load balancer). refer to task [1-distributed_web_infrastructure](https://github.com/Mohabdo21/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.md) for more details.

#### Third infrastructure:

We added additonal layers of security represented in SSL/TLS certificate and firewalls between each server and added data collectors for  _Sumologic_  monitoring service. Refer to to task [2-secured_and_monitored_web_infrastructure](https://github.com/Mohabdo21/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.md) for more.

#### Fourth infrastructure:

In this stage we scaled-up the infrastructure by improving the availability of our server through adding another load balancer and additional server. for more refer to [3-scal_up](https://github.com/Mohabdo21/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/3-scale_up.md).

## More Info

This project is designed to give a practical understanding of how web infrastructure works and how various components interact with each other. By the end of this project, we will be able to design and implement robust and secure web infrastructure.

## Authors:
_Abdallah Abdelrahman_ - abdallah_alkaser@outlook.com <br />
_Mohannad Abdulaziz_ - mohannadabdo21@hotmail.com
