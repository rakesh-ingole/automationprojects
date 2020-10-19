Feature: AutomationPractice.com application launch

  Scenario: logo presence on AutomationPractice home page
     Given I launch Chrome browser
      When I open automation practice home page
      Then I verify that the logo present on page
