from src.pre_built.counter import count_ocurrences

mocked_path = 'data/jobs.csv'
mocked_word = 'python'


def test_counter():
    expected = 1639
    result = count_ocurrences(mocked_path, mocked_word)
    assert result == expected
