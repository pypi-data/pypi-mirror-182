# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup

with open("README.md") as f:
    readme = f.read()


setup(
    name="toehold",
    version='0.0.1',
    description="Predict & Optimization of Toehold switch.",
    long_description=readme,
    author="Weijie Yin",
    url="https://github.com/Bruce-ywj/toehold",
    license="MIT",
    packages=["toehold",],
    zip_safe=True,
)