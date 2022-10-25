# SPDX-FileCopyrightText: 2020 - 2022 Intel Corporation
#
# SPDX-License-Identifier: Proprietary

from setuptools import setup
import os

pkg_version = os.getenv("DPCPP_LLVM_SPIRV_VERSION", "unknown")

setup(
    name="dpcpp_llvm_spirv",
    version=pkg_version,
    author="Intel Corp.",
    author_email="scripting@intel.com",
    description="llvm-spirv helper",
    long_description="Python package vendoring llvm-spirv executable from Intel(R) oneAPI DPC++ compiler package",
    url="https://github.com/IntelPython/dpcpp-llvm-spirv",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license="Intel End User License Agreement for Developer Tools"
)
