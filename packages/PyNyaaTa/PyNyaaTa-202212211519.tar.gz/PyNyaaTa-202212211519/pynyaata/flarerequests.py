from urllib import parse
from requests import RequestException, Session, post
from .config import CLOUDPROXY_ENDPOINT, REQUESTS_TIMEOUT


class FlareRequests(Session):
    def request(self, method, url, params, timeout=REQUESTS_TIMEOUT, **kwargs):
        if not CLOUDPROXY_ENDPOINT:
            return super().request(method, url, params, timeout=timeout, **kwargs)

        sessions = post(CLOUDPROXY_ENDPOINT, json={"cmd": "sessions.list"}).json()

        if "sessions" in sessions and len(sessions["sessions"]) > 0:
            FLARESESSION = sessions["sessions"][0]
        else:
            response = post(CLOUDPROXY_ENDPOINT, json={"cmd": "sessions.create"})
            session = response.json()

            if "session" in session:
                FLARESESSION = session["session"]
            else:
                raise RequestException(response)

        try:
            response = post(
                CLOUDPROXY_ENDPOINT,
                json={
                    "cmd": f"request.{method.lower()}",
                    "session": FLARESESSION,
                    "url": url,
                    "postData": parse.urlencode(params),
                    "maxTimeout": timeout,
                },
            )
            solution = response.json()

            if "solution" in solution:
                response.cookies = solution["solution"]["cookies"]
                response.headers = solution["solution"]["headers"]
                response.text = solution["solution"]["response"]

                return response

            raise RequestException(response)
        except RequestException:
            session = post(
                CLOUDPROXY_ENDPOINT,
                {"cmd": "sessions.destroy", "session": FLARESESSION},
            )

            raise RequestException(solution)
