from urllib import parse
from requests import RequestException, Response, Session, post
from .config import CLOUDPROXY_ENDPOINT, REQUESTS_TIMEOUT


class FlareRequests(Session):
    def request(self, method, url, params=None, timeout=REQUESTS_TIMEOUT, **kwargs):
        if not CLOUDPROXY_ENDPOINT:
            return super().request(method, url, params, timeout=timeout, **kwargs)

        response = post(
            CLOUDPROXY_ENDPOINT,
            json={
                "cmd": f"request.{method.lower()}",
                "url": url,
                "postData": parse.urlencode(params) if params else "",
                "maxTimeout": timeout * 1000,
            },
        )
        solution = response.json()

        if "solution" in solution:
            resolved = Response()

            resolved.raw = solution["solution"]["response"]
            resolved.status_code = solution["solution"]["status"]
            resolved.headers = solution["solution"]["headers"]
            resolved.url = url
            resolved.reason = solution["status"]
            resolved.cookies = solution["solution"]["cookies"]

            return resolved

        raise RequestException(response)
