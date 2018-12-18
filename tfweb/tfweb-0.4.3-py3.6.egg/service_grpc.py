# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: service.proto
# plugin: grpclib.plugin.main
import abc

import grpclib.const
import grpclib.client

import tensorflow.core.framework.tensor_pb2
import google.protobuf.wrappers_pb2
import service_pb2


class ModelBase(abc.ABC):
    @abc.abstractmethod
    async def Predict(self, stream):
        pass

    def __mapping__(self):
        return {
                '/Model/Predict':
                grpclib.const.Handler(
                        self.Predict,
                        grpclib.const.Cardinality.UNARY_UNARY,
                        service_pb2.PredictRequest,
                        service_pb2.PredictResponse,
                ),
        }


class ModelStub:
    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Predict = grpclib.client.UnaryUnaryMethod(
                channel,
                '/Model/Predict',
                service_pb2.PredictRequest,
                service_pb2.PredictResponse,
        )
