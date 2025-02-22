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

