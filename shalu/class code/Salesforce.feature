 Scenario:verify/checking the BEHALogin to Salesforce



  Scenario: Successful login to Salesforce
    Given I am on the Salesforce login page
    When I enter valid credentials
    And I click on the "Login" button
    Then I should see the dashboard page
    And the "Welcome" message is displayed