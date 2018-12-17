#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###############################################################################
#                                                                             #
# Copyright (c) 2016 Idiap Research Institute, http://www.idiap.ch/           #
# Contact: beat.support@idiap.ch                                              #
#                                                                             #
# This file is part of the beat.backend.python module of the BEAT platform.   #
#                                                                             #
# Commercial License Usage                                                    #
# Licensees holding valid commercial BEAT licenses may use this file in       #
# accordance with the terms contained in a written agreement between you      #
# and Idiap. For further information contact tto@idiap.ch                     #
#                                                                             #
# Alternatively, this file may be used under the terms of the GNU Affero      #
# Public License version 3 as published by the Free Software and appearing    #
# in the file LICENSE.AGPL included in the packaging of this file.            #
# The BEAT platform is distributed in the hope that it will be useful, but    #
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY  #
# or FITNESS FOR A PARTICULAR PURPOSE.                                        #
#                                                                             #
# You should have received a copy of the GNU Affero Public License along      #
# with the BEAT platform. If not, see http://www.gnu.org/licenses/.           #
#                                                                             #
###############################################################################

class Algorithm:

    def prepare(self, data_loaders):
        data_loader = data_loaders.loaderOf('in2')

        (data, start, end) = data_loader[0]
        self.offset = data['in2'].value

        return True


    def process(self, data_loaders, outputs):
        data_loader = data_loaders.loaderOf('in1')

        for i in range(data_loader.count()):
            (data, start, end) = data_loader[i]

            outputs['out'].write({
                    'value': data['in1'].value + self.offset,
                },
                end
            )

        return True
