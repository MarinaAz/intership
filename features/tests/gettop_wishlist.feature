# Created by marinaazizbajeva at 06/04/21
Feature: Gettop Wishlist test
  # Enter feature description here

  Scenario: User can add a product to a wishlist
    Given Open Gettop page of product macbook-pro-13
    Then Add product to wishlist
    Then Verify MacBook Pro 13-inch on the page


  Scenario: User can remove a product from a Wishlist
    Given Open Gettop page of product macbook-pro-13
    Then Add product to wishlist
    When Remove product from a wishlist
    Then Verify confirmation message No products added to the wishlist


  Scenario: User has access to correct product from a wishlist
    Given Open Gettop page of product macbook-pro-13
    Then Add product to wishlist
    When Go to the product page
    Then Verify user on macbook-pro-13 page

  Scenario: User can see social logos in wishlist
    Given Open Gettop page of product macbook-pro-13
    Then Add product to wishlist
    Then Verify user can see 4 social links