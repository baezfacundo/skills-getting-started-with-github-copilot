def test_get_activities_returns_seeded_data(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()

    assert "Chess Club" in payload
    assert payload["Chess Club"] == {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": [
            "michael@mergington.edu",
            "daniel@mergington.edu",
        ],
    }


def test_get_activities_returns_expected_structure(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()

    for activity in payload.values():
        assert set(activity) == {
            "description",
            "schedule",
            "max_participants",
            "participants",
        }
        assert isinstance(activity["participants"], list)


def test_root_redirects_to_static_index(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"