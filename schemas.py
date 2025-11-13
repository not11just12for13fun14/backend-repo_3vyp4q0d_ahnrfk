"""
Database Schemas for TPO Portal

Each Pydantic model maps to a MongoDB collection (lowercased class name).
"""
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional

class Studentplaced(BaseModel):
    name: str = Field(..., description="Student full name")
    branch: str = Field(..., description="Department/branch e.g., CSE, ECE")
    company: str = Field(..., description="Company name")
    role: str = Field(..., description="Offered role")
    ctc: str = Field(..., description="CTC or stipend offered, display string")
    year: int = Field(..., description="Placement year")
    avatar_url: Optional[HttpUrl] = Field(None, description="Optional avatar URL")

class Company(BaseModel):
    name: str = Field(..., description="Company name")
    visits: int = Field(1, ge=0, description="Number of campus visits/drive count")
    roles: List[str] = Field(default_factory=list, description="Roles offered")
    logo_url: Optional[HttpUrl] = Field(None, description="Logo URL")
    website: Optional[HttpUrl] = Field(None, description="Company website")

class Teammember(BaseModel):
    name: str = Field(..., description="TPO member name")
    designation: str = Field(..., description="Role/designation in TPO")
    email: Optional[str] = Field(None, description="Contact email")
    phone: Optional[str] = Field(None, description="Contact number")
    linkedin: Optional[HttpUrl] = Field(None, description="LinkedIn profile URL")
    avatar_url: Optional[HttpUrl] = Field(None, description="Profile image URL")
