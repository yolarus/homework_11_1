from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(id_info: list, filter_executed_id_info: list) -> None:
    assert filter_by_state(id_info, "EXECUTED") == filter_executed_id_info


def test_filter_by_state_canceled(id_info: list, filter_canceled_id_info: list) -> None:
    assert filter_by_state(id_info, "CANCELED") == filter_canceled_id_info


def test_sort_by_date_ascending(id_info: list, sort_ascending_id_info: list) -> None:
    assert sort_by_date(id_info, False) == sort_ascending_id_info


def test_sort_by_date_descending(id_info: list, sort_descending_id_info: list) -> None:
    assert sort_by_date(id_info) == sort_descending_id_info
