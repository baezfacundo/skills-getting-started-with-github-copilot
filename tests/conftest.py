from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


SEED_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    app_module.activities.clear()
    app_module.activities.update(deepcopy(SEED_ACTIVITIES))
    yield
    app_module.activities.clear()
    app_module.activities.update(deepcopy(SEED_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app_module.app)