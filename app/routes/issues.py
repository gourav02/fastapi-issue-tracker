from fastapi import APIRouter, status
from ..schemas import issueResponse, issueCreate, issueResponse, issueUpdate
from ..storage import load_data, save_data
import uuid

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get('/', response_model=list[issueResponse])
def read_issues():
    return load_data()

@router.post('/', response_model=issueResponse, status_code=status.HTTP_201_CREATED)
def create_issue(issue: issueCreate):
    issues = load_data()
    new_issue = {
        "id": str(uuid.uuid4()),
        "title": issue.title,
        "description": issue.description,
        "priority": issue.priority,
        "status": "open"
    }
    issues.append(new_issue)
    save_data(issues)
    return new_issue

@router.put("/{issue_id}", response_model=issueResponse)
def update_issue(issue_id: str, payload: issueUpdate):
    """Update an existing issue by ID."""
    issues = load_data()

    for issue in issues:
        if issue["id"] == issue_id:
            if payload.title is not None:
                issue["title"] = payload.title
            if payload.description is not None:
                issue["description"] = payload.description
            if payload.priority is not None:
                issue["priority"] = payload.priority.value
            if payload.status is not None:
                issue["status"] = payload.status.value

            save_data(issues)
            return issue

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Issue not found"
    )


@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: str):
    """Delete an issue by ID."""
    issues = load_data()

    for i, issue in enumerate(issues): #enumerate() adds an index counter to an iterable, returning pairs of (index, value). It's used when you need both the item and its position.
        if issue["id"] == issue_id:
            issues.pop(i)
            save_data(issues)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Issue not found"
    )
