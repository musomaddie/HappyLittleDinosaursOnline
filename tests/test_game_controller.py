import pytest

@pytest.mark.parametrize("path",
                         [("/game/"), ("/game/start"), ("/game/join")])
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