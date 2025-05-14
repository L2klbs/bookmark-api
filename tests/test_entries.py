import sys
import os
import asyncio

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.main import app
from app.db import engine
from fastapi.testclient import TestClient
client = TestClient(app)

def test_create_entry_minimal():
    response = client.post(
        "/entry",
        data={"title": "My Comic"}
    )
    assert response.status_code == 200
    json = response.json()
    assert json["title"] == "My Comic"

def test_create_entry_missing_title():
    response = client.post(
        "/entry",
        data={}  # Missing required field
    )
    assert response.status_code == 422

# def test_list_entries():
#     # Create one entry first
#     client.post("/entry", data={"title": "Test Entry"})

#     # Now check list
#     response = client.get("/entries")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
#     assert any(entry["title"] == "Test Entry" for entry in response.json())

# def test_update_entry():
#     # Step 1: Create
#     client.post("/entry", data={"title": "Original"})

#     # Step 2: Get the entry ID
#     entries = client.get("/entries").json()
#     entry_id = entries[-1]["id"]

#     # Step 3: Update it
#     response = client.put(f"/entry/{entry_id}", data={"title": "Updated Title"})
#     assert response.status_code == 200
#     assert "Updated Title" in response.json()["title"]

# def test_delete_entry():
#     # Step 1: Create
#     client.post("/entry", data={"title": "To Delete"})

#     # Step 2: Get ID
#     entries = client.get("/entries").json()
#     entry_id = entries[-1]["id"]

#     # Step 3: Delete
#     delete_resp = client.delete(f"/entry/{entry_id}")
#     assert delete_resp.status_code == 200
#     assert "deleted" in delete_resp.json()["message"].lower()

#     # Step 4: Confirm it's gone
#     entries = client.get("/entries").json()
#     assert not any(e["id"] == entry_id for e in entries)