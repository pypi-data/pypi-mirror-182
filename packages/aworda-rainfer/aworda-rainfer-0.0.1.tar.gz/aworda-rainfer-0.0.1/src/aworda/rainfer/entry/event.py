"""Rainfer 事件相关的导入集合"""

# no error

from aworda.rainfer.event import MiraiEvent as MiraiEvent
from aworda.rainfer.event.lifecycle import AdapterLaunched as AdapterLaunched
from aworda.rainfer.event.lifecycle import AdapterShutdowned as AdapterShutdowned
from aworda.rainfer.event.lifecycle import ApplicationLaunched as ApplicationLaunched
from aworda.rainfer.event.lifecycle import (
    ApplicationLifecycleEvent as ApplicationLifecycleEvent,
)
from aworda.rainfer.event.lifecycle import (
    ApplicationShutdowned as ApplicationShutdowned,
)
from aworda.rainfer.event.message import FriendMessage as FriendMessage
from aworda.rainfer.event.message import GroupMessage as GroupMessage
from aworda.rainfer.event.message import OtherClientMessage as OtherClientMessage
from aworda.rainfer.event.message import StrangerMessage as StrangerMessage
from aworda.rainfer.event.message import TempMessage as TempMessage
from aworda.rainfer.event.mirai import BotEvent as BotEvent
from aworda.rainfer.event.mirai import (
    BotGroupPermissionChangeEvent as BotGroupPermissionChangeEvent,
)
from aworda.rainfer.event.mirai import (
    BotInvitedJoinGroupRequestEvent as BotInvitedJoinGroupRequestEvent,
)
from aworda.rainfer.event.mirai import BotJoinGroupEvent as BotJoinGroupEvent
from aworda.rainfer.event.mirai import BotLeaveEventActive as BotLeaveEventActive
from aworda.rainfer.event.mirai import BotLeaveEventKick as BotLeaveEventKick
from aworda.rainfer.event.mirai import BotMuteEvent as BotMuteEvent
from aworda.rainfer.event.mirai import BotOfflineEventActive as BotOfflineEventActive
from aworda.rainfer.event.mirai import BotOfflineEventDropped as BotOfflineEventDropped
from aworda.rainfer.event.mirai import BotOfflineEventForce as BotOfflineEventForce
from aworda.rainfer.event.mirai import BotOnlineEvent as BotOnlineEvent
from aworda.rainfer.event.mirai import BotReloginEvent as BotReloginEvent
from aworda.rainfer.event.mirai import BotUnmuteEvent as BotUnmuteEvent
from aworda.rainfer.event.mirai import CommandExecutedEvent as CommandExecutedEvent
from aworda.rainfer.event.mirai import FriendEvent as FriendEvent
from aworda.rainfer.event.mirai import (
    FriendInputStatusChangedEvent as FriendInputStatusChangedEvent,
)
from aworda.rainfer.event.mirai import FriendNickChangedEvent as FriendNickChangedEvent
from aworda.rainfer.event.mirai import FriendRecallEvent as FriendRecallEvent
from aworda.rainfer.event.mirai import (
    GroupAllowAnonymousChatEvent as GroupAllowAnonymousChatEvent,
)
from aworda.rainfer.event.mirai import (
    GroupAllowConfessTalkEvent as GroupAllowConfessTalkEvent,
)
from aworda.rainfer.event.mirai import (
    GroupAllowMemberInviteEvent as GroupAllowMemberInviteEvent,
)
from aworda.rainfer.event.mirai import (
    GroupEntranceAnnouncementChangeEvent as GroupEntranceAnnouncementChangeEvent,
)
from aworda.rainfer.event.mirai import GroupEvent as GroupEvent
from aworda.rainfer.event.mirai import GroupMuteAllEvent as GroupMuteAllEvent
from aworda.rainfer.event.mirai import GroupNameChangeEvent as GroupNameChangeEvent
from aworda.rainfer.event.mirai import GroupRecallEvent as GroupRecallEvent
from aworda.rainfer.event.mirai import MemberCardChangeEvent as MemberCardChangeEvent
from aworda.rainfer.event.mirai import MemberHonorChangeEvent as MemberHonorChangeEvent
from aworda.rainfer.event.mirai import MemberJoinEvent as MemberJoinEvent
from aworda.rainfer.event.mirai import MemberJoinRequestEvent as MemberJoinRequestEvent
from aworda.rainfer.event.mirai import MemberLeaveEventKick as MemberLeaveEventKick
from aworda.rainfer.event.mirai import MemberLeaveEventQuit as MemberLeaveEventQuit
from aworda.rainfer.event.mirai import MemberMuteEvent as MemberMuteEvent
from aworda.rainfer.event.mirai import MemberPerm as MemberPerm
from aworda.rainfer.event.mirai import (
    MemberPermissionChangeEvent as MemberPermissionChangeEvent,
)
from aworda.rainfer.event.mirai import (
    MemberSpecialTitleChangeEvent as MemberSpecialTitleChangeEvent,
)
from aworda.rainfer.event.mirai import MemberUnmuteEvent as MemberUnmuteEvent
from aworda.rainfer.event.mirai import NewFriendRequestEvent as NewFriendRequestEvent
from aworda.rainfer.event.mirai import NudgeEvent as NudgeEvent
from aworda.rainfer.event.mirai import (
    OtherClientOfflineEvent as OtherClientOfflineEvent,
)
from aworda.rainfer.event.mirai import OtherClientOnlineEvent as OtherClientOnlineEvent
from aworda.rainfer.event.mirai import RequestEvent as RequestEvent
