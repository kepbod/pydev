import os.path
import pytest

pytest_plugins = ['helpers_namespace']


@pytest.helpers.register
def data_path(fn):
        return os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'data/' + fn)
