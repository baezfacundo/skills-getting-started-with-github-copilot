"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice teamwork and compete in interschool basketball matches",
        "schedule": "Tuesdays and Thursdays, 4:30 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Soccer Club": {
        "description": "Develop soccer skills through drills and friendly competitions",
        "schedule": "Wednesdays and Fridays, 3:45 PM - 5:15 PM",
        "max_participants": 18,
        "participants": ["isabella@mergington.edu", "ethan@mergington.edu"]
    },
    "Painting Workshop": {
        "description": "Explore painting techniques with acrylics, watercolor, and mixed media",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["mia@mergington.edu", "charlotte@mergington.edu"]
    },
    "School Choir": {
        "description": "Build vocal skills and perform in school and community events",
        "schedule": "Thursdays, 2:30 PM - 4:00 PM",
        "max_participants": 25,
        "participants": ["amelia@mergington.edu", "james@mergington.edu"]
    },
    "Debate Club": {
        "description": "Practice public speaking, argumentation, and competitive debate formats",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["benjamin@mergington.edu", "harper@mergington.edu"]
    },
    "Math Olympiad Prep": {
        "description": "Train for advanced problem-solving and mathematics competitions",
        "schedule": "Fridays, 2:30 PM - 4:00 PM",
        "max_participants": 12,
        "participants": ["elijah@mergington.edu", "evelyn@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Check if student is already registered
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already registered for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
