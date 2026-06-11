"""Acceptance tests for the note search feature."""


def test_search_matches_title(client, app):
    app.notes.clear()
    app.notes.append({"title": "Hello world", "body": "some body"})
    app.notes.append({"title": "Unrelated", "body": "other"})
    r = client.get("/?q=hello")
    assert r.status_code == 200
    assert b"Hello world" in r.data
    assert b"Unrelated" not in r.data


def test_search_matches_body(client, app):
    app.notes.clear()
    app.notes.append({"title": "Note A", "body": "hello in the body"})
    app.notes.append({"title": "Note B", "body": "nothing here"})
    r = client.get("/?q=hello")
    assert r.status_code == 200
    assert b"Note A" in r.data
    assert b"Note B" not in r.data


def test_empty_search_returns_all(client, app):
    app.notes.clear()
    app.notes.extend([
        {"title": "Alpha", "body": "first"},
        {"title": "Beta", "body": "second"},
    ])
    r = client.get("/?q=")
    assert r.status_code == 200
    assert b"Alpha" in r.data
    assert b"Beta" in r.data


def test_no_match_shows_message(client, app):
    app.notes.clear()
    app.notes.append({"title": "Something", "body": "content"})
    r = client.get("/?q=zzznomatch")
    assert r.status_code == 200
    assert b"No notes found" in r.data


def test_search_input_stays_populated(client, app):
    app.notes.clear()
    r = client.get("/?q=hello")
    assert b"hello" in r.data  # input value attribute contains the query


def test_search_is_case_insensitive(client, app):
    app.notes.clear()
    app.notes.append({"title": "HELLO", "body": "world"})
    r = client.get("/?q=hello")
    assert r.status_code == 200
    assert b"HELLO" in r.data
