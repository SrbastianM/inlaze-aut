# Inlaze Technical test
---
Technical test for inlaze
---
## Points of interest:
INSTALL DEPENDENCIES
- Remember install ```requirements.txt``` using the following command: ```pip install -r requirements.txt``` if you don't have it 
- To start the robot, you need to use the following command: ```behave``` in your terminal. This command runs all the scenarios in the folder features
- The unit test's are checking if the robot is normally or have some problem. To use it you need to use the following command ```pytest tests```
- To show the reports and analize the results of the tests run the following command ```allure serve ./allurereports``` this run the allure dependency and show in localhost the result of all the test's

- Clone the project following the next command ```git clone https://github.com/SrbastianM/inlaze-aut.git``` remember! if you had install git on you device, if not install it :D

# Preview of the project
![image](https://github.com/user-attachments/assets/0c780cd1-534b-4a73-b508-c9ed6459b80e)

- In the preview image you can follow the project arquitecture.
- The first folder you can see is the allurereports, this folder contains all the screenshots and settings to run the allure server and analize the unit test and behavior features runned
- In the folder named ```features``` you can access to all the cases made in Gherkin, into that folder you can see the folder named ```steps```, in that folder you found the steps definitions of the cases maded in gherkin
- In the folder ```scripts``` you can found the logic of the robot, all the scripts to found, use or check where made the robot run without problem
- In the folder ```test``` you can found the unit test where check's if the robot dont have any problem

IMPORTANT
- The page test have one bug. I can register the same user whatever I want, that's a issue for now I dont use some bug tracker but is well know it

---
Thanks for watching my project! Follow me if you want
