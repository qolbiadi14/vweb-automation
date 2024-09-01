Feature: Login functionality

  Scenario: Successful login
    Given User berada di halaman login
    When User mengisi username dengan username dan password yang benar
    And User menyelesaikan captcha
    And User menekan tombol login
    Then User masuk ke halaman dashboard