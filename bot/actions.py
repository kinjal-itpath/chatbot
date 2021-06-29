# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Dict, Text, Any, List, Union, Optional
from email_validator import validate_email, EmailNotValidError
import re
from user import user
from rasa_sdk import Tracker
from rasa_sdk.forms import FormValidationAction 
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from db_sqlite import insert_data
import sqlite3
import requests

class LeadFormFirstPart(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "lead_form_p1"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["requirement", "mockup", "timeline", "budget", "name", "email", "phone",]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {


            # "application": [
            #     self.from_text(),
            # ],
            "requirement": [
                self.from_text(),
            ],
            "mockup": [
                self.from_text(),
            ],
            "timeline": [
                self.from_text(),
            ],
            "budget": [
                self.from_text(),
            ],
            "name": [
                self.from_text(),
            ],
            "email": [  
                self.from_text(),
            ],
            "phone": [
                self.from_text(),
            ],


        }
    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text,Any], 
    ) -> Dict[Text, Any]:
      if len(slot_value) <= 2 :
        dispatcher.utter_template("utter_wrong_name",tracker)
        return {"name": None}
      else:
          return {"name": slot_value}
    
    def validate_email(
    self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text,Any],     
    ) -> Dict[Text, Any]:
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if (re.search(regex, slot_value)) == None:
            dispatcher.utter_template("utter_wrong_email",tracker)
            return {"email": None}
        else:
            return {"email": slot_value}
      
     
    def validate_phone(
        self,
        slot_value: Any,    
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text,Any],
    ) -> Dict[Text, Any]:

         if len(slot_value) != 10 :
             dispatcher.utter_template("utter_wrong_phone",tracker)
             return {"phone": None}
         else:
             return {"phone": slot_value}
            
    
    

    def insert_data(requirement, mockup,  timeline, budget, name, email, phone):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        print("Database created and Successfully Connected to SQLite")
        cursor.execute('''INSERT INTO d3(requirement, mockup, timeline, budget, name, email, phone) VALUES ( ?, ?, ?, ?, ?, ?,?)''', (requirement, mockup,  timeline, budget, name, email, phone))
        print("Table created successfully........")
        # conn.commit()
        conn.close()



    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        
        

        #app = tracker.get_slot("application")
        res = tracker.get_slot("requirement")
        mok = tracker.get_slot("mockup")
        time = tracker.get_slot("timeline")
        bud = tracker.get_slot("budget")
        nam = tracker.get_slot("name")
        ema= tracker.get_slot("email")
        no = tracker.get_slot("phone")
        SUBJECT = "IT Path Solutions" 
        TEXT =f"""\0

    
         requirement: {res}
        - mockup: {mok} 
        - timeline: {time}
        - budget: {bud}   
        - name: {nam}
        - email: {ema}
        - phone: {no}"""

        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        user(ema,message)
        dispatcher.utter_message("Thank you so much for showing your intrest in work with us") 
        data = { "res" : tracker.get_slot("requirement") , "mok" : tracker.get_slot("mockup"),"time" : tracker.get_slot("timeline"),"bud" :  tracker.get_slot("budget"),"nam" : tracker.get_slot("name"),"ema"  : tracker.get_slot("email"),"no" : tracker.get_slot("phone") }
        url = "http://127.0.0.1:5000/"
        r = requests.get(url = url, params = data)
        print(r)
        #insert_data(tracker.get_slot("requirement"),tracker.get_slot("mockup"),tracker.get_slot("timeline"),tracker.get_slot("budget"),tracker.get_slot("name"),tracker.get_slot("email"),tracker.get_slot("phone"))
        return []

    

# class LeadFormSecondPart(FormAction):
#     """Example of a custom form action"""

#     def name(self) -> Text:
#         """Unique identifier of the form"""

#         return "lead_form_p2"

#     @staticmethods
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#         return ["url"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         """A dictionary to map required slots to
#             - an extracted entity
#             - intent: value pairs
#             - a whole message
#             or a list of them, where a first match will be picked"""
#         return {
#             "url": [
#                 self.from_text(),
#             ],      
#         }

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         """Define what the form has to do
#             after all required slots are filled"""
#         insert_data(tracker.get_slot("url"))
#         return []


# class LeadFormThirdPart(FormAction):
#     """Example of a custom form action"""

#     def name(self) -> Text:
#         """Unique identifier of the form"""

#         return "lead_form_p3"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#         return ["timeline", "budget", "name", "email", "phone"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         """A dictionary to map required slots to
#             - an extracted entity
#             - intent: value pairs
#             - a whole message
#             or a list of them, where a first match will be picked"""
#         return {
#             "timeline": [
#                 self.from_text(),
#             ],
#             "budget": [
#                 self.from_text(),
#             ],
#             "name": [
#                 self.from_text(),
#             ],
#             "email": [
#                 self.from_text(),
#             ],
#             "phone": [
#                 self.from_text(),
#             ],
#         }

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         """Define what the form has to do
#             after all required slots are filled"""

#         # utter submit template
#         dispatcher.utter_template("utter_lead_q2", tracker)
#         insert_data(tracker.get_slot("timeline"),tracker.get_slot("budget"),tracker.get_slot("name",tracker.get_slot("email"),tracker.get_slot("phone"))
#         return []
