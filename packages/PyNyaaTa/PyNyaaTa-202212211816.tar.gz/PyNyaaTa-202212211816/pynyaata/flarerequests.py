from io import BytesIO
from urllib import parse
from requests import RequestException, Response, Session, post
from .config import CLOUDPROXY_ENDPOINT


class FlareRequests(Session):
    def request(self, method, url, params=None, **kwargs):
        if not CLOUDPROXY_ENDPOINT:
            return super().request(method, url, params, **kwargs)

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

        post_data = {
            "cmd": f"request.{method.lower()}",
            "session": FLARESESSION,
            "url": url,
        }

        if params:
            post_data["postData"] = parse.urlencode(params)

        try:
            response = post(
                CLOUDPROXY_ENDPOINT,
                json=post_data,
            )

            solution = response.json()

            if "solution" in solution:
                resolved = Response()

                resolved.raw = BytesIO(solution["solution"]["response"].encode())
                resolved.status_code = solution["solution"]["status"]
                resolved.headers = solution["solution"]["headers"]
                resolved.url = url
                resolved.reason = solution["status"]
                resolved.cookies = solution["solution"]["cookies"]

                return resolved

            raise RequestException(response)
        except RequestException:
            session = post(
                CLOUDPROXY_ENDPOINT,
                json={"cmd": "sessions.destroy", "session": FLARESESSION},
            )

            raise RequestException(solution)
