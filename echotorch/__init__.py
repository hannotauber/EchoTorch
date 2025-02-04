# -*- coding: utf-8 -*-
#
# File : echotorch/__init__.py
# Description : EchoTorch package init file.
# Date : 26th of January, 2018
#
# This file is part of EchoTorch.  EchoTorch is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Nils Schaetti, University of Neuchâtel <nils.schaetti@unine.ch>


# Imports
import pkg_resources
from pkg_resources import parse_version

# BaseTensors
from .base_tensors import BaseTensor, CharBaseTensor, DoubleBaseTensor, ByteBaseTensor, FloatBaseTensor
from .base_tensors import BFloat16Tensor, HalfBaseTensor

# DataTensors
from .data_tensors import DataTensor, DataIndexer

# TimeTensors
from .timetensors import TimeTensor, CharTimeTensor, DoubleTimeTensor, ByteTimeTensor, FloatTimeTensor
from .timetensors import BFloat16Tensor, HalfTimeTensor

# Base operations
from .base_ops import timetensor, sparse_coo_timetensor, as_timetensor, as_strided, from_numpy, zeros, zeros_like
from .base_ops import ones, ones_like, arange, linspace, logspace, empty, empty_like, empty_strided, full, full_like
from .base_ops import quantize_per_timetensor, quantize_per_channel, dequantize, complex, polar
from .base_ops import cat, tcat, rand
from .base_ops import tindex_select, randn

# Stat operations
from .stat_ops import tmean, tstd, tvar, cov, cor

# ACC operations
from . import acf

# Timeseries operations
from .series_ops import diff

# Nodes
from .nodes import Node


# Min Torch version
MIN_TORCH_VERSION = '1.9.0'


# Try import torch
try:
    # pylint: disable=wrong-import-position
    import torch
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "No module named 'torch', and echotorch depends on PyTorch "
        "(aka 'torch'). "
        "Visit https://pytorch.org/ for installation instructions."
    )
# end try

# Get Torch version
torch_version = pkg_resources.get_distribution('torch').version

# Torch version is too old
if parse_version(torch_version) < parse_version(MIN_TORCH_VERSION):
    # Message
    msg = (
        'echotorch depends on a newer version of PyTorch (at least {req}, not '
        '{installed}). Visit https://pytorch.org for installation details'
    )

    # Import warning
    raise ImportWarning(msg.format(req=MIN_TORCH_VERSION, installed=torch_version))
# end if


# All echotorch's modules
__all__ = [
    # 'esn', 'datasets', 'evaluation', 'models', 'nn', 'transforms', 'utils', 'fit', 'eval',
    # 'cross_val_score', 'copytask', 'discrete_markov_chain', 'csv_file', 'henon',
    # 'delaytask', 'cross_eval', 'segment_series', 'cycle_with_jumps', 'matlab', 'normal', 'uniform',
    # 'cycle_with_jumps_generator', 'matlab_generator', 'normal_generator', 'uniform_generator', 'conceptor', 'cone',
    # 'czero', 'cidentity', 'OR', 'AND', 'NOT', 'PHI', 'conceptor_set', 'csim', 'csimilarity', 'autocorrelation_coefs',
    # 'cov', 'autocorrelation_function', 'acc',
    # Submodels
    # 'data', 'models', 'nn', 'skecho', 'transforms', 'utils', 'viz',
    # BaseTensors
    'BaseTensor',
    'ByteBaseTensor', 'CharBaseTensor', 'HalfBaseTensor', 'DoubleBaseTensor', 'FloatBaseTensor',
    # DataTensors
    'DataTensor', 'DataIndexer',
    # TimeTensors and base ops
    'TimeTensor', 'cat', 'tcat', 'tcat', 'tindex_select', 'rand', 'randn',
    'ByteTimeTensor', 'CharTimeTensor', 'HalfTimeTensor', 'DoubleTimeTensor', 'FloatTimeTensor',
    # Creation ops
    'timetensor', 'sparse_coo_timetensor', 'as_timetensor', 'as_strided', 'from_numpy', 'zeros', 'zeros_like',
    'ones', 'ones_like', 'arange', 'linspace', 'logspace', 'empty', 'empty_like', 'empty_strided', 'full', 'full_like',
    'quantize_per_timetensor', 'quantize_per_channel', 'dequantize', 'complex', 'polar',
    # Stats ops
    'tmean', 'tstd', 'cov', 'cor',
    # Series ops
    'diff',
    # ACC ops
    'acf',
]
