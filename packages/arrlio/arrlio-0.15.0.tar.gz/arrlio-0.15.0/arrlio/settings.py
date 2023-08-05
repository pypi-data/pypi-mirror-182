import os
from typing import Optional, Set, Union
from uuid import uuid4

from pydantic import BaseSettings, Field, PositiveInt, constr

from arrlio.tp import BackendT, ExecutorT, PluginT, PriorityT, TimeoutT

ENV_PREFIX = os.environ.get("ARRLIO_ENV_PREFIX", "ARRLIO_")

BACKEND = "arrlio.backends.local"

TASK_BIND = False
TASK_QUEUE = "arrlio.tasks"
TASK_PRIORITY = 1
TASK_TIMEOUT = 300
TASK_TTL = 300
TASK_ACK_LATE = True
TASK_RESULT_TTL = 300
TASK_RESULT_RETURN = True
TASK_EVENTS = False
TASK_EVENT_TTL = 300

MESSAGE_EXCHANGE = "arrlio.messages"
MESSAGE_PRIORITY = 1
MESSAGE_TTL = 300
MESSAGE_ACK_LATE = True

EVENT_TTL = 300

TASK_QUEUES = [TASK_QUEUE]
MESSAGE_QUEUES = [MESSAGE_EXCHANGE]

PLUGINS = ["arrlio.plugins.events"]
EXECUTOR = "arrlio.executor"


class TaskConfig(BaseSettings):
    bind: bool = Field(default_factory=lambda: TASK_BIND)
    queue: str = Field(default_factory=lambda: TASK_QUEUE)
    priority: PriorityT = Field(default_factory=lambda: TASK_PRIORITY)
    timeout: Optional[TimeoutT] = Field(default_factory=lambda: TASK_TIMEOUT)
    ttl: Optional[PositiveInt] = Field(default_factory=lambda: TASK_TTL)
    ack_late: Optional[bool] = Field(default_factory=lambda: TASK_ACK_LATE)
    result_return: Optional[bool] = Field(default_factory=lambda: TASK_RESULT_RETURN)
    result_ttl: Optional[PositiveInt] = Field(default_factory=lambda: TASK_RESULT_TTL)
    events: Union[Set[str], bool] = Field(default_factory=lambda: TASK_EVENTS)
    event_ttl: Optional[PositiveInt] = Field(default_factory=lambda: TASK_EVENT_TTL)

    class Config:
        validate_assignment = True
        env_prefix = f"{ENV_PREFIX}TASK_"


class MessageConfig(BaseSettings):
    exchange: str = Field(default_factory=lambda: MESSAGE_EXCHANGE)
    priority: PriorityT = Field(default_factory=lambda: MESSAGE_PRIORITY)
    ttl: Optional[PositiveInt] = Field(default_factory=lambda: MESSAGE_TTL)
    ack_late: Optional[bool] = Field(default_factory=lambda: MESSAGE_ACK_LATE)

    class Config:
        validate_assignment = True
        env_prefix = f"{ENV_PREFIX}MESSAGE_"


class EventConfig(BaseSettings):
    ttl: Optional[PositiveInt] = Field(default_factory=lambda: EVENT_TTL)


class Config(BaseSettings):
    app_id: constr(min_length=1) = Field(default_factory=lambda: f"{uuid4()}")
    backend: BackendT = Field(default_factory=lambda: BACKEND, env=f"{ENV_PREFIX}BACKEND")
    task: TaskConfig = Field(default_factory=TaskConfig)
    message: MessageConfig = Field(default_factory=MessageConfig)
    event: EventConfig = Field(default_factory=EventConfig)
    task_queues: Set[str] = Field(default_factory=lambda: TASK_QUEUES)
    message_queues: Set[str] = Field(default_factory=lambda: MESSAGE_QUEUES)
    plugins: Set[PluginT] = Field(default_factory=lambda: PLUGINS)
    executor: ExecutorT = Field(default_factory=lambda: EXECUTOR)

    class Config:
        validate_assignment = True
        env_prefix = ENV_PREFIX
