"""
Team-related type definitions for Slack API
"""

from pydantic import BaseModel, Field


class TeamIcon(BaseModel):
    """Team icon information"""
    image_default: bool = Field(..., description="Whether the icon is the default")
    image_34: str = Field(..., description="34x34 pixel icon URL")
    image_44: str = Field(..., description="44x44 pixel icon URL")
    image_68: str = Field(..., description="68x68 pixel icon URL")
    image_88: str = Field(..., description="88x88 pixel icon URL")
    image_102: str = Field(..., description="102x102 pixel icon URL")
    image_230: str = Field(..., description="230x230 pixel icon URL")
    image_132: str = Field(..., description="132x132 pixel icon URL")


class Team(BaseModel):
    """Team information from Slack API"""
    id: str = Field(..., description="Team ID")
    name: str = Field(..., description="Team name")
    url: str = Field(..., description="Team URL")
    domain: str = Field(..., description="Team domain")
    email_domain: str = Field(..., description="Email domain for the team")
    icon: TeamIcon = Field(..., description="Team icon information")
    avatar_base_url: str = Field(..., description="Base URL for team avatars")
    is_verified: bool = Field(..., description="Whether the team is verified")
    lob_sales_home_enabled: bool = Field(..., description="Whether LOB sales home is enabled")
    is_sfdc_auto_slack: bool = Field(..., description="Whether SFDC auto Slack is enabled")


class TeamInfoResponse(BaseModel):
    """Response wrapper for team.info API call"""
    ok: bool = Field(..., description="Whether the API call was successful")
    team: Team = Field(..., description="Team information")