from datetime import datetime
from io import BytesIO
from pathlib import Path
from typing import Iterable, List, Optional, Union

from aworda.rainfer.message.chain import MessageChain

from ..model import Friend, Member, Stranger
from .element import App as App
from .element import At as At
from .element import AtAll as AtAll
from .element import Dice as Dice
from .element import Element as Element
from .element import Face as Face
from .element import File as File
from .element import FlashImage as FlashImage
from .element import Forward as Forward
from .element import ForwardNode as ForwardNode
from .element import Image as Image
from .element import MusicShare as MusicShare
from .element import MusicShareKind
from .element import Plain as Plain
from .element import Poke as Poke
from .element import PokeMethods
from .element import Voice as Voice


class MessageChainX:
    elements: List[Element] = []

    def __str__(self) -> str:
        return str(self.elements)

    def App(self, content: str):
        self.elements.append(App(content=content))
        return self

    def At(self, target: Union[int, Member] = ...):
        self.elements.append(At(target))
        return self

    def AtAll(self):
        self.elements.append(AtAll())
        return self

    def Dice(self, value: int):
        self.elements.append(Dice(value=value))
        return self

    def Face(self, id: int = ...):
        self.elements.append(Face(id=id))
        return self

    def File(
        self,
        id: str,
        name: str,
        size: int,
        type: str = "Unknown",
    ):
        self.elements.append(File(type=type, id=id, name=name, size=size))
        return self

    def FlashImage(
        self,
        id: Optional[str] = None,
        url: Optional[str] = None,
        *,
        path: Optional[Union[Path, str]] = None,
        base64: Optional[str] = None,
        data_bytes: Union[None, bytes, BytesIO] = None,
    ):
        self.elements.append(FlashImage(id=id, url=url, path=path, base64=base64, data_bytes=data_bytes))
        return self

    def Forward(self, *nodes: Union[Iterable[ForwardNode], ForwardNode], **data):
        self.elements.append(Forward(*nodes, **data))
        return self

    def ForwardNode(
        self,
        target: Union[int, Friend, Member, Stranger] = ...,
        time: datetime = ...,
        message: "MessageChainX" = ...,
        name: str = ...,
        **data,
    ) -> ForwardNode:
        return ForwardNode(target=target, time=time, message=message.toMessageChain(), name=name, **data)

    def Image(
        self,
        id: Optional[str] = None,
        url: Optional[str] = None,
        *,
        path: Optional[Union[Path, str]] = None,
        base64: Optional[str] = None,
        data_bytes: Union[None, bytes, BytesIO] = None,
    ):
        self.elements.append(Image(id=id, url=url, path=path, base64=base64, data_bytes=data_bytes))
        return self

    def MusicShare(
        self,
        kind: MusicShareKind,
        title: Optional[str] = None,
        summary: Optional[str] = None,
        jumpUrl: Optional[str] = None,
        pictureUrl: Optional[str] = None,
        musicUrl: Optional[str] = None,
        brief: Optional[str] = None,
    ):
        self.elements.append(
            MusicShare(
                kind=kind,
                title=title,
                summary=summary,
                jumpUrl=jumpUrl,
                pictureUrl=pictureUrl,
                musicUrl=musicUrl,
                brief=brief,
            )
        )
        return self

    def Plain(self, text: str):
        self.elements.append(Plain(text))
        return self

    def Poke(self, name: PokeMethods):
        self.elements.append(Poke(name))
        return self

    def Voice(
        self,
        id: Optional[str] = None,
        url: Optional[str] = None,
        *,
        path: Optional[Union[Path, str]] = None,
        base64: Optional[str] = None,
        data_bytes: Union[None, bytes, BytesIO] = None,
        **kwargs,
    ):
        self.elements.append(Voice(id=id, url=url, path=path, base64=base64, data_bytes=data_bytes, **kwargs))

    def asDisplay(self) -> str:
        """
        获取以字符串形式表示的消息链, 且趋于通常你见到的样子.

        Returns:
            str: 以字符串形式表示的消息链
        """
        return "".join(i.asDisplay() for i in self.elements)

    def toMessageChain(self) -> MessageChain:
        return MessageChain.create(self.elements)
