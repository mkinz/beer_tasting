from main_app import do_something

class TestMainApp:
    def test_do_something(self):
        dut = do_something()
        assert dut == "I did something"