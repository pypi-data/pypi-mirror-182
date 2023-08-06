"""Rainfer 内置的 Dispatcher"""


import contextlib

from graia.broadcast.entities.dispatcher import BaseDispatcher as AbstractDispatcher
from graia.broadcast.interfaces.dispatcher import DispatcherInterface

from .message.chain import MessageChain
from .message.chainsaw import ChainSaw
from .message.element import Source
from .typing import generic_isinstance, generic_issubclass  # type:ignore


class MessageChainDispatcher(AbstractDispatcher):
    """从 MessageEvent 提取 MessageChain 的 Dispatcher"""

    @staticmethod
    async def catch(interface: DispatcherInterface):
        from .event.message import ActiveMessage, MessageEvent

        if isinstance(interface.event, (MessageEvent, ActiveMessage)):
            if generic_issubclass(MessageChain, interface.annotation):
                return interface.event.messageChain


class ChainSawDispatcher(AbstractDispatcher):
    """从 MessageEvent 提取 MessageChain 并转化为 ChainSaw 的 Dispatcher"""

    @staticmethod
    async def catch(interface: DispatcherInterface):
        from .event.message import ActiveMessage, MessageEvent

        if isinstance(interface.event, (MessageEvent, ActiveMessage)):
            if generic_issubclass(ChainSaw, interface.annotation):
                return ChainSaw(interface.event.messageChain)


class ContextDispatcher(AbstractDispatcher):
    """提取上下文的 Dispatcher"""

    @staticmethod
    async def catch(interface: DispatcherInterface):
        from . import get_running

        if generic_isinstance(interface.event, interface.annotation):
            return interface.event

        return get_running(interface.annotation, fail_err=False)


class SourceDispatcher(AbstractDispatcher):
    """提取 MessageEvent 消息链 Source 元素的 Dispatcher"""

    @staticmethod
    async def catch(interface: DispatcherInterface):
        from .event.message import ActiveMessage, MessageEvent

        if isinstance(interface.event, (MessageEvent, ActiveMessage)):
            if generic_issubclass(Source, interface.annotation):
                return interface.event.messageChain.getFirst(Source)


class SenderDispatcher(AbstractDispatcher):
    """
    从 MessageEvent 提取 sender 的 Dispatcher.
    """

    @staticmethod
    async def catch(interface: DispatcherInterface):
        from .event.message import MessageEvent

        if isinstance(interface.event, MessageEvent):
            with contextlib.suppress(TypeError):
                if generic_isinstance(interface.event.sender, interface.annotation):
                    return interface.event.sender


class SubjectDispatcher(AbstractDispatcher):
    """从 ActiveMessage 提取 subject 的 Dispatcher"""

    @staticmethod
    async def catch(interface: DispatcherInterface):
        from .event.message import ActiveMessage

        if isinstance(interface.event, ActiveMessage):
            if generic_issubclass(interface.annotation, interface.event.subject):
                return interface.event.subject


class BaseDispatcher(AbstractDispatcher):
    """空 Dispatcher"""

    @staticmethod
    async def catch(*_):
        pass
