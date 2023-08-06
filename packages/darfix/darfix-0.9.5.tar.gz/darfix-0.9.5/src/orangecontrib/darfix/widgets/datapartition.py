# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/


__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "28/09/2020"


from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output
from darfix.gui.dataPartitionWidget import DataPartitionWidget
from darfix.core.process import DataPartition


class DataPartitionWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "partition data"
    icon = "icons/filter.png"
    want_main_area = False
    ewokstaskclass = DataPartition

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)

    # Outputs
    class Outputs:
        dataset = Output("dataset", tuple)

    bins = Setting(str(), schema_only=True)
    bottom_bins = Setting(str(), schema_only=True)
    top_bins = Setting(str(), schema_only=True)

    def __init__(self):
        super().__init__()

        self._widget = DataPartitionWidget(parent=self)
        self._widget.sigComputed.connect(self._sendSignal)
        self.controlArea.layout().addWidget(self._widget)

    @Inputs.dataset
    def setDataset(self, _input):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(*dataset)
            if update is None:
                self.open()
            if self.bins:
                self._widget.bins.setText(self.bins)
            if self.bottom_bins:
                self._widget.bottomBinsNumber.setText(self.bottom_bins)
            if self.top_bins:
                self._widget.topBinsNumber.setText(self.top_bins)

    def _sendSignal(self):
        self.Outputs.dataset.send(((self,) + self._widget.getDataset(), None))
        self.bins = self._widget.bins.text()
        self.bottom_bins = self._widget.bottomBinsNumber.text()
        self.top_bins = self._widget.topBinsNumber.text()
        self.close()

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)
