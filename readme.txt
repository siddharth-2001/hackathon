######################################## Hackathon Submission ########################################
                                  by: Siddharth Bharmoria IT SG19845

I have tested each and every part of both the phases and everything seems to work. If you run into 
errors, you might be passing wrong primary keys.
Also due to the Heroku policies, it is possible that the database gets wiped out in 24 hours after deployment
because of the use of sqlite databse.

To make things easier I have added a check_dictionaries.txt file which contains sample dictionaries that can be used
to test the apis.

Some features use sending of primary keys over the links that were not originally specified in the hackathon pdf
these are:
     changePassword
     deleteUser
     deleteProduct

So to run them correctly you need to specify the id of the object you want to edit
like:
    changePassword/(id)
    deleteUser/(id)

Also the user product list displays the id of the products added
superuser account
username = siddh
password = password123