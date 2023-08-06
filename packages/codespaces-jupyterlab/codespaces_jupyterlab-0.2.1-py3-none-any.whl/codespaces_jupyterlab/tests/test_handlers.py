import json


async def test_hello(jp_fetch):
    # When
    response = await jp_fetch("codespaces-jupyterlab", "hello")

    # Then
    assert response.code == 200
    payload = json.loads(response.body)
    assert payload == {
        "data": "This is /codespaces-jupyterlab/hello endpoint!"
    }