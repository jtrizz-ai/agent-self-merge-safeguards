# Repo Safeguards Summary

## Branch Protection Rules (main)
- **PR Required**: All changes must go through pull requests
- **Required Checks**: Status checks must pass before merge
- **No Force Pushes**: Force pushes are disabled
- **Code Owner Reviews**: At least 1 approving review required
- **Dismiss Stale Reviews**: Old reviews are dismissed on new pushes
- **Enforce Admins**: Rules apply to repository administrators too
- **No Branch Deletion**: Branch cannot be deleted

## CODEOWNERS
All files require approval from `@jtrizz-ai` (Jonathan Rizzo)

## Proof PRs
| PR | Description | Expected Behavior |
|----|-------------|-------------------|
| #1 | Failing test | Blocked - test fails |
| #2 | Workflow edit | Blocked - requires review |
| #3 | Clean merge | Auto-merges after approval |
