import os
from typing import List, Optional, Dict, Any
import requests
from dataclasses import dataclass
import json
import dacite
import aiohttp
import asyncio


@dataclass
class WorkflowResponse:
    outputs: Optional[List[str]]
    namedOutputs: Optional[List[Any]]
    executionTrace: Optional[Dict[Any, Any]]

    @classmethod
    def create(cls, response: Dict[Any, Any]):
        result = dacite.from_dict(data_class=cls, data=response)
        try:
            result.namedOutputs = dict(
                *(((k, v) for k, v in x.items()) for x in result.namedOutputs)
            )
        except Exception as e:
            result.namedOutputs = []
        return result

    def __getitem__(self, key):
        return getattr(self, key)

    def generations(self):
        result = []
        for block, block_info in self.executionTrace.items():
            if block_info["node_type"] == "AGIBLOCK":  # lol
                result.append(
                    dict(id=block, inputs=block_info["inputs"], output=block_info["output"])
                )
        return result

    def print_generations(self):
        def _fmt_block(block):
            return json.dumps(block, indent=2)

        for block in self.generations():
            print(_fmt_block(block))


def run_workflow(
    workflow_id: str, api_key: str, args: List[str], kwargs: Dict[str, Any]
) -> WorkflowResponse:
    assert api_key is not None, "api_key not provided"
    headers = {
        "accept": "application/json",
    }
    json_data = {
        "apiKey": api_key,
        "args": args,
        "kwargs": kwargs,
    }
    response = requests.post(
        f"https://prometheus-api.llm.llc/api/workflow/{workflow_id}",
        headers=headers,
        json=json_data,
    )
    decoded_response = response.content.decode("utf-8")
    response_dict = json.loads(decoded_response)
    workflow_response = dacite.from_dict(data_class=WorkflowResponse, data=response_dict)

    return workflow_response

async def run_workflow_async(
        workflow_id: str, api_key: str, args: List[str], session, kwargs: Dict[str, Any]
) -> WorkflowResponse:
    if session is None:
        session = aiohttp.ClientSession()
        
    assert api_key is not None, "api_key not provided"
    headers = {
        "accept": "application/json",
    }
    json_data = {
        "apiKey": api_key,
        "args": args,
        "kwargs": kwargs,
    }
    # response = requests.post(
    #     f"https://prometheus-api.llm.llc/api/workflow/{workflow_id}",
    #     headers=headers,
    #     json=json_data,
    # )
    # decoded_response = response.content.decode("utf-8")
    # response_dict = json.loads(decoded_response)
    # workflow_response = dacite.from_dict(data_class=WorkflowResponse, data=response_dict)

    async with session.post(f"https://prometheus-api.llm.llc/api/workflow/{workflow_id}", headers=headers, json=json_data) as resp:
        response_dict = await resp.json()
        workflow_response = dacite.from_dict(data_class=WorkflowResponse, data=response_dict)
    return workflow_response


def get_type_signature(workflow_id: str, api_key: str):
    url = f"https://prometheus-api.llm.llc/api/workflow/{workflow_id}?apiKey={api_key}"
    headers = {"accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    return json.loads(response.content.decode("utf-8"))


@dataclass
class Workflow:
    id: str
    api_key: Optional[str] = None

    def __post_init__(self):
        self.api_key = os.environ.get("MULTIFLOW_API_KEY", None)

    def run(self, *args, api_key: Optional[str] = None, **kwargs):
        return run_workflow(self.id, api_key or self.api_key, args=args, kwargs=kwargs)

    def type_signature(self, api_key: Optional[str] = None):
        return get_type_signature(self.id, api_key or self.api_key)

    async def run_async(self, *args, api_key: Optional[str] = None, session = None, **kwargs):
        return await run_workflow_async(self.id, api_key or self.api_key, args=args, session = None, kwargs=kwargs)
