from unittest import mock

from example_class import ExampleClass


def mock_fetch_results(self):
    # This is our fake method that we will patch into the ExampleClass
    self.results.append('mocked value')


@mock.patch.object(ExampleClass, 'fetch_results', mock_fetch_results)
def test_decorator():
    example = ExampleClass()
    example.fetch_results()
    assert example.get_results() == ['mocked value']


def test_context_manager():
    example = ExampleClass()
    with mock.patch.object(ExampleClass, 'fetch_results', mock_fetch_results):
        example.fetch_results()
    assert example.get_results() == ['mocked value']


if __name__ == '__main__':
    test_decorator()
    test_context_manager()
    print('Success')
