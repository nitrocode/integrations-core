# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest

from .common import POSTGRES_VERSION

requires_over_10 = pytest.mark.skipif(
    POSTGRES_VERSION is None or float(POSTGRES_VERSION) < 10,
    reason='This test is for over 10 only (make sure POSTGRES_VERSION is set)',
)

requires_over_13 = pytest.mark.skipif(
    POSTGRES_VERSION is None or float(POSTGRES_VERSION) < 13,
    reason='This test is for over 13 only (make sure POSTGRES_VERSION is set)',
)
