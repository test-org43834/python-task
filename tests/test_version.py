import example.version

def test_version_returns_consistent_version_number() -> None:
	assert example.version.version() == example.version.version()
