from app.orchestrator.service import OrchestrationService


def test_orchestration_service_end_to_end() -> None:
    service = OrchestrationService()
    result = service.execute_goal("Research top startups in AI and create a report")

    assert result["goal"].startswith("Research top startups")
    assert len(result["plan"]) == 3
    assert len(result["results"]) == 3
    assert "Final Report" in result["final_report"]
