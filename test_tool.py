import json
from base64_inspector import transform
def test_transform():
    value='aGk='
    if True: result=transform(value)
    else: result=transform(json.loads(value))
    assert 'hi' in json.dumps(result,ensure_ascii=False)
