from src import NameGenerator

def test_name_generator():
    name_generator = NameGenerator()
    name = name_generator.generate()
    assert ' ' in name, "Name should contain a space"
