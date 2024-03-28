from flask import Flask, url_for
from typing import Callable, List


def get_endpoints(curr_endpoint:Callable, app:Flask)->List[Callable]:
    endpoints = []
    for rule in app.url_map.iter_rules():
        print(rule.endpoint)
        if "GET" in rule.methods and not rule.endpoint.startswith('static'):  # Filter GET methods and static files
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            endpoints.append({"url": url, "name": rule.endpoint})
    return endpoints
