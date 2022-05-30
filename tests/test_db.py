import sqlite3
import pytest

from game.db import get_db, add_room_id, get_all_room_ids


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute("SELECT 1")

    assert "closed" in str(e.value)


def test_init_db(runner, monkeypatch):
    class Recorder:
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr("game.db.init_db", fake_init_db)
    result = runner.invoke(args=["init-db"])
    assert "Initialized" in result.output
    assert Recorder.called


def test_add_room_id(app):
    r_id = "ABCDEF"
    with app.app_context():
        add_room_id(r_id)
        expected_results = get_db().execute(
            """SELECT room_id FROM room_ids""").fetchall()

    assert len(expected_results) == 1
    assert expected_results[0]["room_id"] == r_id


def test_get_all_room_ids(app):
    with app.app_context():
        results_none = get_all_room_ids()
        add_room_id("ABCDEF")
        results_one = get_all_room_ids()
        add_room_id("GHIJKL")
        results_two = get_all_room_ids()

    assert len(results_none) == 0
    assert len(results_one) == 1
    assert "ABCDEF" in results_one
    assert len(results_two) == 2
    assert "ABCDEF" in results_two
    assert "GHIJKL" in results_two