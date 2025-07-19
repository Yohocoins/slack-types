"""
Slack Types - Type definitions for Slack API using Pydantic
"""

from .team import Team, TeamInfoResponse, TeamIcon
from .user import User, UserInfoResponse, UserProfile
from .conversation import (
    Channel, DirectMessage, DirectMessageWithMembers, ConversationInfoResponse,
    Topic, Purpose, Tab, Properties, LatestMessage
)
from .events import (
    MessageEvent, EventCallback, Authorization, RichTextBlock, RichTextSection,
    EmojiElement, TextElement, UserElement
)

__version__ = "0.1.0"

__all__ = [
    "Team", "TeamInfoResponse", "TeamIcon",
    "User", "UserInfoResponse", "UserProfile",
    "Channel", "DirectMessage", "DirectMessageWithMembers", "ConversationInfoResponse",
    "Topic", "Purpose", "Tab", "Properties", "LatestMessage",
    "MessageEvent", "EventCallback", "Authorization", "RichTextBlock", "RichTextSection",
    "EmojiElement", "TextElement", "UserElement"
]