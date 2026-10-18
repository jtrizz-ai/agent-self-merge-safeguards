# Agent Self-Merge Safeguards

This repository demonstrates safeguards for agent-driven self-merge workflows.

## Safeguards

1. **Branch Protection**: Main branch requires PR, passes required checks, no force pushes
2. **Code Ownership**: CODEOWNERS ensures files are owned by authorized maintainers
3. **Proof PRs**: Three test PRs validate the safeguard system

## Proof PRs

- [PR 1: Failing Test](https://github.com/jtrizz-ai/agent-self-merge-safeguards/pull/1) - Should be blocked from merge
- [PR 2: Workflow Edit](https://github.com/jtrizz-ai/agent-self-merge-safeguards/pull/2) - Should be blocked from merge
- [PR 3: Clean PR](https://github.com/jtrizz-ai/agent-self-merge-safeguards/pull/3) - Should auto-merge
