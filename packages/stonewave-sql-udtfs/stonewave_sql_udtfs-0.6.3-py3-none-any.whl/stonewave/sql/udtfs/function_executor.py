import sys
import os
import json
from stonewave.sql.udtfs.load_function import load_function_by_name
from stonewave.sql.udtfs.logger import logger
from stonewave.sql.udtfs.constants import USER_DEFINED_TABLE_FUNCTIONS_PATH
from stonewave.sql.udtfs.protocol.fsm.apply_function_fsm import ApplyFunctionFsm
from stonewave.sql.udtfs.protocol.fsm.eval_function_fsm import EvalFunctionFsm
from stonewave.sql.udtfs.protocol.fsm.eval_function_with_table_param_fsm import (
    EvalFunctionWithTableParamFsm,
)
from stonewave.sql.udtfs.protocol.fsm.result_batch_sender import (
    SharedMemoryRecordBatchSender,
)
from pydantic import BaseModel
from typing import Optional
import threading


class ResponseObj(BaseModel):
    pid: Optional[int] = None
    result: Optional[str] = None
    error: Optional[str] = None


def execute_child_worker(func_name, recv_queue, send_queue):
    def respond(result, error=None, state=None):
        res = json.dumps({"result": result, "error": error, "state": state})
        logger.debug("send response", function=func_name, response=res)
        send_queue.put(res)
        send_queue.join()

    try:
        if not USER_DEFINED_TABLE_FUNCTIONS_PATH in sys.path:
            sys.path.append(USER_DEFINED_TABLE_FUNCTIONS_PATH)
        func_sys_path = os.path.join(USER_DEFINED_TABLE_FUNCTIONS_PATH, func_name)
        if not func_sys_path in sys.path:
            sys.path.append(func_sys_path)

        function = load_function_by_name(func_name)
        if function is None:
            command = recv_queue.get()
            recv_queue.task_done()
            respond(
                result="finish",
                error="function not found, name is {}".format(func_name),
                state="finish",
            )
            return

        func = function()
        fsm = None
        batch_sender = SharedMemoryRecordBatchSender()

        while True:
            logger.debug("waiting for request", function=func_name)
            command = recv_queue.get()
            recv_queue.task_done()
            logger.debug("receive request", function=func_name, request=command)
            request = command
            method, params = request.method, request.params

            if fsm is None:
                if method == "apply":
                    fsm = ApplyFunctionFsm(func, batch_sender, respond)
                elif method == "eval":
                    fsm = EvalFunctionFsm(func, batch_sender, respond)
                elif method == "eval_with_table_param":
                    fsm = EvalFunctionWithTableParamFsm(func, batch_sender, respond)
            fsm_trigger = getattr(fsm, method, None)
            if fsm_trigger:
                try:
                    fsm_trigger(params)
                except Exception as e:
                    logger.error("error occurred during function execution", error=str(e))
                    params = None
                    request = None
                    fsm._clean_up()
                    respond(result="finish", error=e.args[0], state="finish")
                    break
                logger.debug("finish executing request", function=func_name, state=fsm.state)
                if fsm.is_end():
                    logger.debug("finish function execution", function=func_name)
                    break
            else:
                respond(result="finish", error="invalid_method=" + method, state="finish")
                break
        if func_sys_path in sys.path:
            sys.path.remove(func_sys_path)
        if USER_DEFINED_TABLE_FUNCTIONS_PATH in sys.path:
            sys.path.remove(USER_DEFINED_TABLE_FUNCTIONS_PATH)
    except Exception as e:
        logger.error("error occured", error=str(e))
        respond("finish", error=str(e), state="finish")
    finally:
        fsm = None
        batch_sender = None
        function = None
        fsm_trigger = None


def execute_worker(func_name, recv_queue, send_queue):
    thread = threading.Thread(target=execute_child_worker, args=(func_name, recv_queue, send_queue))
    thread.start()
    logger.info(
        "start executing function",
        function=func_name,
        thread_id=thread.ident,
        thread_native_id=thread.native_id,
    )
