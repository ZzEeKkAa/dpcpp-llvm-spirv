# SPDX-FileCopyrightText: 2020 - 2022 Intel Corporation
#
# SPDX-License-Identifier: Proprietary

import os


def get_llvm_spirv_path():
    """Returns the path to llvm-spirv executable
    vendored in this package.
    """

    result = os.path.dirname(__file__) + "/llvm-spirv"

    return result
