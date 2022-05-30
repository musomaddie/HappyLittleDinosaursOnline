import string
import pytest

from game.db import get_all_room_ids
from game.game_controller import generate_room_id, add_room_id
from unittest.mock import patch


@pytest.mark.parametrize(
    "path",
    ["/game/", "/game/start", "/game/join", "/game/waiting_room"]
)
def test_get(client, path):
    assert client.get(path).status_code == 200


@pytest.mark.parametrize(
    ("data", "location"),
    [({"new_game": "Start A New Game"}, "/game/start"),
     ({"join_game": "Join An Existing Game"}, "/game/join")]
)
def test_join_or_start_game_post(client, data, location):
    response = client.post("/game/", data=data)
    assert response.headers["Location"] == location


def test_start_new_game(client):
    response = client.post("/game/start", data={"start": "Start Game"})
    assert response.headers["Location"] == "/game/waiting_room"


def test_generate_room_id_valid_id(app):
    allowed_letters = string.ascii_uppercase
    with app.app_context():
        result = generate_room_id()
    # Have to import this here - if imported earlier it won't update value
    from game.game_controller import ROOM_ID
    assert result == ROOM_ID
    for letter in result:
        assert letter in allowed_letters


def test_generate_room_id_add_to_database(app):
    with app.app_context():
        # Set get all ids is already tested can use it to help here
        result = generate_room_id()
        all_ids = get_all_room_ids()

    assert len(all_ids) == 1
    assert result in all_ids

@patch("game.game_controller.random.choice")
def test_generate_room_id_already_in_database(random_mock, app):
    with app.app_context():
        add_room_id("ABCDEF")
        random_mock.side_effect = ["A", "B", "C", "D", "E", "F",
                                   "D", "E", "F", "G", "H", "I"]
        result = generate_room_id()
        all_ids = get_all_room_ids()

    assert len(all_ids) == 2
    assert "ABCDEF" in all_ids
    assert "DEFGHI" in all_ids
