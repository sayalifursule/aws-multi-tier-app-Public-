# AWS Multi-Tier Web Application (Public Deployment)

## Project Overview
This project demonstrates a fully deployed **multi-tier web application on AWS** using EC2, Application Load Balancer (ALB), Flask backend, Apache frontend, and Amazon RDS MySQL database.

The system follows a scalable cloud architecture where user requests are handled through multiple layers:
Frontend → Backend → Database

---

## Architecture

User → Application Load Balancer → Frontend EC2 → Backend EC2 → Amazon RDS MySQL

---

## Tech Stack

- AWS EC2 (Frontend & Backend)
- AWS Application Load Balancer (ALB)
- Amazon RDS (MySQL Database)
- Flask (Python Backend API)
- Apache HTTP Server (Frontend)
- HTML, JavaScript
- PyMySQL (Database connectivity)

---

## Features

- Multi-tier architecture deployment on AWS
- Load balancing using ALB
- Backend API using Flask
- Frontend hosted on Apache server
- Database integration with Amazon RDS MySQL
- Secure communication using AWS Security Groups
- End-to-end request flow from UI to database

---

## Working Flow

1. User opens ALB DNS URL  
2. Request goes to Frontend EC2 (Apache)  
3. Frontend sends request to Backend API (/api)  
4. Backend connects to RDS MySQL database  
5. Response is returned to frontend and displayed to user  

---

## Project Screenshots

### Frontend Working
<img width="940" height="499" alt="Frontend" src="https://github.com/user-attachments/assets/3fb4917c-be3d-4b8a-a872-af7a71221f4b" />

---

### Backend Working
<img width="940" height="499" alt="Backend" src="https://github.com/user-attachments/assets/44347bcd-34aa-4b55-a0f2-40cedae1775f" />

---

### Frontend → Backend Connection
<img width="940" height="499" alt="Connection" src="https://github.com/user-attachments/assets/ceff3e58-1c4a-4da5-aace-b2fb1d0561d5" />

---

### ALB DNS Working
<img width="940" height="529" alt="ALB DNS" src="https://github.com/user-attachments/assets/77e165de-e8b1-4393-827f-630833b011e5" />

---

### ALB Routing (Frontend + Backend)
<img width="940" height="499" alt="ALB Routing" src="https://github.com/user-attachments/assets/aa38b2d1-fa1d-4225-b1bf-c4829609f048" />

---

### Target Group Healthy Status
<img width="940" height="529" alt="Target Group" src="https://github.com/user-attachments/assets/40945440-3850-4ea4-a167-523b8d1f697a" />

---

## Key Learnings

- AWS EC2 instance deployment
- Application Load Balancer configuration
- Flask backend API development
- Apache frontend setup
- RDS MySQL database integration
- Security Group configuration
- Real-world multi-tier architecture design

---

## Resume Highlight

Designed and deployed a scalable multi-tier web application on AWS using EC2, Application Load Balancer, Flask, Apache, and Amazon RDS with end-to-end connectivity and secure cloud architecture.

---

## Project Status

Frontend: Working  
Backend: Working  
Database: Connected  
ALB: Active  
Target Group: Healthy  
Project: COMPLETED 



