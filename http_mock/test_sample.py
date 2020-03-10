import requests


def test_blocked_network():
    resp = requests.get("https://www.lingscars.com/")
    assert resp.text == "COOL WEBSITE"


def test_with_counter(mocked_response):

    with mocked_response(status_code=200, content="SMTH") as kinda_server:
        requests.get("https://www.some_site.com/")
        requests.get("https://www.some_other_site.com/")
        assert kinda_server.call_count == 2
        assert len(kinda_server.requests)
        assert kinda_server.requests[0].url == 'I stil want lingscars'


def test_for_urls(mocked_response):

    with mocked_response(url="https://foo.bar", status_code=200, content="CATCHED!"):
        resp = requests.get("https://www.lingscars.com/")
        assert resp.text == "BOOM! U FORGOT TO MOCK!"

        resp = requests.get("https://foo.bar/")
        assert resp.text == "CATCHED!"
