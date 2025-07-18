"""
Team-related type definitions for Slack API
"""

from pydantic import BaseModel, Field, EmailStr


class TeamIcon(BaseModel):
    """Team icon information"""
    image_34: str = Field(..., description="34x34 pixel icon URL")
    image_44: str = Field(..., description="44x44 pixel icon URL")
    image_68: str = Field(..., description="68x68 pixel icon URL")
    image_88: str = Field(..., description="88x88 pixel icon URL")
    image_102: str = Field(..., description="102x102 pixel icon URL")
    image_132: str = Field(..., description="132x132 pixel icon URL")
    image_default: bool = Field(..., description="Whether the icon is the default")


class Team(BaseModel):
    """Team information from Slack API"""
    id: str = Field(..., description="Team ID")
    name: str = Field(..., description="Team name")
    domain: str = Field(..., description="Team domain")
    email_domain: EmailStr = Field(..., description="Email domain for the team")
    icon: TeamIcon = Field(..., description="Team icon information")
    enterprise_id: str = Field(..., description="Enterprise ID if part of an enterprise")
    enterprise_name: str = Field(..., description="Enterprise name if part of an enterprise")


class TeamInfoResponse(BaseModel):
    """Response wrapper for team.info API call"""
    ok: bool = Field(..., description="Whether the API call was successful")
    team: Team = Field(..., description="Team information")