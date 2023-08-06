import json
import os
from typing import Any, Dict

import jwt
from google.protobuf.json_format import MessageToDict, ParseDict
from twirp.context import Context  # type: ignore

from .gen.video.coordinator.call_v1.call_pb2 import CallSettings
from .gen.video.coordinator.client_v1_rpc import client_rpc_pb2, client_rpc_twirp
from .gen.video.coordinator.server_v1_rpc import server_rpc_pb2, server_rpc_twirp

try:
    from importlib import metadata  # type: ignore
except ImportError:  # for Python<3.8
    import importlib_metadata as metadata  # type: ignore

__version__ = metadata.version("stream_video")


def get_user_agent() -> str:
    return f"stream-python-client-{__version__}"


def get_default_header() -> Dict[str, str]:
    return {
        "Content-type": "application/json",
        "X-Stream-Client": get_user_agent(),
    }


def message_to_dict(message: Any) -> Dict[str, Any]:
    """Converts protobuf message to a dictionary."""
    return MessageToDict(
        message,
        preserving_proto_field_name=True,
    )


class StreamVideo:
    def __init__(
        self,
        api_key: str,
        api_secret: str,
        timeout: float = 6.0,
        **options: Dict[str, Any],
    ):
        self.base_url = "http://localhost:26991"
        if options.get("base_url"):
            self.base_url = str(options["base_url"])
        elif os.getenv("STREAM_VIDEO_URL"):
            self.base_url = os.environ["STREAM_VIDEO_URL"]

        self.timeout = timeout
        if os.getenv("STREAM_VIDEO_TIMEOUT"):
            self.timeout = float(os.environ["STREAM_VIDEO_TIMEOUT"])

        self.server_side_twirp = server_rpc_twirp.ServerRPCClient(
            address=self.base_url,
            timeout=self.timeout,
        )

        self.client_side_twirp = client_rpc_twirp.ClientRPCClient(
            address=self.base_url,
            timeout=self.timeout,
        )

        self.api_key = api_key
        self.api_secret = api_secret
        self.auth_token = jwt.encode(
            {"server": True}, self.api_secret, algorithm="HS256"
        )
        self.ctx = Context(
            headers={
                **get_default_header(),
                "api_key": self.api_key,
                "authorization": self.auth_token,
            }
        )

        self.options = options

    def request(self, twirp_method: Any, request_message: Any) -> Dict[str, Any]:
        return message_to_dict(
            twirp_method(
                ctx=self.ctx,
                server_path_prefix="/rpc",
                request=request_message,
            )
        )

    def get_app(self) -> Dict:
        return self.request(
            self.server_side_twirp.GetApp, server_rpc_pb2.GetAppRequest()
        )

    def get_call_type(self, name: str) -> Dict:
        return self.request(
            self.server_side_twirp.GetCallType,
            server_rpc_pb2.GetCallTypeRequest(name=name),
        )

    def create_call_type(self, name: str, **settings: Dict[str, Any]) -> Dict:
        message = ParseDict(
            dict(name=name, settings=settings),
            server_rpc_pb2.CreateCallTypeRequest(),
            ignore_unknown_fields=True,
        )
        return self.request(self.server_side_twirp.CreateCallType, message)

    def update_call_type(self, name: str, **settings: Dict[str, Any]) -> Dict:
        message = ParseDict(
            dict(settings=settings),
            server_rpc_pb2.UpdateCallTypeRequest(name=name),
            ignore_unknown_fields=True,
        )
        return self.request(self.server_side_twirp.UpdateCallType, message)

    def delete_call_type(self, name: str) -> Dict:
        message = server_rpc_pb2.DeleteCallTypeRequest(name=name)
        return self.request(self.server_side_twirp.DeleteCallType, message)

    def query_call_types(self, **params: Dict[str, Any]) -> Dict:
        message = ParseDict(
            params,
            server_rpc_pb2.QueryCallTypesRequest(),
            ignore_unknown_fields=True,
        )
        return self.request(self.server_side_twirp.QueryCallTypes, message)

    def update_app(self, **params: Dict[str, Any]) -> Dict:
        message = ParseDict(
            params,
            server_rpc_pb2.UpdateAppRequest(),
            ignore_unknown_fields=True,
        )
        return self.request(self.server_side_twirp.UpdateApp, message)

    def _call_input(self, custom_data: Dict, settings_overrides: Dict) -> Any:
        custom_data_encoded = json.dumps(custom_data or {})
        overrides = ParseDict(
            settings_overrides,
            CallSettings(),
            ignore_unknown_fields=True,
        )
        return client_rpc_pb2.CallInput(
            custom_json=custom_data_encoded, settings_overrides=overrides
        )

    def get_or_create_call(
        self,
        call_type: str,
        call_id: str,
        custom_data: Dict,
        **settings_overrides: Dict[str, Any],
    ) -> Dict:
        message = client_rpc_pb2.CreateCallRequest(
            type=call_type,
            id=call_id,
            input=self._call_input(custom_data, settings_overrides),
        )
        return self.request(self.client_side_twirp.GetOrCreateCall, message)

    def create_call(
        self,
        call_type: str,
        call_id: str,
        custom_data: Dict,
        **settings_overrides: Dict[str, Any],
    ) -> Dict:
        call_input = self._call_input(custom_data, settings_overrides)
        message = client_rpc_pb2.CreateCallRequest(
            type=call_type, id=call_id, input=call_input
        )
        return self.request(self.client_side_twirp.CreateCall, message)

    def update_call(self) -> Dict:
        pass

    def query_session_timeline_events(self, session_id: str) -> Dict:
        message = server_rpc_pb2.QuerySessionTimelineEventsRequest(
            session_id=session_id
        )
        return self.request(self.server_side_twirp.QuerySessionTimelineEvents, message)

    def query_sessions(self) -> Dict:
        return self.request(
            self.server_side_twirp.QuerySessions, server_rpc_pb2.QuerySessionsRequest()
        )

    def get_push_provider(self, provider_id: str) -> Dict:
        return self.request(
            self.server_side_twirp.GetPushProvider,
            server_rpc_pb2.GetPushProviderRequest(id=provider_id),
        )

    def create_push_provider(
        self, provider_id: str, **provider_settings: Dict[str, Any]
    ) -> Dict:
        return self.request(
            self.server_side_twirp.CreatePushProvider,
            server_rpc_pb2.CreatePushProviderRequest(
                input=dict(id=provider_id, **provider_settings),
            ),
        )

    def update_push_provider(
        self, provider_id: str, **provider_settings: Dict[str, Any]
    ) -> Dict:
        return self.request(
            self.server_side_twirp.UpdatePushProvider,
            server_rpc_pb2.UpdatePushProviderRequest(
                input=dict(id=provider_id, **provider_settings),
            ),
        )

    def delete_push_provider(self, provider_id: str) -> Dict:
        return self.request(
            self.server_side_twirp.DeletePushProvider,
            server_rpc_pb2.DeletePushProviderRequest(id=provider_id),
        )

    def query_push_providers(self) -> Dict:
        return self.request(
            self.server_side_twirp.QueryPushProviders,
            server_rpc_pb2.QueryPushProvidersRequest(),
        )
