"""Proof PR 1: Failing test - should be blocked from merge."""

def test_safeguard_system():
    """This test intentionally fails to demonstrate branch protection."""
    assert False, "This test is designed to fail - proving the safeguard works"

def test_main_branch_protected():
    """Verify main branch requires PR."""
    assert True  # This would pass, but the above test fails
