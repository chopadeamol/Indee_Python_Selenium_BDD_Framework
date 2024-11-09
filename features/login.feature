Feature:Login functionality
  @Login
  Scenario:Sign in to the platform
    Given I got navigated to the Indee login page
    When I enter valid access code
    And Click on sign in button and did so many actions as it is on the same page
    Then Home page of the Indee website should display