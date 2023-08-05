#
# Copyright 2016 The BigDL Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from abc import abstractmethod, ABCMeta


class Trainable(metaclass=ABCMeta):
    """The base behavior of a Pytorch trainer

    All runners should inherit `Trainer`` as the worker interface
    and implement the following APIs:

    - ``train_epochs``
    - ``validate``
    - ``predict``

    """

    @abstractmethod
    def train_epochs(self, **kwargs):
        pass

    @abstractmethod
    def predict(self, **kwargs):
        pass

    @abstractmethod
    def validate(self, **kwargs):
        pass
