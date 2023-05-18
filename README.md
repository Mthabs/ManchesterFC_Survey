ManchesterFC_Survey

Manchester FC Survey is conducted with the goal of gathering feedback and insights from thier valued supporters. The club want to understand how supporters perceive the brand, coach, and players, as this information is essential for shaping the future direction of Manchester FC.

The survey is conducted through a command-line application, which provides a user-friendly interface for the user to manage the dataset. Users are prompted to provide ratings on a scale of 1 to 10 for each category—brand, coach, and players. The application validates the input to ensure it falls within the appropriate range and format.

By collecting these ratings, the survey aims to achieve several objectives. Firstly, it seeks to assess the overall perception of Manchester FC's brand and how well it resonates with the supporters. Secondly, it aims to evaluate the coaching strategies implemented by the dedicated coaching staff and understand their impact on the team. Lastly, the survey aims to gain insights into how supporters perceive the performance of the players on the field.

The ultimate goal of the survey is to use the gathered feedback to drive continuous improvement within Manchester FC. It allows the club to identify areas of strength and areas that require attention, enabling the club to enhance the overall fan experience, develop effective coaching strategies, and ensure the team's performance aligns with the supporters' expectations.

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
