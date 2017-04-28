import unittest
import datafy

import sys; sys.path.insert(0, "../")
import limited_process


class TestLimitedProcess(unittest.TestCase):
    """
    These tests are built against datafy.get, in conjunction with which this module was originally written.

    Unfortunately multiprocessing and requests_mock don't seem to get along, as when a mock is substituted for this
    network request the process hangs. Until/unless I figure out why, this test suite is therefore network dependent.
    """
    def setUp(self):
        self.q = limited_process.q()
        self.test_uri = "https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.csv?accessType=DOWNLOAD"
        self.test_timeout_uri = "https://data.cityofnewyork.us/api/geospatial/pi5s-9p35?method=export&format=Shapefile"
        self.callback = lambda uri, q, kwargs: q.put(datafy.get(uri, **kwargs))

    def test_success(self):
        # See the note above.
        #     with requests_mock.Mocker() as mock:
        #         # Interdict network requests to retrieve data from the localized store instead.
        #         mock.get(self.mock_uri, text='HELLO WORLD')
        result = limited_process.limited_get(
            self.test_uri,
            self.q,
            callback=self.callback,
            timeout=10
        )
        result[0].pop('data')
        expected = [{'filepath': '.', 'mimetype': 'text/csv', 'extension': 'csv'}]
        assert result == expected

    def test_timeout(self):
        assert not limited_process.limited_get(self.test_timeout_uri, self.q, callback=self.callback, timeout=0.1)
