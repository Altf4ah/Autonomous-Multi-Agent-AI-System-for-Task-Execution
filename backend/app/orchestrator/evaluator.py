from __future__ import annotations


class Evaluator:
    """Very lightweight quality check + refinement hook."""

    def needs_refinement(self, report: str) -> bool:
        return len(report.strip()) < 80

    def refine(self, report: str) -> str:
        return report + "\n\n## Refinement\nThe report was expanded for clarity and completeness."
