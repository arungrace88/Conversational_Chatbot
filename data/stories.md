## search capital happy 
* greet
  - utter_greet
* search_capital{"GPE":"India"}
  - action_capital_search
  - slot{"capital":"London"}
* goodbye
  - utter_goodbye

## search capital happy 
* greet
  - utter_greet
* greet
  - utter_greet
* search_capital{"GPE":"India"}
  - action_capital_search
  - slot{"capital":"London"}
* goodbye
  - utter_goodbye

## search capital without country
* greet
  - utter_greet
* search_capital
  - utter_ask_country
* country
  - action_capital_search
  - slot{"capital":"London"}
* goodbye
  - utter_goodbye

## search capital without country happy path
* greet
  - utter_greet
* greet
  - utter_greet
* search_capital
  - utter_ask_country
* country
  - action_capital_search
  - slot{"capital":"London"}
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## New Story

* greet
    - utter_greet
