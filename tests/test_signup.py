import src.app as app_module


def test_signup_for_activity_adds_participant(client):
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "newstudent@mergington.edu"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Signed up newstudent@mergington.edu for Chess Club"
    }
    assert "newstudent@mergington.edu" in app_module.activities["Chess Club"]["participants"]


def test_signup_for_unknown_activity_returns_not_found(client):
    response = client.post(
        "/activities/Unknown Club/signup",
        params={"email": "newstudent@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_for_activity_rejects_duplicate_participant(client):
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Student already registered for this activity"
    }


def test_unregister_from_activity_removes_participant(client):
    response = client.delete(
        "/activities/Chess Club/participants",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Removed michael@mergington.edu from Chess Club"
    }
    assert "michael@mergington.edu" not in app_module.activities["Chess Club"]["participants"]


def test_unregister_from_unknown_activity_returns_not_found(client):
    response = client.delete(
        "/activities/Unknown Club/participants",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_missing_participant_returns_not_found(client):
    response = client.delete(
        "/activities/Chess Club/participants",
        params={"email": "absent@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Student not registered for this activity"
    }