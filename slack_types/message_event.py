"""
Event-related type definitions for Slack API
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class EmojiElement(BaseModel):
    """Emoji element in rich text"""
    type: str = Field(description="Element type")
    name: str = Field(description="Emoji name")
    unicode: str = Field(description="Emoji unicode")


class TextElement(BaseModel):
    """Text element in rich text"""
    type: str = Field(description="Element type")
    text: str = Field(description="Text content")


class UserElement(BaseModel):
    """User mention element in rich text"""
    type: str = Field(description="Element type")
    user_id: str = Field(description="User ID")


class RichTextSection(BaseModel):
    """Rich text section containing elements"""
    type: str = Field(description="Section type")
    elements: List[EmojiElement | TextElement | UserElement] = Field(description="Section elements")


class RichTextBlock(BaseModel):
    """Rich text block in message"""
    type: str = Field(description="Block type")
    block_id: str = Field(description="Block ID")
    elements: List[RichTextSection] = Field(description="Block elements")


class MessageEvent(BaseModel):
    """Message event data"""
    user: str = Field(description="User ID who sent the message")
    type: str = Field(description="Event type")
    ts: str = Field(description="Message timestamp")
    client_msg_id: str = Field(description="Client message ID")
    text: str = Field(description="Message text")
    team: str = Field(description="Team ID")
    blocks: List[RichTextBlock] = Field(description="Message blocks")
    channel: str = Field(description="Channel ID")
    event_ts: str = Field(description="Event timestamp")
    channel_type: str = Field(description="Channel type")


class Authorization(BaseModel):
    """Authorization information"""
    enterprise_id: Optional[str] = Field(None, description="Enterprise ID")
    team_id: str = Field(description="Team ID")
    user_id: str = Field(description="User ID")
    is_bot: bool = Field(description="Whether the user is a bot")
    is_enterprise_install: bool = Field(description="Whether it's an enterprise install")


class MessageEventCallback(BaseModel):
    """Event callback wrapper"""
    token: str = Field(description="Verification token")
    team_id: str = Field(description="Team ID")
    context_team_id: str = Field(description="Context team ID")
    context_enterprise_id: Optional[str] = Field(None, description="Context enterprise ID")
    api_app_id: str = Field(description="API app ID")
    event: MessageEvent = Field(description="Event data")
    type: str = Field(description="Callback type")
    event_id: str = Field(description="Event ID")
    event_time: int = Field(description="Event time")
    authorizations: List[Authorization] = Field(description="Authorizations")
    is_ext_shared_channel: bool = Field(description="Whether it's an external shared channel")
    event_context: str = Field(description="Event context")
