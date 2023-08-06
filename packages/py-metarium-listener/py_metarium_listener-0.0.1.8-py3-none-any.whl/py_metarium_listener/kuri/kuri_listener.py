import re

from ..base import BaseListener
from ..utils import (
    QueryParameter,
    KuriObject,
    KuriOperation,
    ExtrinsicCall,
)

METARIUM_EXTRINSIC = "Metarium"
# SRC-related extrinsic calls

FUNCTION_CALL_ADMIN_UPDATE_SCRIBE_STATUS = "force_update_scribe_authority_status"

KURI_OPERATION = KuriOperation()

class KuriListener(BaseListener):

    def __processed_block(self, block):
        processed_block = {
            "block_number": block["header"]["number"],
            "extrinsics": []
        }
        for extrinsic in block["extrinsics"]:
            extrinsic = extrinsic.serialize()
            if extrinsic["call"]["call_module"] == METARIUM_EXTRINSIC:
                call = ExtrinsicCall(
                    call_function=extrinsic["call"]["call_function"],
                    call_index=extrinsic["call"]["call_index"],
                    caller=extrinsic["address"]
                )
                if call.call_function in (
                            KURI_OPERATION.create,
                            KURI_OPERATION.accept,
                            KURI_OPERATION.delete
                        ):
                    processed_block["extrinsics"].append(
                        KuriObject(
                            kuri = extrinsic["call"]["call_args"][0]["value"],
                            call_function=call.call_function,
                            call_index=call.call_index,
                            caller=call.caller
                        )
                    )
                elif call.call_function == KURI_OPERATION.transfer:
                    processed_block["extrinsics"].append(
                        KuriObject(
                            kuri = extrinsic["call"]["call_args"][1]["value"],
                            call_function=call.call_function,
                            call_index=call.call_index,
                            caller=call.caller
                        )
                    )
        return processed_block

    def __listen(self, direction, block_hash, block_count, query):
        assert all(isinstance(parameter, QueryParameter) for parameter in query)
        
        # print(f"\n\nQUERY IS {query}\n\n")
        
        for block, is_metarium in super().listen(direction, block_hash, block_count):
            if not is_metarium:
                continue
            block = self.__processed_block(block)
            if len(query):
                extrinsics = block.pop("extrinsics")
                block["extrinsics"] = []
                for kuri_object in extrinsics:
                    assert isinstance(kuri_object, KuriObject)
                    extrinsic = kuri_object._asdict()
                    query_matches = 0
                    for parameter in query:
                        if (
                                (f"{parameter.field}" in extrinsic) and \
                                (re.search(f"{parameter.value}", f"{extrinsic[parameter.field]}"))
                            ):
                            query_matches += 1
                    if query_matches == len(query):
                        block["extrinsics"].append(extrinsic)
                if not len(block["extrinsics"]):
                    continue

            yield block

    def listen(self, direction, block_hash=None, block_count=None, query=[]):
        query = query or []
        for block in self.__listen(direction, block_hash, block_count, query):
            yield block
