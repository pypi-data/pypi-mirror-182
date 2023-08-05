import importlib
import re
from types import FunctionType, ModuleType
from typing import Any, Callable, Coroutine, Dict, Optional, no_type_check

from pydantic import AnyUrl, conint

AsyncCallableT = Callable[..., Coroutine]
ExceptionFilterT = Callable[[Exception], bool]
PriorityT = conint(ge=1, le=10)
TimeoutT = conint(ge=0)


class SecretAnyUrl(AnyUrl):
    __slots__ = AnyUrl.__slots__ + ("_url",)

    @no_type_check
    def __new__(cls, url: Optional[str], **kwds) -> object:
        if url is None:
            _url = cls.build(**kwds)
        else:
            _url = url
            if re.match(r".*://([^:.]*):?([^:.]*)@.*", url):
                url = re.sub(r"://([^:.]*):?([^.]*)@", "://***:***@", url)
        if kwds.get("user") is not None:
            kwds["user"] = "***"
        if kwds.get("password") is not None:
            kwds["password"] = "***"
        obj = super().__new__(cls, url, **kwds)
        obj._url = _url
        return obj

    def __repr__(self) -> str:
        return f"AnyUrl('{self}')"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, SecretAnyUrl) and self.get_secret_value() == other.get_secret_value()

    def __hash__(self):
        return self._url.__hash__()

    def get_secret_value(self) -> str:
        return self._url


class AmqpDsn(SecretAnyUrl):
    allowed_schemes = {"amqp", "amqps"}
    user_required = True


class RedisDsn(SecretAnyUrl):
    allowed_schemes = {"redis", "rediss"}
    user_required = False

    @classmethod
    def validate_parts(cls, parts: Dict[str, str]) -> Dict[str, str]:
        defaults = {
            "domain": "localhost" if not (parts["ipv4"] or parts["ipv6"]) else "",
            "port": "6379",
            "path": "/0",
        }
        for key, value in defaults.items():
            if not parts[key]:
                parts[key] = value
        return super().validate_parts(parts)


class BackendT:
    validate_always = True

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, str):
            v = importlib.import_module(v)
            if not hasattr(v, "BackendConfig"):
                raise TypeError("Module doesn't provide BackendConfig class")
            if not hasattr(v, "Backend"):
                raise TypeError("Module doesn't provide Backend class")
        if not isinstance(v, (FunctionType, ModuleType)):
            raise ValueError("Expect Function or Module")
        return v


class SerializerT:
    validate_always = True

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, str):
            v = importlib.import_module(v)
        if isinstance(v, ModuleType):
            v = v.Serializer
        if not callable(v):
            raise ValueError("Expect module path, module or callable object")
        return v


class PluginT:
    validate_always = True

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, str):
            v = importlib.import_module(v)
        if isinstance(v, ModuleType):
            v = v.Plugin
        if not callable(v):
            raise ValueError("Expect module path, module or callable object")
        return v


class ExecutorT:
    validate_always = True

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, str):
            v = importlib.import_module(v)
        if isinstance(v, ModuleType):
            v = v.Executor
        if not callable(v):
            raise ValueError("Expect module path, module or callable object")
        return v
