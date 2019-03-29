import tasting


def test_finds_direct_parent(taste, needs, checkpoint, simple_nesting):
    simple_nesting()
    assert any(
        result.checkpoint == checkpoint and result.needs == needs
        for result in tasting.results()
    )

