Feature: Login Succesfully

    Before the registration of an user, login into aplication

    Background:
        Given the user is on the web page

    Scenario Outline: Login Succesfully
        When the user put the login details like: <email>, <password>
        And the user select the "Sign In" button
        And the user is logged into the aplication
        Then the user logout the aplication

        Examples:
            | email                   | password   |
            | inlaze-user@yopmail.com | T123@mails |

    Scenario Outline: Login Unsuccessfuly
        When the user put wrong login details: <email>, <password>
        And the user select the "Sign In" button
        Then the user see "User not found" message

        Examples:
            | email            | password   |
            | pruebas@mail.com | T233@mails |