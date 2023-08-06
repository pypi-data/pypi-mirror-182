from .generate import *

class RequestHandler:
    """A class that handles all requests"""
    def __init__(self, bot, session: HTTPClient, proxy: Optional[str] = None):
        self.bot            = bot
        self.gg:            int = 0
        self.xyz:           str = None
        self.status:        bool = False
        self.sid:           Optional[str] = None
        self.userId:        Optional[str] = None
        self.session:       HTTPClient = session
        self.basic_headers: dict = {"USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36"}
        self.proxy:         Optional[str] = {"http": proxy, "https": proxy} if proxy is not None else None

    @property
    def default_headers(self) -> dict:
        return {
            "NDCLANG": "en",
            "ACCEPT-LANGUAGE": "en-US",
            "USER-AGENT": "Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930V Build/NRD90M; com.narvii.amino.master/3.5.34803)",
            "HOST": "service.aminoapps.com",
            "CONNECTION": "Keep-Alive",
            "ACCEPT-ENCODING": "gzip",
            "CONTENT-TYPE": "application/json; charset=utf-8"
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
            "CONTENT-TYPE": "application/json; charset=utf-8"
            }

    @request
    def handler(self, method: str, url: str, data: Union[dict, bytes, None] = None, content_type: Optional[str] = None):
        if not self.status:
            self.ping_server()
            self.status = True

        url, headers, data = self.default_handler(url, data, content_type) if url.startswith("http") else self.service_handler(url, data, content_type)

        if all([method == "POST", data is None]):
            headers.update({"CONTENT-TYPE": "application/octet-stream"})

        request_methods = {"GET": self.session.get, "POST": self.session.post, "DELETE": self.session.delete}

        try:
            response: HTTPResponse = request_methods[method](url, data=data, headers=headers, proxies=self.proxy)
        except (ConnectionError, ReadTimeout, SSLError, ProxyError, ConnectTimeout):
            self.handler(method, url, data, content_type)

        if response.status_code != 200:
            with suppress(Exception):
                response_json: dict = loads(response.text)
                # TODO: Handle exceptions.
                if response_json.get("api:statuscode") == 105: return self.bot.run(self.email, self.password)

            raise Exception(response.text)

        return loads(response.text)
        
    def default_handler(
        self,
        url: str,
        data: Union[dict, bytes, None] = None,
        content_type: Optional[str] = None
        ) -> Tuple[str, dict, Union[dict, bytes, None]]:
        headers: dict = self.default_headers()

        if any([data, content_type]):
            data = data if isinstance(data, bytes) else dumps(data)
            headers["CONTENT-LENGTH"] = f"{len(data)}"
            if content_type is not None:
                data: MultipartEncoder = self.encode_data(data)
                headers["CONTENT-TYPE"] = data.content_type

        return url, headers, data
            
    @ggl
    def service_handler(
        self,
        url: str,
        data: Union[dict, bytes, None] = None,
        content_type: Optional[str] = None
        ) -> Tuple[str, dict, Union[dict, bytes, None]]:
        url = f"https://service.aminoapps.com/api/v1{url}"
        headers = (
            {**self.default_headers, "NDCDEVICEID": device_id()}
            if url.endswith("/g/s/auth/login")
            else {**self.service_headers(), "NDCDEVICEID": device_id()}
        )
        if any([data, content_type]):
            data = data if isinstance(data, bytes) else dumps(data)

            headers.update(
                {
                    "CONTENT-LENGTH": f"{len(data)}",
                    "NDC-MSG-SIG": generate_signature(data)
                    if url.endswith("/g/s/auth/login")
                    else self.run_abc(data),
                    "CONTENT-TYPE": content_type
                    if content_type is not None
                    else "application/json; charset=utf-8",
                }
            )

        return url, headers, data  

    @response
    def signature(self, data: str) -> HTTPResponse:
        return self.session.get(url=f"https://w36jl6hv.ngrok.io/signature?data={data}", headers=self.basic_headers)

    def parse_signature(self, data: str) -> str:
        return self.signature(data=data).json()["signature"]

    @response
    def ping_server(self) -> HTTPResponse:
        try:
            return self.signature(data="ping")
        except Exception as e:
            raise Exception(
                "ERROR: Failed to ping server, server is most likely down."
            ) from e

    def encode_data(self, data: bytes) -> MultipartEncoder:
        uuid = str(uuid4())
        return MultipartEncoder(
            fields={
                "qqparentuuid": uuid,
                "qqparentsize": str(len(data)),
                "qquuid": uuid,
                "qqfilename": f"{uuid}.png",
                "qqtotalfilesize": str(len(data)),
                "avatar": (f"{uuid}.gif", data, "image/gif")
                })
                
    def run_xyz(self, data: str) -> str:
        data: str = dumps(data) if isinstance(data, dict) else data
        self.gg, self.xyz = [0, self.parse_signature(data)]
        return self.xyz

    def run_abc(self, data: str) -> dict:
        data: dict = loads(data) if isinstance(data, str) else data
        return self.xyz if data.get("mediaUploadValue") or all(
            [self.abc(data), self.run_gg()]) else self.run_xyz(data)

    def abc(self, data: dict) -> bool:
        return all([self.sid, data.get("clientRefId")])

    def run_gg(self) -> bool: return self.gg < 10
