# HackAI IIT Bombay Techfest Finale


## Video Demo
You can watch a video demo of our project: [Google Drive Video Folder](https://drive.google.com/drive/folders/1PLGQ_YnQ4fvnEtzlbFvwRCLQBNDxQVbf?usp=sharing)


## *Vision of FetchAI*
- Automate repetitive tasks
- Remove centralisation
- Replacing so many applications on our mobile phone with autonomous agents

## Project Information

## Abstract
Travelling to a new city and unsure of the places to visit?
Tired of the repetitive tasks of booking cabs?
Want an assistant who automatically gives you important reminders?
Wish you had a digital twin who makes your life easier by maximizing your productivity and economic value?

Well, this is absolutely what our project aims for! Let's dive in

### Assumptions made
- Each cab service agent would be deployed already on the fetch network.
- Currently we have pre determined the order of actions being performed between the agents. We assume DeltaV is gonna provide this functionality of deciding the optimal assembly of agents best facilitating the given user query.

## *Agents used in our Project, aligning with Vision of FetchAI*
1. User Agent
  - Interacts with other agents based on user input query
  - Knows the preferences of user based on previous interactions with agents
  - Aims to maximize the economic value of the user while also providing the best options towards user query
2. Travel Agent
  - Gives a travel plan according to user travel needs and preferences
  - Has the capability to call the calender agent and set up reminders for all set of events in our travel plan .
3. Cab Service Agent
  - Every cab driver owns its own cab service agent in accordance with a decentralised economy of agents.
  - Has the communication capability to *call the travel agent*.
4. Calender Agent
  - Puts up reminders for various events in our google calender
  - Can give the list of free slot within a time range to facilitate booking of appointments
  - Puts up a agent prefix on our events added to the calender. Also puts up the agent address of the agent the event is catering to.

![Screenshot (1383)](https://github.com/AryanShr/HACK_230395/assets/75170293/60b174d3-9f8b-4d3f-8306-ae5fbcb5ade6)


## Sample Flow of our Personal Assistant
1. User puts up a query "I am new to Delhi, suggest me a travel plan this weekend"
2. *User Agent* captures the query and calls the *Travel Agent* to get a list of latest travel plans that align with user preferences.
3. *Travel agent* responds with the list of travelling options.
4. *User agent* interacts with the user and gets the list of travel options confirmed.
5. *User agent* calls the *calender agent* to schedule the reminders for events in travel plans. The reminders are setup with certain agent suffix to distinguish the address of the agent it indicates to.
6. *User agent* calls the *travel agent* to schedule the cab service.
7. *Travel agent* broadcasts the travel source and destinations to *cab service agents.*  
8. Multiple cab service agents responds with their availability and location details back to the *user agent*. Finds the best economic value option for the user.
9. *User agent* interacts with the user and confirms one cab service and call the *cab service agent*
10.*Cab service agent* books the cab.


*Screenshots:*
## Screenshots
Reminder autonomously setup by calender agent
![appointmnet](https://github.com/AryanShr/laughing-eureka/assets/75170293/3de760fe-2460-4f67-bd8d-2d0a48cf9114)

*Technology Stack:*
- Python
- Fetch.ai uAgent Library
- Agentverse

## Getting Started

### Installation

1. Clone the repository:

   ```git clone https://github.com/AryanShr/HACK_230395.git```


2. Install the required dependencies

    
    ```
    cd temperature-alert-agent
    Install dependencies:
    pip install -r requirements.txt
    ```


3. Initialise the environment

    ```
    poetry install
    poetry shell
    ```

4. Running the ecosystems of agents

    ```
    python main.py
    python app.py
    python cab_booking.py
    ```
Run the above commands in order in different terminals
