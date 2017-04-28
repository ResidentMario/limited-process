"""
This is a small module which defines an API for downloading resources from the web within a time-limited context. In
other words, while `requests.get` allows you to download something off the web, `limited_requests.limited_get` allows
you to download it off the web, but only if it does so successfully within <timeout> seconds.
"""

import multiprocessing as mp


def q():
    return mp.Queue()


def limited_get(uri, q, timeout=60,
                callback=lambda uri: uri,
                # callback=lambda uri, q, kwargs: q.put(datafy.get(uri, **kwargs)),
                **kwargs):
    """
    Implemented a timed request. Note: this function blocks.

    Parameters
    ----------
    uri: str
        The resource URI.
    q: mp.Queue
        An `mp.Queue` object for message passing. For ease of use initialzie using `q = limited_process.q()`.
    timeout: float
        The maximum amount of time that this entire process will get. If the process takes longer than this, a SIGINT
        will be raised to interrupt and kill the process and move on. This, the crux of the whole problem addressed
        by this module, is done in order to avoid getting stuck on inordinately large files (for which sizeout can't
        be specified).
    callback: func
        The function that will be executed. A wrapped datafy.get operation by default, but you can specify your own
        if so inclined.

    Returns
    -------
    Either the result of your callback as applied on the URI, or None.
    """
    p = mp.Process(target=callback, args=(uri, q, kwargs))
    p.start()
    p.join(timeout)
    p.terminate()
    # If the process succeeded the exitcode is 0.
    return q.get() if p.exitcode == 0 else None
