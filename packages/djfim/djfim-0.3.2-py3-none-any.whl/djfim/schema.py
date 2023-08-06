# -*- python -*-
#
# Copyright 2021, 2022 Cecelia Chen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# djfim.schema

#from dmprj.engineering.schema.bief import BIEFEntity


class NormalizedPath(object):
    '''
    provide normalized path/URI
    '''

    FMT_APP_LABEL = 'app={app_label}'
    FMT_MOD_NAME  = 'model={model_name}'
    FMT_ANCHOR    = 'pk={anchor}'

    def __str__(self):
        SEP = ','
        uri = [
            self.FMT_ANCHOR.format(**self.data),
            self.FMT_MOD_NAME.format(**self.data),
            self.FMT_APP_LABEL.format(**self.data),
        ]
        return SEP.join(uri)
