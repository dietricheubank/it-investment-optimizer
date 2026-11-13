import unittest
from app import Project
from scenarios import budget_frontier, project_marginal_impact

DATA=[Project("A",6,10),Project("B",5,8),Project("C",4,9,("A",)),Project("D",3,4)]
class ScenarioTests(unittest.TestCase):
    def test_frontier_monotonic(self):
        result=budget_frontier(DATA,[0,3,5,10,15])
        self.assertEqual([r["value"] for r in result],sorted(r["value"] for r in result))
        self.assertEqual(result[3]["selected"],["A","C"])
    def test_dependency_cascade(self):
        result=project_marginal_impact(DATA,10,"A")
        self.assertEqual(result["removed_with_dependents"],["A","C"])
        self.assertGreater(result["marginal_value"],0)
    def test_invalid(self):
        with self.assertRaises(ValueError):
            budget_frontier(DATA,[-1])
        with self.assertRaises(ValueError):
            project_marginal_impact(DATA,10,"missing")
if __name__=="__main__": unittest.main()
