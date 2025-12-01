from enum import Enum

import uvicorn
from fastapi import FastAPI, Request
from typing import Optional

from fastapi import Header

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello FastAPI!"}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/hello/{model_name}")
def hello(model_name : ModelName,
          message: str):
    return {"message": f"Hello {model_name} {message}"}




@app.post("/debug")
async def debug_basic_request(request: Request):
    """HTTP 요청 디버깅용 API"""
    headers = dict(request.headers)
    body = await request.body()

    return {
        "method": request.method,
        "url": str(request.url),
        "headers": headers,
        "body": body.decode() if body else None,
        "query_params": dict(request.query_params),
        "path_params": dict(request.path_params),
        "usage_guide": {
            "query_params": "Use like: POST /debug?param1=value1&param2=value2",
            "path_params": "Use like: POST /debug/{item_id}",
            "body": "Send JSON body for testing"
        }
    }


@app.post("/debug/{item_id}")
async def debug_path_request(request: Request, item_id: str, category: Optional[str] = None):
    """HTTP 요청 디버깅용 API"""
    headers = dict(request.headers)
    body = await request.body()

    return {
        "method": request.method,
        "url": {
            "full_url": str(request.url),
            "scheme": request.url.scheme,
            "hostname": request.url.hostname,
            "port": request.url.port,
            "path": request.url.path,
            "query": request.url.query,
            "fragment": request.url.fragment
        },
        "headers": headers,
        "body": {
            "raw": body.decode() if body else None,
            "size": len(body) if body else 0
        },
        "path_params": {
            "item_id": item_id,
            "from_request": dict(request.path_params)
        },
        "query_params": {
            "category": category,
            "all_params": dict(request.query_params)
        },
        "client": {
            "host": request.client.host if request.client else None,
            "port": request.client.port if request.client else None
        },
        "cookies": dict(request.cookies),
        "content_type": request.headers.get("content-type"),
        "user_agent": request.headers.get("user-agent"),
        "auth": request.headers.get("authorization"),
        "usage_examples": {
            "path_param": f"Current item_id: {item_id}",
            "query_param": f"Current category: {category}",
            "example_url": "POST /debug/123?category=test&other=value"
        }
    }
