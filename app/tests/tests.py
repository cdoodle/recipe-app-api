class TestClass:
    def test_one(self):
        x = "one"
        assert "n" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")