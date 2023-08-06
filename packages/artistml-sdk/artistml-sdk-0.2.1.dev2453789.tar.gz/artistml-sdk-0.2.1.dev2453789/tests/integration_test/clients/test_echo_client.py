from artistml_sdk.clients import EchoClient
from artistml_sdk.gateway import echo_client

echo_client.set_endpoint(endpoint="host.docker.internal:60002")
client = EchoClient()


def test_create_greeting():
    resp = client.create_greeting("sylvan", "hello!")
    assert resp.details.id > 0
