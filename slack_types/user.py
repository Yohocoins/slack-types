"""
User-related type definitions for Slack API
"""

from pydantic import BaseModel, Field, EmailStr


class UserProfile(BaseModel):
    """User profile information"""
    avatar_hash: str = Field(..., description="Avatar hash")
    status_text: str = Field(..., description="Status text")
    status_emoji: str = Field(..., description="Status emoji")
    real_name: str = Field(..., description="Real name")
    display_name: str = Field(..., description="Display name")
    real_name_normalized: str = Field(..., description="Normalized real name")
    display_name_normalized: str = Field(..., description="Normalized display name")
    email: EmailStr = Field(..., description="User email")
    image_original: str = Field(..., description="Original image URL")
    image_24: str = Field(..., description="24x24 pixel image URL")
    image_32: str = Field(..., description="32x32 pixel image URL")
    image_48: str = Field(..., description="48x48 pixel image URL")
    image_72: str = Field(..., description="72x72 pixel image URL")
    image_192: str = Field(..., description="192x192 pixel image URL")
    image_512: str = Field(..., description="512x512 pixel image URL")
    team: str = Field(..., description="Team ID")


class User(BaseModel):
    """User information from Slack API"""
    id: str = Field(..., description="User ID")
    team_id: str = Field(..., description="Team ID")
    name: str = Field(..., description="Username")
    deleted: bool = Field(..., description="Whether user is deleted")
    color: str = Field(..., description="User color")
    real_name: str = Field(..., description="Real name")
    tz: str = Field(..., description="Timezone")
    tz_label: str = Field(..., description="Timezone label")
    tz_offset: int = Field(..., description="Timezone offset in seconds")
    profile: UserProfile = Field(..., description="User profile information")
    is_admin: bool = Field(..., description="Whether user is admin")
    is_owner: bool = Field(..., description="Whether user is owner")
    is_primary_owner: bool = Field(..., description="Whether user is primary owner")
    is_restricted: bool = Field(..., description="Whether user is restricted")
    is_ultra_restricted: bool = Field(..., description="Whether user is ultra restricted")
    is_bot: bool = Field(..., description="Whether user is a bot")
    updated: int = Field(..., description="Last updated timestamp")
    is_app_user: bool = Field(..., description="Whether user is an app user")
    has_2fa: bool = Field(..., description="Whether user has 2FA enabled")


class UserInfoResponse(BaseModel):
    """Response wrapper for user.info API call"""
    ok: bool = Field(..., description="Whether the API call was successful")
    user: User = Field(..., description="User information")
