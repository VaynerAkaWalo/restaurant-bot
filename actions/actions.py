import json
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionMenu(Action):
    def name(self) -> Text:
        return "action_menu"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            with open("data/menu.json", "r", encoding="utf-8") as file:
                menu_data = json.load(file)
                menu_items = menu_data.get("items", [])

                menu_text = "\n".join([f"- {item['name']}: {item['price']} zł" for item in menu_items])

                dispatcher.utter_message(text=f"W naszym menu mamy:\n{menu_text}")
        except Exception as e:
            dispatcher.utter_message(text="Podczas wczytywania menu wystąpil błąd")

        return []

class ActionOpenHours(Action):
    def name(self) -> Text:
        return "action_open_hours"

    def open_time_at_day(self, item) -> Text:
        start = item['open']
        end = item['close']

        if  start == end:
            return "Zamknięte"
        return f"{start}-{end}"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            with open("data/opening_hours.json", "r", encoding="utf-8") as file:
                open_hours = json.load(file)
                open_hours = open_hours.get("items", {})

                open_hours = "\n".join([f"- {day}: {self.open_time_at_day(hours)}" for day, hours in open_hours.items()])

                dispatcher.utter_message(text=f"Godziny otwarcia:\n{open_hours}")
        except Exception as e:
            dispatcher.utter_message(text="Podczas wczytywania godzin pracy wystąpil błąd")

        return []

