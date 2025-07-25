"""
User-related type definitions for Slack API
"""

from pydantic import BaseModel, Field


class StatusEmojiDisplayInfo(BaseModel):
    """Status emoji display information"""
    # Empty list in the JSON, so this is a placeholder for potential future fields
    pass


class UserProfile(BaseModel):
    """User profile information"""
    real_name: str = Field(description="Real name")
    display_name: str = Field(description="Display name")
    avatar_hash: str = Field(description="Avatar hash")
    real_name_normalized: str = Field(description="Normalized real name")
    display_name_normalized: str = Field(description="Normalized display name")
    image_24: str = Field(description="24x24 pixel image URL")
    image_32: str = Field(description="32x32 pixel image URL")
    image_48: str = Field(description="48x48 pixel image URL")
    image_72: str = Field(description="72x72 pixel image URL")
    image_192: str = Field(description="192x192 pixel image URL")
    image_512: str = Field(description="512x512 pixel image URL")
    image_1024: str | None = Field(default=None, description="1024x1024 pixel image URL")
    image_original: str | None = Field(default=None, description="Original image URL")
    is_custom_image: bool | None = Field(default=None, description="Whether the image is custom")
    first_name: str = Field(description="First name")
    last_name: str = Field(description="Last name")
    team: str = Field(description="Team ID")
    title: str = Field(description="Job title")
    phone: str = Field(description="Phone number")
    skype: str = Field(description="Skype username")
    status_text: str = Field(description="Status text")
    status_text_canonical: str = Field(description="Canonical status text")
    status_emoji: str = Field(description="Status emoji")
    status_emoji_display_info: list[StatusEmojiDisplayInfo] = Field(description="Status emoji display info")
    status_expiration: int = Field(description="Status expiration timestamp")


class User(BaseModel):
    """User information from Slack API"""
    id: str = Field(description="User ID")
    name: str = Field(description="Username")
    is_bot: bool = Field(description="Whether user is a bot")
    updated: int = Field(description="Last updated timestamp")
    is_app_user: bool = Field(description="Whether user is an app user")
    team_id: str = Field(description="Team ID")
    deleted: bool = Field(description="Whether user is deleted")
    color: str = Field(description="User color")
    is_email_confirmed: bool = Field(description="Whether email is confirmed")
    real_name: str = Field(description="Real name")
    tz: str = Field(description="Timezone")
    tz_label: str = Field(description="Timezone label")
    tz_offset: int = Field(description="Timezone offset in seconds")
    is_admin: bool = Field(description="Whether user is admin")
    is_owner: bool = Field(description="Whether user is owner")
    is_primary_owner: bool = Field(description="Whether user is primary owner")
    is_restricted: bool = Field(description="Whether user is restricted")
    is_ultra_restricted: bool = Field(description="Whether user is ultra restricted")
    locale: str = Field(description="User locale")
    who_can_share_contact_card: str = Field(description="Who can share contact card")
    profile: UserProfile = Field(description="User profile information")


class UserInfoResponse(BaseModel):
    """Response wrapper for user.info API call"""
    ok: bool = Field(description="Whether the API call was successful")
    user: User = Field(description="User information")
