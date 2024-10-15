from openai import OpenAI
from keyfile import key
import streamlit as st
import json
from datetime import date


today = date.today()


client = OpenAI(api_key=key)
file_path = r"C:\Users\Wylie\Documents\GitHub\TimeAI\TimeAI\events.json"

def load_events(file_path):
    with open(file_path, "r") as file:
        events = json.load(file)
        print(events)
    return events

def chat(prompt):
    prompt = prompt
    print("")

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": """You generate JSON Code, only return information
             as JSON objects with the following keys and formats:
             
             [
                {
                    "title": String,
                    "start": ISO 8601 date string,
                    "end": ISO 8601 date string,
                }
            ]
            
            You will not schedule anything between 10pm and 7am, and only schedule for future dates.
            The current date is """ + today.strftime("%B %d, %Y")},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    #print("Response: \n")
    #print(completion.choices[0].message.content)
    
    events = load_events(file_path)
    
    events.extend(json.loads(completion.choices[0].message.content))
    
    with open(file_path, "w") as file:
        json.dump(events, file, indent=4)
        
user_in = str(input("Enter A Scheduling Problem: "))
chat(user_in)
#load_events(file_path)

