from ast import Pass
from tkinter import N
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from datetime import datetime
from actions.time_handle import *

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_id = (tracker.current_state())["sender_id"]

        sexual = tracker.get_slot("sexual")
        utterself = "em"

        if sexual is None:
            sexual = "anh chị"

        dispatcher.utter_message(response = "utter_greet", sexual= sexual)
        dispatcher.utter_message(response = "utter_ask_name", sexual= sexual, utterself=utterself)

        return [SlotSet("utterself", utterself)]
class ActionAskName(Action):

    def name(self) -> Text:
        return "action_ask_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_id = (tracker.current_state())["sender_id"]

        name = tracker.get_slot("name")
        sexual_temp = tracker.get_slot("sexual")

        if name is None:
            dispatcher.utter_message(response = "utter_ask_name")

        lst_check = ["tôi", "tớ", "mình"]

        if sexual_temp is None or sexual_temp in lst_check:
            sexual = "bạn"
            utterself = "mình"           
        else:
            sexual = sexual_temp
            utterself = "em"
        
        return [SlotSet("sexual", sexual), SlotSet("utterself", utterself)]

class ActionGreetName(Action):
    def name(self) -> Text:
        return "action_greet_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_id = (tracker.current_state())["sender_id"]

        sexual = tracker.get_slot("sexual")
        name = tracker.get_slot("name")
        print("sexual", sexual)
        print("name", name)
        if name is not None:
            dispatcher.utter_message(response = "utter_greet_name")
            dispatcher.utter_message(response = "utter_ask_service")
        return []

class ActionAskService(Action):
    def name(self) -> Text:
        return "action_ask_service"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_id = (tracker.current_state())["sender_id"]

        sexual = tracker.get_slot("sexual")
        service = tracker.get_slot("service")
        print("sexual", sexual)
        print("service", service)
        if service is None:
            dispatcher.utter_message(response = "utter_ask_service")
        else:
            dispatcher.utter_message(response = "utter_ask_timeday")
        return []

class ActionAskTimeDay(Action):

    def name(self) -> Text:
        return "action_ask_timeday"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_id = (tracker.current_state())["sender_id"]

        Date = datetime.now()
        str_year = tracker.get_slot("year")
        str_month = tracker.get_slot("month")
        str_week = tracker.get_slot("week")
        str_weekday = tracker.get_slot("weekday")
        str_day = tracker.get_slot("day")
        str_time = tracker.get_slot("time")

        if str_year is not None:
            Date = year_format(year=str_year, Date=Date) 
        if str_month is not None:
            Date = month_format(month=str_month, Date=Date)
        if str_week is not None:
            Date = week_format(week=str_week, Date=Date)
        if str_weekday is not None:
            Date = weekday_format(weekday=str_weekday, Date=Date)
        if str_day is not None:
            Date = day_format(day=str_day, Date=Date)
        if str_time is not None:
            Date = time_format(time=str_time, Date=Date)
        else:
            Date = time_format(time="7 giờ", Date=Date)
           
        if Date == datetime.now():
            dispatcher.utter_message(response = "utter_ask_timeday")

        else:
            time = str(Date.time().replace(microsecond=0))
            day = str(Date.day)
            month = str(Date.month)
            year = str(Date.year)
            print(time, "-", day, "-", month, "-", year)
            sexual = tracker.get_slot("sexual")
            service = tracker.get_slot("service")
            dispatcher.utter_message(response = "utter_confirm", sexual=sexual, service=service, time=time, day=day, month=month, year=year)

        return [SlotSet("time", time), SlotSet("day", day), SlotSet("month", month), SlotSet("year", year)]

class ActionConfirm(Action):

    def name(self) -> Text:
        return "action_confirm"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_id = (tracker.current_state())["sender_id"]

        sexual = tracker.get_slot("sexual")
        name = tracker.get_slot("name")
        if name is None:
            dispatcher.utter_message(response = "utter_ask_name")
        
        service = tracker.get_slot("service")
        time = tracker.get_slot("time")
        day =tracker.get_slot("day")
        month = tracker.get_slot("month")
        year = tracker.get_slot("year")
        
        if name is not None and service is not None and time is not None:
            dispatcher.utter_message(response = "utter_waitting")
            dispatcher.utter_message(response = "utter_thank")
            hour, minute, _ = time.split(":")
            Date = datetime(year=year, month=month, day=day, hour=hour, minute=minute)
            print(str(Date))

        # dispatcher.utter_message(response = "utter_greet_name", name = name, sexual = sexual)
        
        return []