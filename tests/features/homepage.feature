Feature: homepage
    A listing of entries from the learning journal in reverse chronological order.

Scenario: The homepage lists entries for anonymous users
    Given an anonymous user
    And a list of three entries
    When the user visits the homepage
    Then they see a list of three entries


Scenario: The homepage displays relevant buttons for anonymous users
    Given an anonymous user
    When the user visits the homepage
    Then they will see a login button
    And they will not see a logout button
    And they will not see an add button


Scenario: The homepage allows anonymous users to view the detail page
    Given an anonymous user
    And a list of three entries
    When the user clicks on an entry
    Then they will see the detail page


Scenario: The detail page displays relevant buttons for anonymous users
    Given an anonymous user
    And a list of three entries
    When the user clicks on an entry
    Then they will see a login button
    And they will not see a logout button
    And they will not see an edit button
    And they will not see an add button


Scenario: The homepage displays relevant buttons for authorized users
    Given an authorized user
    When the user visits the homepage
    Then they will see a logout button
    And they will see an add button


# Scenario: The detail page displays relevant buttons for authorized users
#     Given an authorized user
#     And a list of three entries
#     When the user clicks on an entry
#     Then they will not see a login button
#     And they will see a logout button
#     And they will see an edit button
#     And they will see an add button

Scenario: An authorized user can edit an entry
    Given an authorized user
    And a list of three entries
    When the user visits the edit page
    And the user edits an entry
    # Then the the detail page will change
