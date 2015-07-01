Feature: Homepage
    A listing of entries from the learning journal in reverse chronological order.

Scenario: The Homepage lists entires for anonymous users
    Given an anonymous user
    And a list od three entires
    When the user visits the Homepage
    Then they see a list of three entries
