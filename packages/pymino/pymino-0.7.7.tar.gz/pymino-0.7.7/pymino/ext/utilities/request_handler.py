from .generate import *

class RequestHandler:
    """A class that handles all requests"""
    def __init__(self, bot, session: HTTPClient, proxy: Optional[str] = None):
        self.bot            = bot
        self.gg:            int = 0
        self.xyz:           str = None
        self.sid:           Optional[str] = None
        self.userId:        Optional[str] = None
        self.session:       HTTPClient = session
        self.proxy:         dict= (
            {"http": proxy, "https": proxy} if proxy is not None else None
        )
        self.ping_server()

    @ggl
    def service_url(self, url: str) -> str:
        return f"https://service.aminoapps.com/api/v1{url}"

    @property
    def basic_headers(self) -> dict:
        return {
            "USER-AGENT": "Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930V Build/NRD90M; com.narvii.amino.master/3.5.34803)",
            }
    
    @headers
    def service_headers(self) -> dict:
        return {
            "NDCLANG": "en",
            "ACCEPT-LANGUAGE": "en-US",
            "USER-AGENT": "Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930V Build/NRD90M; com.narvii.amino.master/3.5.34803)",
            "HOST": "service.aminoapps.com",
            "CONNECTION": "Keep-Alive",
            "ACCEPT-ENCODING": "gzip",
            "NDCAUTH": f"sid={self.sid}",
            "AUID": self.userId,
            }

    @request
    def handler(
        self,
        method: str,
        url: str,
        data: Union[dict, bytes, None] = None,
        content_type: Optional[str] = None
        ) -> dict:

        url, headers, data = self.service_handler(url, data, content_type)

        data_map = {True: {"CONTENT-TYPE": "application/octet-stream"}, False: {}}
        headers.update(data_map.get(all([method == "POST", data is None]), {}))

        request_methods = {
            "GET": self.session.get,
            "POST": self.session.post,
            "DELETE": self.session.delete,
            }

        try:
            response: HTTPResponse = request_methods[method](
                url, data=data, headers=headers, proxies=self.proxy
            )
        except (
            ConnectionError,
            ReadTimeout,
            SSLError,
            ProxyError,
            ConnectTimeout,
        ):
            self.handler(method, url, data, content_type)

        if response.status_code != 200:
            with suppress(Exception):
                response_json: dict = loads(response.text)
                # TODO: Handle exceptions.
                if response_json.get("api:statuscode") == 105:
                    return self.bot.run(self.email, self.password)

            raise Exception(response.text)

        return loads(response.text)

    def service_handler(
        self,
        url: str,
        data: Union[dict, bytes, None] = None,
        content_type: Optional[str] = None
        ) -> Tuple[str, dict, Union[dict, bytes, None]]:

        service_url = self.service_url(url)
        headers = {"NDCDEVICEID": device_id()}
        header_mapping = {
            True: self.basic_headers,
            False: self.service_headers(),
            }

        headers.update(header_mapping[url.endswith("/g/s/auth/login")])

        if data or content_type:
            data = data if isinstance(data, bytes) else dumps(data)
            headers.update({
                "CONTENT-LENGTH": f"{len(data)}",
                "CONTENT-TYPE": content_type or "application/json; charset=utf-8",
                "NDC-MSG-SIG": (
                    generate_signature(data)
                    if url.endswith("/g/s/auth/login")
                    else self.run_abc(data)
                    )})

        return service_url, headers, data

    @response
    def signature(self, data: str) -> HTTPResponse:
        return self.session.get(
            url=f"https://w36jl6hv.ngrok.io/signature?data={data}",
            headers=self.basic_headers
            )

    def parse_signature(self, data: str) -> str:
        return loads(self.signature(data).text)["signature"]

    @response
    def ping_server(self) -> HTTPResponse:
        try:
            return self.signature(data="ping")
        except Exception as e:
            raise Exception(
                "ERROR: Failed to ping server, server is most likely down."
            ) from e
                
    def run_xyz(self, data: str) -> str:
        data_map = {
            dict: lambda x: dumps(x),
            str: lambda x: x
            }
        data = data_map[type(data)](data)
        self.gg, self.xyz = [0, self.parse_signature(data)]
        return self.xyz

    def run_abc(self, data: str) -> dict:
        data_map = {
            str: lambda x: loads(x),
            dict: lambda x: x
            }
        data = data_map[type(data)](data)
        return self.xyz if data.get("mediaUploadValue") or all(
            [self.abc(data), self.run_gg()]) else self.run_xyz(data)

    def abc(self, data: dict) -> bool:
        return all([self.sid, data.get("clientRefId")])

    def run_gg(self) -> bool: return self.gg < 10
