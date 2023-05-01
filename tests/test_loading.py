from langflow import load_flow_from_json
import os

def test_loading():
    for json_file in os.listdir('./examples'):
        if json_file.endswith('.json'):
            flow = load_flow_from_json(f'./examples/{json_file}', build=False)
            assert flow is not None
