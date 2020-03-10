
def test_with_breakpoint():
    import pudb; pu.db  # breakpoint actually
    assert False
