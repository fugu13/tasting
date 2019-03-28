from tasting import checkpoint, needs


def func():
    pass


def test_functions_unaltered_when_not_tasting():
    assert func == checkpoint("description")(func)
    assert func == needs.qa("reason")(func)


def test_functions_altered_when_tasting(taste):
    assert func != checkpoint("description")(func)
    assert func != needs.qa("reason")(func)


def test_pytest_flag_tastes(testdir):
    testdir.makepyfile(
        """
        from tasting import checkpoint, needs

        def func():
            pass
        
        def test_pytest_flag_tastes():
            assert func != checkpoint("description")(func)
            assert func != needs.qa("reason")(func)
        """
    )

    result = testdir.runpytest("--tasting")
    result.assert_outcomes(passed=1)
