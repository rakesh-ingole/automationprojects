Feature: Registration
Background:
Given user launch automation practice application
When user clicks on My Account link

@positive
Scenario: Create a New User & verify successful registration - Happy Path
When user fills "valid" registration email
|EMAIL|
|ct@gmail.com|
When user clicks create an account button
When user enters the registration details
|TITLE|FIRSTNAME |LASTNAME |EMAIL                   |PASSWORD|DATE|MONTH|YEAR|NEWSLETTER|PARTNERS|ADDRESSFIRSTNAME|ADDRESSLASTNAME|COMPANY|ADDRESS|ADDRESLINE2|CITY|STATE      |ZIP  |COUNTRY      |ADDITIONALINFO|HOMEPHONE |MOBILEPHONE|ADDRESSFORFUTUREREFERENCE|
|MR   |FIRSTNAME |LASTNAME |ct000000000001@gmail.com|test!123|30  |2    |1992|Y         |N       |ADDRESSFIRSTNAME|ADDRESSLASTNAME|COMPANY|ADDRESS|ADDRESLINE2|CITY|Connecticut|06851|United States|ADDITIONALINFO|1234567890|1234567891 |ADDRESSFORFUTURE|
Then verify the registration success
Then user sing off application

@negative
Scenario: verify invalid email address
When user fills "invalid" registration email
|EMAIL|
|ct@@gmail.com|
When user clicks create an account button
Then verify that error message as "Invalid email address."
Then application quits
