from scanner import scan_port, scan_ports


def test_scan_ports_returns_results():
    results = scan_ports("127.0.0.1", [22, 80])

    assert isinstance(results, dict)
    assert 22 in results
    assert 80 in results


def test_scan_port_returns_boolean():
    result = scan_port("127.0.0.1", 22)

    assert isinstance(result, bool)