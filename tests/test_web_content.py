import pytest

@pytest.mark.parametrize("path", [("/"), ("/rules")])
def test_get(client, path):
    assert client.get(path).status_code == 200
