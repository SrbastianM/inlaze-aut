Feature: User Registration

    The form must allow you to register a user with name, email and password.

    Scenario: The registration for an user in a web
        Given the user is on the web page
        When the user select the "Sign Up" option
        And the user can see the "Sign Up" page
        And the user put the registration details like: <fullName>, <email>, <password>,<repeatYourPassword>
        And the user select the "Sign Up" button
        Then the user is register on the web page

    Example:
            | fullName | email                   | password   | repeatYourPassword |
            | Jhon Doe | inlaze-user@yopmail.com | T123@mails | T123@mails         |

    Scenario: The user already exist in the web page
        Given the user is on the web page
        When the user select the "Sign Up" option
        And the user can see the "Sign Up" page
        And the user put the registration details like: <fullName>, <email>, <password>,<repeatYourPassword>
        And the user select the "Sign Up" button
        Then the user is register on the web page

    Example:
            | full name | email         | password | repeat your password |
            | Jhon Doe  | jhon@mail.com |          | 123A@asdf            |