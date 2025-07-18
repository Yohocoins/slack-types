"""
Slack Types - Type definitions for Slack API using Pydantic
"""

from .team import TeamInfo, TeamInfoResponse, TeamIcon
from .user import User, UserInfoResponse, UserProfile
from .conversation import (
    Channel, DirectMessage, DirectMessageWithMembers, ConversationInfoResponse,
    Topic, Purpose, Tab, Properties, LatestMessage
)

__all__ = [
    "Team", "TeamInfoResponse", "TeamIcon",
    "User", "UserInfoResponse", "UserProfile",
    "Channel", "DirectMessage", "DirectMessageWithMembers", "ConversationInfoResponse",
    "Topic", "Purpose", "Tab", "Properties", "LatestMessage"
] 