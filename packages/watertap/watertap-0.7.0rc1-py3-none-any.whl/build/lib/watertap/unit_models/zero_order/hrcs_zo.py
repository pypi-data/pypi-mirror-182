###############################################################################
# WaterTAP Copyright (c) 2021, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory, Oak Ridge National
# Laboratory, National Renewable Energy Laboratory, and National Energy
# Technology Laboratory (subject to receipt of any required approvals from
# the U.S. Dept. of Energy). All rights reserved.
#
# Please see the files COPYRIGHT.md and LICENSE.md for full copyright and license
# information, respectively. These files are also available online at the URL
# "https://github.com/watertap-org/watertap/"
#
###############################################################################
"""
This module contains a zero-order representation of a high-rate contact stabilization unit.
"""

from idaes.core import declare_process_block_class
from watertap.core import build_sido_reactive, constant_intensity, ZeroOrderBaseData

# Some more information about this module
__author__ = "Marcus Holly"


@declare_process_block_class("HRCSZO")
class HRCSZOData(ZeroOrderBaseData):
    """
    Zero-Order model for a high-rate contact stabilization (HR-CS) unit.
    """

    CONFIG = ZeroOrderBaseData.CONFIG()

    def build(self):
        super().build()

        self._tech_type = "hrcs"

        build_sido_reactive(self)
        constant_intensity(self)
