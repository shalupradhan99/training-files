Feature: :verify/checking the OrangeHRM login & logout application

  Scenario: Successful Login with valid credentials
  Given user should open the chrome browser
  When  user should enter url in browser
  When  user should Navigate login page
  And Enter Username & password in edit box
  And click on login button
  Then display login Successfullly
  Then user should close browser
