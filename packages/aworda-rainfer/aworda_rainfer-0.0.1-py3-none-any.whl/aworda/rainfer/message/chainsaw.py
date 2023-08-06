from typing import Type, TypeVar

from aworda.rainfer.message.chain import MessageChain

from .element import App as App
from .element import At as At
from .element import AtAll as AtAll
from .element import Dice as Dice
from .element import Element as Element
from .element import Face as Face
from .element import File as File
from .element import FlashImage as FlashImage
from .element import Forward as Forward
from .element import Image as Image
from .element import MusicShare as MusicShare
from .element import Plain as Plain
from .element import Poke as Poke
from .element import Voice as Voice

Element_T = TypeVar("Element_T", bound=Element)


class ChainSaw:
    def __str__(self) -> str:
        return str(self.origin_chain)

    def __init__(self, origin_chain: MessageChain):
        self.origin_chain = origin_chain

    def anySaw(self, needing: Type[Element_T]):
        if not self.origin_chain.has(needing):
            return False
        return self.origin_chain.getFirst(needing)

    def anySawList(self, needing: Type[Element_T], limit: int = 0):
        """
        获取消息链中所有特定类型的消息元素

        Args:
            element_class (T): 指定的消息元素的类型, 例如 "Plain", "At", "Image" 等.

        Returns:
            List[T]: 获取到的符合要求的所有消息元素; 另: 可能是空列表([]).
        """
        if not self.origin_chain.has(needing):
            return []
        if limit == 0:
            return self.origin_chain.get(needing)
        else:
            return self.origin_chain.get(needing, limit)

    def Plain(self):
        return self.anySaw(Plain)

    def Plains(self, limit: int = 0):
        return self.anySawList(Plain, limit)

    def Voice(self):
        return self.anySaw(Voice)

    def Dice(self):
        return self.anySaw(Dice)

    def At(self):
        return self.anySaw(At)

    def Ats(self, limit: int = 0):
        return self.anySawList(At, limit)

    def AtAll(self):
        return self.anySaw(AtAll)

    def FlashImage(self):
        return self.anySaw(FlashImage)

    def Forward(self):
        return self.anySaw(Forward)

    def Image(self):
        return self.anySaw(Image)

    def Images(self, limit: int = 0):
        return self.anySawList(Image, limit)

    def MusicShare(self):
        return self.anySaw(MusicShare)

    def Poke(self):
        return self.anySaw(Poke)

    def Face(self):
        return self.anySaw(Face)

    def File(self):
        return self.anySaw(File)

    def App(self):
        return self.anySaw(App)

    def asDisplay(self):
        return self.origin_chain.asDisplay()
