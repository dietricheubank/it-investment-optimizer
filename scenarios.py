"""Budget sensitivity and inclusion-exclusion diagnostics for small portfolios."""
from app import Project, optimize

def budget_frontier(projects: list[Project], budgets: list[int]) -> list[dict]:
    if any(type(b) is not int or b < 0 for b in budgets):
        raise ValueError("budgets must be nonnegative integers")
    return [
        {"budget": b, "selected": codes, "value": value, "spent": spent}
        for b in budgets
        for codes, value, spent in [optimize(projects, b)]
    ]

def project_marginal_impact(projects: list[Project], budget: int, code: str) -> dict:
    """Difference between unrestricted optimum and optimum where code cannot be selected.
    
    If other projects depend on it, they are excluded too, transitively.
    """
    if code not in {p.code for p in projects}:
        raise ValueError("project does not exist")
    full_codes, full_value, _ = optimize(projects, budget)
    excluded = {code}
    changed = True
    while changed:
        old = len(excluded)
        excluded.update(p.code for p in projects if any(d in excluded for d in p.dependencies))
        changed = len(excluded) != old
    reduced = [p for p in projects if p.code not in excluded]
    _, without_value, _ = optimize(reduced, budget)
    return {"code": code, "chosen_in_optimum": code in full_codes,
            "value_without": without_value, "optimal_value": full_value,
            "marginal_value": full_value - without_value,
            "removed_with_dependents": sorted(excluded)}
