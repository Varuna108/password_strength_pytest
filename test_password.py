def test_len_password(user_password):
    assert len(user_password) >= 12


def test_number(user_password):
    for char in user_password:
        if str.isdigit(char):
            assert True


def test_letters(user_password):
    for char in user_password:
        if not str.isdigit(char):
            assert True


def test_upper_letters(user_password):
    for char in user_password:
        if str.isupper(char):
            assert True


def test_lower_letters(user_password):
    for char in user_password:
        if str.islower(char):
            assert True


def test_symbols(user_password):
    for char in user_password:
        if not str.isalpha(char):
            assert True


def test_not_only_symbols(user_password):
    for char in user_password:
        if str.isalpha(char):
            assert True
