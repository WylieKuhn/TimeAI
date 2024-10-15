from streamlit_calendar import calendar
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import os
import json
from pages.prompt import chat

refresh = st_autorefresh(interval=2000, limit=None)

events_file = r"C:\Users\Wylie\Documents\GitHub\TimeAI\TimeAI\events.json"

def load_events():
    if not os.path.exists(events_file) or os.stat(events_file).st_size == 0:
        return []
    with open(events_file, 'r') as f:
        return json.load(f)
    


calendar_options = {
    "editable": "true",
    "selectable": "true",
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "01:00:00",
    "slotMaxTime": "23:00:00",
    "initialView": "dayGridMonth"
}
calendar_events = load_events()
custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""

calendar = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)
st.write(calendar)

user_input = st.text_area("Enter A Scheduling Problem")

if st.button("Submit"):
    if len(user_input) == 0:
        st.warning("Enter A Prompt")
    else:
        chat(user_input)
    