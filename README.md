# It Investment Optimizer

Exact budget-constrained project selection with dependencies using exhaustive search for small candidate sets.

## Run

Requires Python 3.11+ and no third-party dependencies.

```bash
cd it-investment-optimizer
python app.py
python -m unittest discover -s tests -v
```

## Design / scope

This is an **independent starter project** staged under the public portfolio repository until a matching standalone GitHub repository can be created. The implementation is synthetic by default; no integrations with private systems, employer APIs, secrets, or confidential data.

An exact exponential search is intentional for <=20 projects; it is not appropriate for large portfolios. Values are arbitrary utility points, not guaranteed ROI.

## Next steps

- Extend coverage for invalid input and edge cases.
- Document real-world threat models, operational constraints, and test fixtures.
- Publish a dedicated repository without exposing private configurations.
- Add versioned sample data, user-facing CLI, and packaging when project grows.

License: MIT (parent repository).


## Repository status

This is the standalone public project. It is developed independently with GitHub Actions CI.

## JSON scenario runner

```bash
python cli.py examples/sample_portfolio.json
```

The scenario contains a numeric budget and project records with unique codes, nonnegative integer costs and value points, and optional dependencies. The solver enumerates valid combinations and maximizes total value, breaking ties by lower cost. For more than 20 projects, use a dedicated optimizer rather than exhaustive enumeration. These are **illustrative utility points**, not guaranteed ROI or a validated financial model.

**Development:** `python -m unittest discover -s tests -v`. CI runs the suite on each push and pull request.
