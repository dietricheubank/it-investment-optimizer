# Investment selection workflow

This is an educational workflow, not an automated funding approval system.

```mermaid
flowchart TD
  A[Define strategic outcomes] --> B[Capture candidate projects]
  B --> C[Estimate value and cost]
  C --> D[Identify dependencies]
  D --> E{Validate scenario?}
  E -- No --> B
  E -- Yes --> F[Enumerate feasible subsets]
  F --> G[Apply budget constraint]
  G --> H[Maximize total value]
  H --> I[Tie-break on lower cost]
  I --> J[Review qualitative risks and capacity]
  J --> K{Sponsor approves?}
  K -- No --> B
  K -- Yes --> L[Record investment decision]
```

The current `app.py` performs the exact small-scale computation in steps F–I. It does **not** automatically execute or approve projects. The review and authorization steps are governance guidance only.

## Example inputs

Use `examples/sample_portfolio.json` with `python cli.py examples/sample_portfolio.json`. Values are fictional utility points. The solver is exponential and accepts at most 20 candidate projects.
