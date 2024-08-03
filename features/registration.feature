Feature: User Registration

    The form must allow you to register a user with name, email and password.

    Background:
        Given the user is on the web page
        When the user select the "Sign Up" option
        And the user can see the "Sign Up" page

    Scenario Outline: The registration for an user in a web
        When the user put the registration details like: <fullName>, <email>, <password>,<repeatYourPassword>
        And the user select the "Sign Up" button
        Then the user is register on the web page

        Examples:
            | fullName | email                   | password   | repeatYourPassword |
            | Jhon Doe | inlaze-user@yopmail.com | T123@mails | T123@mails         |

    Scenario Outline: The user already exist in the web page
        When the user put the registration details like: <fullName>, <email>, <password>,<repeatYourPassword>
        And the user select the "Sign Up" button
        Then the user should see a message indicating the user already exists
        And the user cannot register with the same details again: <fullName>, <email>, <password>,<repeatYourPassword>

        Examples:
            | fullName | email         | password   | repeatYourPassword |
            | Jhon Doe | jhon@mail.com | T123@mails | T123@mails         |