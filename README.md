# LinkedinSpearMailer
automates the scheduling of messages on linkedin. send direct message to targeted users on linked in and schedule the time of message delivery.

## Demo
![Demo](https://raw.githubusercontent.com/Harshit00yadav/LinkedinSpearMailer/main/demos/demo_01.gif)

 + ask's for your credentials and target's linkedin profile name
 + launches an instance of chromium browser
 + log in with your entered credentials
 + search for the target user
 + send messages from the `./messages_per_person.txt` to the target

## Installation
prerequisite : bash, python3
```bash
git clone https://github.com/Harshit00yadav/LinkedinSpearMailer.git
bash ./setup.sh
```

## Use
for linux:
```bash
source venv/bin/activate
python SpearMailer.py
deactivate
```
