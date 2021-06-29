## begin conversation
* greet
  - utter_greet
  - utter_menu

## combined begin with url
* greet
  - utter_greet
  - utter_menu
* begin_lead
  - utter_lead_q1
  - lead_form_p1
  - form{"name": "lead_form_p1"}
  - form{"name": null}
  - utter_lead_q3
  - utter_lead_q4
  - utter_lead_q5
* goodbye
  - utter_goodbye

<!-- ## combined begin without url

* greet
  - utter_greet
  - utter_menu
* begin_lead
  - utter_lead_q1
  - lead_form_p1
  - form{"name": "lead_form_p1"}
  - form{"name": null}
* reject
  - lead_form_p3
  - form{"name": "lead_form_p3"}
  - form{"name": null}
  - utter_lead_q3
  - utter_lead_q4
  - utter_lead_q5
* goodbye
  - utter_goodbye -->

## bot challenge
* bot_challenge
  - utter_iamabot

## New Story

* greet
    - utter_greet
    - utter_menu
* begin_lead
    - utter_lead_q1
    - lead_form_p1
    - form{"name":"lead_form_p1"}
    - slot{"requested_slot":"requirement"}
* begin_lead
    - lead_form_p1
    - slot{"requirement":"web for business"}
* begin_lead
    - lead_form_p1
    - slot{"mockup":"Wireframes"}
* bot_challenge
    - lead_form_p1
    - slot{"timeline":"within the next 3 months"}
* bot_challenge
    - lead_form_p1
    - slot{"budget":"$15000 - $25000"}
* greet
    - lead_form_p1
* bot_challenge
    - lead_form_p1
    - slot{"email":"nishtha @gmail.com3"}
* greet
    - lead_form_p1
    - form{"name":null}
    - slot{"phone":"5645567545"}
    - utter_lead_q3
    - utter_lead_q4
    - utter_lead_q5
