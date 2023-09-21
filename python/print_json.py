import json

with open('./course-data.js') as f:
    d = json.load(f)
    # print(d.keys())
    print(d['assignments'][28])
    print(d['assignments'][28].keys())
    # print(json.dumps(d, indent=4))
