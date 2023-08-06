from urllib import parse
from requests import RequestException, Session, post
from .config import CLOUDPROXY_ENDPOINT, REQUESTS_TIMEOUT


class FlareRequests(Session):
    def request(self, method, url, params=None, timeout=REQUESTS_TIMEOUT, **kwargs):
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
                    "postData": parse.urlencode(params) if params else "",
                    "maxTimeout": timeout * 1000,
                },
            )
            solution = response.json()

            if "solution" in solution:
                response.status_code = solution["solution"]["status"]
                response.headers = solution["solution"]["headers"]
                response.raw = solution["solution"]["response"]
                response.url = url
                response.cookies = solution["solution"]["cookies"]

                return response

            raise RequestException(response)
        except RequestException:
            session = post(
                CLOUDPROXY_ENDPOINT,
                json={"cmd": "sessions.destroy", "session": FLARESESSION},
            )

            raise RequestException(solution)
