def test_hello(client):
  r = client.get("/hello/")
  assert r.data == b"Hello"