from clinikehr.pagination import CursorPage, paginate


def test_yields_every_row_across_every_page_in_order():
    pages = {
        None: CursorPage(data=[1, 2], has_more=True, next_cursor="p2"),
        "p2": CursorPage(data=[3, 4], has_more=True, next_cursor="p3"),
        "p3": CursorPage(data=[5], has_more=False, next_cursor=None),
    }
    assert list(paginate(lambda cursor: pages[cursor])) == [1, 2, 3, 4, 5]


def test_fetches_lazily_breaking_early_never_triggers_a_later_page():
    calls = []

    def fetch_page(cursor):
        calls.append(cursor)
        if cursor is None:
            return CursorPage(data=[1, 2], has_more=True, next_cursor="p2")
        return CursorPage(data=[3, 4], has_more=False, next_cursor=None)

    first = []
    for row in paginate(fetch_page):
        first.append(row)
        if len(first) == 1:
            break

    assert first == [1]
    assert calls == [None]


def test_single_page_yields_and_stops():
    page = CursorPage(data=["a", "b"], has_more=False, next_cursor=None)
    assert list(paginate(lambda cursor: page)) == ["a", "b"]


def test_empty_first_page_yields_nothing():
    page = CursorPage(data=[], has_more=False, next_cursor=None)
    assert list(paginate(lambda cursor: page)) == []


def test_has_more_true_but_null_cursor_stops_rather_than_looping_forever():
    page = CursorPage(data=[1], has_more=True, next_cursor=None)
    assert list(paginate(lambda cursor: page)) == [1]
