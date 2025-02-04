# -*- coding: utf-8 -*-
#
# File : echotorch/data/datasets/__init__.py
# Description : Dataset subpackages init file
# Date : 3th of March, 2021
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
# Copyright Nils Schaetti <nils.schaetti@unine.ch>

# Imports datasets
from echotorch.data.datasets.LogisticMapDataset import LogisticMapDataset

__all__ = [
   # Datasets
   'CopyTaskDataset', 'DatasetComposer', 'DiscreteMarkovChainDataset', 'FromCSVDataset', 'HenonAttractor',
   'LambdaDataset', 'LatchTaskDataset', 'LogisticMapDataset', 'LorenzAttractor', 'MackeyGlassDataset', 'MemTestDataset',
   'NARMADataset', 'RosslerAttractor', 'SinusoidalTimeseries', 'PeriodicSignalDataset', 'RandomSymbolDataset',
   'ImageToTimeseries', 'MarkovChainDataset', 'MixedSinesDataset', 'RepeatTaskDataset',
   'TimeseriesBatchSequencesDataset', 'TransformDataset', 'TripletBatching', 'DelayDataset', 'EchoDataset',
   'MackeyGlass2DDataset'
]
