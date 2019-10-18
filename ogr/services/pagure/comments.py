# MIT License
#
# Copyright (c) 2018-2019 Red Hat, Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import datetime

from ogr.abstract import IssueComment, PRComment


# TODO: Keep reference to (ogr's) Issue/PR


class PagureIssueComment(IssueComment):
    def __init__(self, raw_comment: dict = None, **kwargs) -> None:
        if raw_comment is not None:
            super().__init__(
                comment=raw_comment["comment"],
                author=raw_comment["user"]["name"],
                created=datetime.datetime.fromtimestamp(
                    int(raw_comment["date_created"])
                ),
                edited=None,
            )
        else:
            super().__init__(**kwargs)

    def __str__(self) -> str:
        return "Pagure" + super().__str__()


class PagurePRComment(PRComment):
    def __init__(self, raw_comment: dict = None, **kwargs) -> None:
        if raw_comment is not None:
            super().__init__(
                comment=raw_comment["comment"],
                author=raw_comment["user"]["name"],
                created=datetime.datetime.fromtimestamp(
                    int(raw_comment["date_created"])
                ),
                edited=datetime.datetime.fromtimestamp(int(raw_comment["edited_on"]))
                if raw_comment["edited_on"]
                else None,
            )
        else:
            super().__init__(**kwargs)

    def __str__(self) -> str:
        return "Pagure" + super().__str__()
