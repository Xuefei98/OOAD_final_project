# OOAD_final_project
### Project Title:
 Wheel and Reel

### Team Members:
* Srihaasa Pidikiti
* Xuefei Sun
* Alexander Louie

### Packages need to be installed:
1. Python 3.7.3
2. Flask 1.1.1
3. pymongo
4. dnspython

### Overview:
Due to COVID-19, there has been a sharp increase in preference for drive-in theatres as opposed to traditional theatres. But there is no one particular website to search for the shows currently being played in all the nearby drive ins. To meet this new onset of demand a one place website for ticket booking at drive ins would be needed. We plan to design such a drive in specific websites catering to the drive in movie goers. This is a user specific website intended to provide a list of shows based on preset preferences upon signup. Our end system would focus on the following user preferences majorly-location (how far the user prefers to drive), genre of movies, ticket cost, food and drinks availability at the theater. These preferences can be updated anytime by the user. Once signed in, the user is provided with a list of shows playing based on their preferences. Users can choose from this list and go ahead for checkout. When a user purchases a ticket they will also be provided with an option to include food and drinks add-ons. Payment can be done using either debit card or credit card. The user can cancel their ticket purchase or view the purchased ticket in their profile dashboard’s transaction history. 

### Assumptions:
1. Maximum Distance of the theater is calculated from the Boulder city center.
2. List of genres that can be chosen are - Action, Comedy, Drama, Fantasy, Horror and Romance.
3. Movies, Shows and Theaters data are simulated and do not represent any original references.
4. Validity check for credit and debit card numbers.
5. Theaters cook food based on the requested demand by the users. There will not be any inventory shortage.
### Instructions to run the application:
1. Run controller.py class. This starts flask server on localhost:5000 and renders corresponding html pages as you navigate the web app.
2. client.py can also be used to test all the API end points.

