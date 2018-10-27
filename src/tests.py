from nQueens import calculate


class TestNQueens(object):
    def test_one(self):
        assert calculate(1) == 1

    def test_two(self):
        assert calculate(2) == 0

    def test_three(self):
        assert calculate(3) == 0

    def test_four(self):
        assert calculate(4) == 2

    def test_five(self):
        assert calculate(5) == 10

    def test_six(self):
        assert calculate(6) == 4

    def test_seven(self):
        assert calculate(7) == 40

    def test_eight(self):
        assert calculate(8) == 92

    def test_nine(self):
        assert calculate(9) == 352

    def test_ten(self):
        assert calculate(10) == 724

    def test_eleven(self):
        assert calculate(11) == 2680