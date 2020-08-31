# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from restcountries import RestCountryApiV2 as rapi
#
class ActionCapitalSearch(Action):
#
    def name(self) -> Text:
        return "action_capital_search"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        country = tracker.get_slot("GPE")
       
        
        country_list = rapi.get_countries_by_name(country)
        capital = country_list[0].capital
        dispatcher.utter_message(text="Sure. The capital city is {}".format(capital))

        return [SlotSet("capital",capital)]
