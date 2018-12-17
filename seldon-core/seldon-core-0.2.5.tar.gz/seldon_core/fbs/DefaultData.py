# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class DefaultData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsDefaultData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DefaultData()
        x.Init(buf, n + offset)
        return x

    # DefaultData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DefaultData
    def Names(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # DefaultData
    def NamesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # DefaultData
    def Tensor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Tensor import Tensor
            obj = Tensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def DefaultDataStart(builder): builder.StartObject(2)
def DefaultDataAddNames(builder, names): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(names), 0)
def DefaultDataStartNamesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def DefaultDataAddTensor(builder, tensor): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(tensor), 0)
def DefaultDataEnd(builder): return builder.EndObject()
