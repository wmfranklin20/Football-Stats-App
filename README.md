# Football-Stats-App
Repository to host files related to tracking and analysis of football stats in the English Premier League. 


Workflow Goal:

- Python (BS4) to get data from FBRef sites for each team
- Python to interpret and organize data pulled for each team.
- HTML/CSS/JS to create web app to view stats by team, or compare league and player stats.

Current Workflow:

- Requests main Premier League page on FBREf
- Function (pullTable) to select each table on the page
- Function (rowData) to pull stats for each team by row of the table
- Construction of objects for each team (Team object)
- Overwrite object variables using stored table data by searching corresponding row for each team and calling function to pull from specific cell from each row