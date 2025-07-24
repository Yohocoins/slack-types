"""
App Home event-related type definitions for Slack API
"""

from pydantic import BaseModel, Field


class AppHomeOpenedEvent(BaseModel):
    """App home opened event data"""
    type: str = Field(description="Event type")
    user: str = Field(description="User ID who opened the app home")
    channel: str = Field(description="Channel ID (DM with the app)")
    tab: str = Field(description="Tab that was opened (messages or home)")
    event_ts: str = Field(description="Event timestamp")


class Authorization(BaseModel):
    """Authorization information"""
    enterprise_id: str | None = Field(None, description="Enterprise ID")
    team_id: str = Field(description="Team ID")
    user_id: str = Field(description="User ID")
    is_bot: bool = Field(description="Whether the user is a bot")
    is_enterprise_install: bool = Field(description="Whether it's an enterprise install")


class AppHomeOpenedEventCallback(BaseModel):
    """App home event callback wrapper"""
    token: str = Field(description="Verification token")
    team_id: str = Field(description="Team ID")
    api_app_id: str = Field(description="API app ID")
    event: AppHomeOpenedEvent = Field(description="Event data")
    type: str = Field(description="Callback type")
    event_id: str = Field(description="Event ID")
    event_time: int = Field(description="Event time")
    authorizations: list[Authorization] = Field(description="Authorizations")
    is_ext_shared_channel: bool = Field(description="Whether it's an external shared channel") 