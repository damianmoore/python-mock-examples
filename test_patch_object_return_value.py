from unittest import mock

from example_class import ExampleClass


@mock.patch.object(ExampleClass, 'get_results', return_value=['mocked value'])
def test_decorator(mock_example_class):
    example = ExampleClass()
    assert example.get_results() == ['mocked value']


def test_context_manager():
    example = ExampleClass()
    with mock.patch.object(ExampleClass, 'get_results', return_value=['mocked value']):
        assert example.get_results() == ['mocked value']


if __name__ == '__main__':
    test_decorator()
    test_context_manager()
    print('Success')
