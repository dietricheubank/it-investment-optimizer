# IT Investment Optimizer

Exact budget-constrained project selection with dependencies using exhaustive search for small candidate sets.

## Run

Requires Python 3.11+ and no third-party dependencies.

```bash
cd it-investment-optimizer
python app.py
python -m unittest discover -s tests -v
```

## Design / scope

This standalone public project includes a Python implementation, a JSON command-line runner, synthetic examples, and automated checks in GitHub Actions.

An exact exponential search is intentional for <=20 projects; it is not appropriate for large portfolios. Values are arbitrary utility points, not guaranteed ROI.

## License

[MIT](LICENSE).

## JSON scenario runner

```bash
python cli.py examples/sample_portfolio.json
```

The scenario contains a numeric budget and project records with unique codes, nonnegative integer costs and value points, and optional dependencies. The solver enumerates valid combinations and maximizes total value, breaking ties by lower cost. For more than 20 projects, use a dedicated optimizer rather than exhaustive enumeration. These are **illustrative utility points**, not guaranteed ROI or a validated financial model.

**Development:** `python -m unittest discover -s tests -v`. CI runs the suite on each push and pull request.

## Portfolio sensitivity analysis

The new [scenario analysis module](scenarios.py) produces a **budget frontier** over multiple spending levels and measures how much the optimal portfolio value changes if a project (and any projects depending on it) is excluded. See [scenario regression tests](tests/test_scenarios.py).

This adds useful decision analysis, but does not model uncertainty, multi-period spending or real investment returns. Project values remain fictional utility points.
