#
# Copyright (c) 2013-2018 Quarkslab.
# This file is part of IRMA project.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the top-level directory
# of this distribution and at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# No part of the project, including this file, may be copied,
# modified, propagated, or distributed except according to the
# terms contained in the LICENSE file.

from marshmallow import fields, Schema, post_load, pre_load

from .fileext import FileCliSchemaV3, FileCliSchemaV2
from .scan import Scan


# {{{ V3

class SRFileCliSchemaV3(FileCliSchemaV3):
    size = fields.Pluck('FileSchema', 'size', dump_only=True, attribute="file")

    @pre_load
    def rm_size(self, data):
        del data['size']
        return data


class SRScanSchemaV3(Schema):
    id = fields.UUID(attribute="external_id")
    date = fields.Number()
    status = fields.Integer(allow_none=True)

    probes_finished = fields.Integer()
    probes_total = fields.Integer()

    results = fields.Nested(
        SRFileCliSchemaV3,
        attribute="files_ext",
        many=True,
        only=(
            'id',
            'status',
            'name',
            'path',
            'file', 'file_sha256', 'size',
        )
    )

    @post_load
    def make_object(self, data):
        return Scan(**data)


class ScanRetrievalCodeSchemaV3(Schema):
    id = fields.String(attribute="external_id")

    @post_load
    def make_object(self, data):
        return ScanRetrievalCode(**data)

# }}}


# {{{ V2

class SRFileCliSchemaV2(FileCliSchemaV2):
    size = fields.Pluck('FileSchema', 'size', dump_only=True, attribute="file")

    @pre_load
    def rm_size(self, data):
        del data['size']
        return data


class SRScanSchemaV2(Schema):
    id = fields.UUID(attribute="external_id")
    date = fields.Number()
    status = fields.Integer(allow_none=True)

    probes_finished = fields.Integer()
    probes_total = fields.Integer()

    results = fields.Nested(
        SRFileCliSchemaV2,
        attribute="files_ext",
        many=True,
        only=('id', 'name', 'size', 'path', 'status')
    )

    @post_load
    def make_object(self, data):
        return Scan(**data)


class ScanRetrievalCodeSchemaV2(Schema):
    id = fields.String(attribute="external_id")

    @post_load
    def make_object(self, data):
        return ScanRetrievalCode(**data)

# }}}


# {{{ OBJECTS

class ScanRetrievalCode:

    def __init__(self, external_id):
        self.external_id = external_id

    @property
    def id(self):
        return self.external_id

    def __eq__(self, other):
        return isinstance(other, ScanRetrievalCode) and self.id == other.id

    def __neq__(self, other):
        return not (self == other)

# }}}
