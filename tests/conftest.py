import pytest
from sphinx.application import Sphinx
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"

@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "roots"

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "sphinx"
    )
