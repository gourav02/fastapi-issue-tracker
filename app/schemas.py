from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
# str, Enum means the class inherits from both str and Enum. This makes the enum values behave like strings while retaining enum benefits.
class IssueStatus(str,Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class issuePriority(str,Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class issueCreate(BaseModel):
    title: str = Field(min_length=3 , max_length=100)
    description: str = Field(min_length=5 , max_length=1000)
    priority: issuePriority = issuePriority.MEDIUM

class issueUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3 , max_length=100)
    description: Optional[str] = Field(None, min_length=5 , max_length=1000)
    priority: Optional[issuePriority] = None
    status: Optional[IssueStatus] = None

class issueResponse(BaseModel):
    id: str
    title: str
    description: str
    priority: issuePriority
    status: IssueStatus
