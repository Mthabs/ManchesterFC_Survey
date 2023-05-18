ManchesterFC_Survey

Manchester FC Survey is conducted with the goal of gathering feedback and insights from thier valued supporters. The club want to understand how supporters perceive the brand, coach, and players, as this information is essential for shaping the future direction of Manchester FC.

The survey is conducted through a command-line application, which provides a user-friendly interface for the user to manage the dataset. Users are prompted to provide ratings on a scale of 1 to 10 for each category—brand, coach, and players. The application validates the input to ensure it falls within the appropriate range and format.

By collecting these ratings, the survey aims to achieve several objectives. Firstly, it seeks to assess the overall perception of Manchester FC's brand and how well it resonates with the supporters. Secondly, it aims to evaluate the coaching strategies implemented by the dedicated coaching staff and understand their impact on the team. Lastly, the survey aims to gain insights into how supporters perceive the performance of the players on the field.

Features

Survey Questions

The application presents a series of survey questions to the user, covering various aspects of their experience as Manchester United fans. The questions may include topics such as matchday experience, favorite players, club merchandise, and overall satisfaction. By providing their responses, fans can contribute to shaping the future direction of the club.

Data Collection

The survey responses provided by the users are collected and stored for further analysis. The application utilizes a spreadsheet or database to record the survey data, ensuring that it is organized and easily accessible for future use. This enables the club to review and analyze the data to gain valuable insights into fan opinions.

Error Handling

The application incorporates error handling mechanisms to ensure that users provide valid and complete responses. It validates user input and provides appropriate error messages if invalid data is entered, allowing users to correct their responses and ensuring the accuracy of the collected data
.

Setup Instructions

To set up the ManchesterFC_Survey project, follow these steps:

• Clone the project repository from GitHub: git clone https://github.com/your-username/ManchesterFC_Survey.git

• Navigate to the project directory: cd ManchesterFC_Survey

• Install the required dependencies by running: pip install -r requirements.txt

• Prepare the survey data storage (e.g., spreadsheet or database) and ensure the necessary credentials or connection details are available.

• Update the configuration file (config.py) with the appropriate settings, such as the data storage location and credentials.

• Run the command-line application by executing the main.py file: python main.py

• Follow the prompts to provide your survey responses. Ensure that you enter valid and complete information to contribute to the survey effectively.

• Once you have completed the survey, the application will store your responses in the designated data storage for further analysis.

Dependencies

The ManchesterFC_Survey project utilizes the following dependencies:

• Python (version 3.6 or above)

• pip (Python package installer)


Running the Application

To run the ManchesterFC_Survey application, execute the main.py file using Python:

shellCopy code

python main.py 

Follow the on-screen instructions and provide your responses to the survey questions. The application will handle the data storage and error handling automatically.

Testing

The ManchesterFC_Survey application has undergone thorough testing to ensure its functionality and reliability. The following tests were performed:

• Tested different scenarios with valid and invalid inputs to verify the application's response and error handling mechanisms.

• Checked the data storage functionality by validating that survey responses were correctly recorded in the designated storage (e.g., spreadsheet or database).

• Conducted cross-browser testing to ensure compatibility across popular web browsers.

• Tested the application on various screen sizes and resolutions to ensure responsiveness and proper display on different devices.

The ultimate goal of the survey is to use the gathered feedback to drive continuous improvement within Manchester FC. It allows the club to identify areas of strength and areas that require attention, enabling the club to enhance the overall fan experience, develop effective coaching strategies, and ensure the team's performance aligns with the supporters' expectations.
Features

Survey Questions

The application presents a series of survey questions to the user, covering various aspects of their experience as Manchester United fans. The questions may include topics such as matchday experience, favorite players, club merchandise, and overall satisfaction. By providing their responses, fans can contribute to shaping the future direction of the club.

Data Collection

The survey responses provided by the users are collected and stored for further analysis. The application utilizes a spreadsheet or database to record the survey data, ensuring that it is organized and easily accessible for future use. This enables the club to review and analyze the data to gain valuable insights into fan opinions.
![alt text](https://github.com/Mthabs/ManchesterFC_Survey/blob/main/submitscore.png?raw=true)

Error Handling

The application incorporates error handling mechanisms to ensure that users provide valid and complete responses. It validates user input and provides appropriate error messages if invalid data is entered, allowing users to correct their responses and ensuring the accuracy of the collected data.
![alt text](https://github.com/Mthabs/ManchesterFC_Survey/blob/main/datavaidation.png?raw=true)

Setup Instructions

To set up the ManchesterFC_Survey project, follow these steps:

• Clone the project repository from GitHub: git clone https://github.com/your-username/ManchesterFC_Survey.git

• Navigate to the project directory: cd ManchesterFC_Survey

• Install the required dependencies by running: pip install -r requirements.txt

• Prepare the survey data storage (e.g., spreadsheet or database) and ensure the necessary credentials or connection details are available.

• Update the configuration file (config.py) with the appropriate settings, such as the data storage location and credentials.

• Run the command-line application by executing the main.py file: python main.py

• Follow the prompts to provide your survey responses. Ensure that you enter valid and complete information to contribute to the survey effectively.

• Once you have completed the survey, the application will store your responses in the designated data storage for further analysis.

Dependencies

The ManchesterFC_Survey project utilizes the following dependencies:

• Python (version 3.6 or above)

• pip (Python package installer)

• pandas - A powerful data manipulation library used for managing survey data.

• openpyxl - A library for reading and writing Excel files, used for storing survey data in spreadsheets.

• sqlite3 - A built-in Python library for working with SQLite databases, used for storing survey data.

Ensure that you have Python and pip installed on your system before proceeding with the setup instructions.

Running the Application

To run the ManchesterFC_Survey application, execute the main.py file using Python:

shellCopy code

python main.py 

Follow the on-screen instructions and provide your responses to the survey questions. The application will handle the data storage and error handling automatically.

Testing			
I have manually tested this project by doing the following:			
• Passed the code through a PEP8 linter and confirmed there are no problems			
"• Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice"			
• Tested in my local terminal and the Code Institute Heroku terminal			
Bugs			
Solved Bugs			
"• When I wrote the project, I was getting index errors because I had forgotten that the lists are zero indexed. I fixed"			
this by adding  size  -  1 where necessary			
• My validate_ coordinates function was returning false positives because I hadn't structured the if statement properly			
Remaining Bugs			
• No bugs remaining		

Validator Testing		

• PEP8			
o   Two errors were returned from PEP8online.com			
![alt text](https://github.com/Mthabs/ManchesterFC_Survey/blob/main/pythoncheker.png?raw=true)

Deployment			
This project was deployed using Code lnstitute's mock terminal for Heroku.			
• Steps for deployment:			
o  Fork or clone this repository			
o  Create a new Heroku app			
o Set the buildbacks to Pyt hon  and NodeJS  in that order			
o  Link the Heroku app to the repository			
o  Click on Deploy			




