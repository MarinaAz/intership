# Created by marinaazizbajeva at 06/04/21
Feature: Gettop Wishlist test
  # Enter feature description here

  Scenario: User can add a product to a wishlist
    Given Open Gettop page of product macbook-pro-13
    When Verify Wishlist popup btn is clickable
    Then Add product to wishlist
    Then Verify user can see correct product