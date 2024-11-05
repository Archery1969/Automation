Feature: Login Tests

  Background: Accept cookies on the home page
    Given the user is on the storefront home page
    When the user clicks the accept all cookies button
    Then the cookie accept button should no longer be visible

  Scenario: Login with valid credentials
    Given the user is on the storefront login page
    When the user enters valid storefront credentials
    And the user clicks on the storefront login button
    Then the user is redirected to the storefront account dashboard
