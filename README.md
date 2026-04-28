# TaskMaster

Many people struggle to plan out their day with all the tasks they have, especially students, juggling classes, sports and ECs. This can lead to unfinished tasks and can take a mental toll on students by increasing their stress. Taskmaster looks to solve this problem by creating an easy to use, digital whiteboard for students to plan out their day.

Taskmaster is a tool which helps students keep track of and plan the work - or tasks - they need to do. It will (hopefully) connect to Canvas’ API to load tasks from classes.

---

## 1. Introduction
 
### 1.1 Purpose
 
Taskmaster is a tool which helps students keep track of and plan the work — or tasks — they need to do. It will connect to Canvas' API to load tasks from classes if not added explicitly by the user.
 
### 1.2 Document Conventions
 
| Abbreviation | Definition |
|---|---|
| GUI | Graphical User Interface |
| API | Application Programming Interface |
 
### 1.3 Intended Audience
 
| Audience | Relevant Sections |
|---|---|
| Project Managers | Sections 1 & 2 — evaluate feasibility and scope |
| Testers | Sections 3 & 5 — develop appropriate test cases |
| Developers | Sections 2–5 — understand functionality and technical expectations |
 
All of these parties are stakeholders and will have access to this document to stay aligned.
 
### 1.4 Scope
 
The goals of TaskMaster align with GRS's commitment to clear, organized, and streamlined management and work ethic. This project benefits the business by creating software that does exactly that — actualizing company goals to benefit both public reputation and business credibility.
 
### 1.5 References
 
None.
 
---
 
## 2. General Description
 
### 2.1 Product Perspective
 
Many people struggle to plan out their day with all the tasks they have, especially students juggling classes, sports, and extracurriculars. This can lead to unfinished tasks and increased stress. Taskmaster looks to solve this problem by creating an easy-to-use digital whiteboard for students to plan out their day.
 
### 2.2 Product Features
 
Taskmaster will start by letting a user input all the tasks they need to finish, including:
 
- How long each task takes
- Specific deadlines
- How much time they have left to complete them
The software will then create a schedule for the rest of the student's day that prioritizes tasks based on the earliest deadline and leaves time for breaks. If the student is curious about why the schedule was made the way it was, they can ask, and Taskmaster will give a brief summary on how the schedule was decided. Potential integration with AI for the above.
 
### 2.3 User Class and Characteristics
 
Taskmaster appeals to anyone who needs a way to plan out their day, but specifically targets students who are managing school, extracurriculars, and other responsibilities throughout their day.
 
### 2.4 Operating Environment
 
The software runs in a Python IDE and requires internet access due to the integration of Flask.
 
### 2.5 Constraints
 
- Time frame available to complete the project
- Learning curve for implementing Python for the backend
- Learning curve for implementing Flask for the frontend
### 2.6 Assumptions and Dependencies
 
- The project assumes that users need more organization and planning for the tasks they have at hand.
- Target users are assumed to be school students or members of the workforce who need more organization.
### 2.7 Source Code Repository
 
[https://github.com/WaffleDG/task-master](https://github.com/WaffleDG/task-master)
 
---
 
## 3. System Requirements
 
### 3.1 Functional Requirements
 
- Requires access and use of **Python 3.13 or above**.
---
 
## 4. External Interface Requirements
 
### 4.1 User Interfaces
 
The home screen will include a graphic and buttons to enter tasks. Once "Enter Tasks" is clicked, the user will see options to:
 
- **Enter New Task**
- **View Current Schedule**
- **View Whiteboard**
Once a new task is entered, the user can then see their updated schedule made by TaskMaster. The overall style will be simple (simple colors, clean font) and easy to follow.
 
### 4.2 Hardware Interfaces
 
The program runs with network access on a computer and is intended to work wherever Python works — **Windows, Mac, and Linux**.
 
### 4.3 Communications Interfaces
 
The system will communicate with the user through the GUI.
 
### 4.4 Software Interfaces
 
- **Frontend:** GUI developed in Python
- **Backend:** Canvas API keys to connect TaskMaster to Canvas
---
 
## 5. Non-Functional Requirements
 
### 5.1 Performance Requirements
 
Minimum additional performance requirements needed.
 
### 5.2 Safety Requirements
 
Any explanations or messages given to the user will be pre-written or restricted so that the system cannot give inaccurate or potentially harmful information.
 
### 5.3 Security Requirements
 
Any data entered in the program will not be shared.
 
### 5.4 Software Quality Attributes
 
The program will be:
 
- Usable
- Reliable
- Functional
- Productive
- Catered to students' needs
### 5.5 Other Requirements
 
None.