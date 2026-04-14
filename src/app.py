"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException, Response, Cookie, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, JSONResponse
import os
import json
import hashlib
import secrets
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# Load teacher credentials from JSON file
teachers_file = Path(__file__).parent / "teachers.json"
with open(teachers_file) as f:
    teachers_data = json.load(f)
teachers = {t["username"]: t for t in teachers_data["teachers"]}

# Active sessions: token -> username
active_sessions: dict[str, str] = {}


def _verify_password(username: str, password: str) -> bool:
    teacher = teachers.get(username)
    if not teacher:
        return False
    expected = hashlib.sha256((teacher["salt"] + password).encode()).hexdigest()
    return secrets.compare_digest(expected, teacher["password_hash"])


def _is_authenticated(session_token: str | None) -> bool:
    return session_token is not None and session_token in active_sessions

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
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice and play basketball with the school team",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore your creativity through painting and drawing",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
    },
    "Drama Club": {
        "description": "Act, direct, and produce plays and performances",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["ella@mergington.edu", "scarlett@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging problems and participate in math competitions",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["charlotte@mergington.edu", "henry@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


# ---------------------------------------------------------------------------
# Authentication endpoints
# ---------------------------------------------------------------------------

@app.post("/auth/login")
def login(response: Response, username: str = Form(...), password: str = Form(...)):
    """Authenticate a teacher and issue a session cookie"""
    if not _verify_password(username, password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = secrets.token_hex(32)
    active_sessions[token] = username
    response = JSONResponse(content={"message": "Logged in successfully"})
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        samesite="strict",
        max_age=3600,
    )
    return response


@app.post("/auth/logout")
def logout(response: Response, session_token: str | None = Cookie(default=None)):
    """Invalidate the current session"""
    if session_token and session_token in active_sessions:
        del active_sessions[session_token]
    response = JSONResponse(content={"message": "Logged out successfully"})
    response.delete_cookie("session_token")
    return response


@app.get("/auth/status")
def auth_status(session_token: str | None = Cookie(default=None)):
    """Return whether the current request belongs to an authenticated teacher"""
    if _is_authenticated(session_token):
        return {"authenticated": True, "username": active_sessions[session_token]}
    return {"authenticated": False}


# ---------------------------------------------------------------------------
# Activity signup / unregister (teacher-only)
# ---------------------------------------------------------------------------

@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str,
                         session_token: str | None = Cookie(default=None)):
    """Sign up a student for an activity (teacher only)"""
    if not _is_authenticated(session_token):
        raise HTTPException(status_code=401, detail="Authentication required")

    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(
            status_code=400,
            detail="Student is already signed up"
        )

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str,
                              session_token: str | None = Cookie(default=None)):
    """Unregister a student from an activity (teacher only)"""
    if not _is_authenticated(session_token):
        raise HTTPException(status_code=401, detail="Authentication required")

    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is signed up
    if email not in activity["participants"]:
        raise HTTPException(
            status_code=400,
            detail="Student is not signed up for this activity"
        )

    # Remove student
    activity["participants"].remove(email)
    return {"message": f"Unregistered {email} from {activity_name}"}
