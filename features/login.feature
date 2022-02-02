Feature: Validate Login Feature

    Background:
        Given launch the browser
        When open the Pijar website
        Then the website has been opened
        Then click menu login


    Scenario: Login with valid credential
        And input the username "liamikha1209@gmail.com" and password "lia12345"
        And click th login button