import pytest
import re
from decorateme import abcd
from decorateme.abcd import CodeIncompleteError

raises = pytest.raises
warns = pytest.warns


class TestAbcd:
    def test_auto_obj(self):
        @abcd.auto_obj()
        class X:
            def __init__(self, s):
                self.s = s

        x = X(5)
        assert str(x) == "X(s=5)"
        assert (
            re.compile(r"X\(s=5 @ 0x[0-9a-h]+\)").fullmatch(repr(x)) is not None
        ), f"repr is {repr(x)}"
        assert hash(x) == hash((5,))
        assert x == X(5)
        assert x != X(6)

    def test_immutable(self):
        @abcd.immutable
        class X:
            __slots__ = ["s"]

            def __init__(self, s):
                self.s = s

        x = X(5)
        with raises(AttributeError):
            x.s = 5

    def test_float_type(self):
        @abcd.float_type("s")
        class X:
            def __init__(self, s):
                self.s = s

        x = X(5)
        # noinspection PyTypeChecker
        assert float(x) == 5.0

    def test_status(self):
        @abcd.status(abcd.CodeStatus.Incomplete)
        def x():
            pass

        with raises(CodeIncompleteError):
            x()

        @abcd.status(abcd.CodeStatus.Deprecated)
        def x():
            pass

        with warns(DeprecationWarning):
            x()

        @abcd.status(abcd.CodeStatus.Immature)
        def y():
            pass

        with warns(abcd.ImmatureWarning):
            y()

        @abcd.status(abcd.CodeStatus.Stable)
        def z():
            pass

        with warns(None):
            z()

    """
    @pytest.mark.timeout(2)  # TODO nope
    def test_timeout(self):
        @abcd.auto_timeout(1)
        def run():
            for i in list(range(0, 100000000)):
                if i % 2 == 0:
                    i -= 1
        # TODO not great
        if os.name.lower() == 'nt':
            with raises(NotImplementedError):
                run()
        else:
            with raises(TimeoutError):
                run()
    """


if __name__ == "__main__":
    pytest.main()
