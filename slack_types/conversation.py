"""
Conversation-related type definitions for Slack API
"""

from typing import List
from pydantic import BaseModel, Field


class Topic(BaseModel):
    """Channel topic information"""
    value: str = Field(..., description="Topic value")
    creator: str = Field(..., description="Creator user ID")
    last_set: int = Field(..., description="Last set timestamp")


class Purpose(BaseModel):
    """Channel purpose information"""
    value: str = Field(..., description="Purpose value")
    creator: str = Field(..., description="Creator user ID")
    last_set: int = Field(..., description="Last set timestamp")


class Tab(BaseModel):
    """Channel tab information"""
    id: str = Field(..., description="Tab ID")
    label: str = Field(..., description="Tab label")
    type: str = Field(..., description="Tab type")


class Properties(BaseModel):
    """Channel properties"""
    tabs: List[Tab] = Field(..., description="Channel tabs")


class LatestMessage(BaseModel):
    """Latest message in conversation"""
    type: str = Field(..., description="Message type")
    user: str = Field(..., description="User ID")
    text: str = Field(..., description="Message text")
    ts: str = Field(..., description="Message timestamp")


class Channel(BaseModel):
    """Channel conversation information"""
    id: str = Field(..., description="Channel ID")
    name: str = Field(..., description="Channel name")
    is_channel: bool = Field(..., description="Whether it's a channel")
    is_group: bool = Field(..., description="Whether it's a group")
    is_im: bool = Field(..., description="Whether it's a direct message")
    is_mpim: bool = Field(..., description="Whether it's a multi-person direct message")
    is_private: bool = Field(..., description="Whether it's private")
    created: int = Field(..., description="Creation timestamp")
    is_archived: bool = Field(..., description="Whether it's archived")
    is_general: bool = Field(..., description="Whether it's the general channel")
    unlinked: int = Field(..., description="Unlinked count")
    name_normalized: str = Field(..., description="Normalized name")
    is_shared: bool = Field(..., description="Whether it's shared")
    is_frozen: bool = Field(..., description="Whether it's frozen")
    is_org_shared: bool = Field(..., description="Whether it's organization shared")
    is_pending_ext_shared: bool = Field(..., description="Whether it's pending external share")
    pending_shared: List[str] = Field(..., description="Pending shared team IDs")
    context_team_id: str = Field(..., description="Context team ID")
    updated: int = Field(..., description="Last updated timestamp")
    parent_conversation: str | None = Field(None, description="Parent conversation ID")
    creator: str = Field(..., description="Creator user ID")
    is_ext_shared: bool = Field(..., description="Whether it's externally shared")
    shared_team_ids: List[str] = Field(..., description="Shared team IDs")
    pending_connected_team_ids: List[str] = Field(..., description="Pending connected team IDs")
    topic: Topic = Field(..., description="Channel topic")
    purpose: Purpose = Field(..., description="Channel purpose")
    properties: Properties = Field(..., description="Channel properties")
    previous_names: List[str] = Field(..., description="Previous names")


class DirectMessage(BaseModel):
    """Direct message conversation information"""
    id: str = Field(..., description="DM ID")
    created: int = Field(..., description="Creation timestamp")
    is_im: bool = Field(..., description="Whether it's a direct message")
    is_org_shared: bool = Field(..., description="Whether it's organization shared")
    user: str = Field(..., description="User ID")
    last_read: str = Field(..., description="Last read timestamp")
    latest: LatestMessage = Field(..., description="Latest message")
    unread_count: int = Field(..., description="Unread count")
    unread_count_display: int = Field(..., description="Unread count display")
    is_open: bool = Field(..., description="Whether it's open")
    locale: str = Field(..., description="Locale")
    priority: float = Field(..., description="Priority")


class DirectMessageWithMembers(DirectMessage):
    """Direct message with member count"""
    num_members: int = Field(..., description="Number of members")


class ConversationInfoResponse(BaseModel):
    """Response wrapper for conversations.info API call"""
    ok: bool = Field(..., description="Whether the API call was successful")
    channel: Channel | DirectMessage | DirectMessageWithMembers = Field(..., description="Conversation information")
