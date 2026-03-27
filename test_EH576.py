from EH576 import clean_name, valid_email_cheker, add_rating, get_average_rating

def test_clean_name():
    assert clean_name("  alice smith ") == "Alice Smith"


def test_email():
    assert valid_email_cheker("test@email.com") is True


def test_average(tmp_path):
    file = tmp_path / "ratings.csv"
    add_rating("Levi", 8, file)
    add_rating("eddie", 6, file)
    assert get_average_rating(file) == 7.0