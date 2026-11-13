"""Run an exact small project selection scenario from a JSON file."""
import argparse
import json
from pathlib import Path
from app import Project, optimize

def load_scenario(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("projects"), list):
        raise ValueError("Expected object containing projects array")
    projects = []
    for p in data["projects"]:
        projects.append(Project(
            code=str(p["code"]),
            cost=int(p["cost"]),
            value=int(p["value"]),
            dependencies=tuple(p.get("dependencies", [])),
        ))
    budget = int(data["budget"])
    return projects, budget

def main():
    parser = argparse.ArgumentParser(description="Select maximum-value projects within a budget")
    parser.add_argument("scenario", help="JSON file containing projects and budget")
    args = parser.parse_args()
    projects, budget = load_scenario(args.scenario)
    selected, value, cost = optimize(projects, budget)
    print(json.dumps({"selected": selected, "total_value": value,
                      "total_cost": cost, "budget": budget}, indent=2))

if __name__ == "__main__":
    main()
