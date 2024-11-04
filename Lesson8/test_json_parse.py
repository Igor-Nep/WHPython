import json
company_json = """
    {
    "id": 111,
    "isActive": true,
    "createDateTime": "2022-12-23T14:43:26.7132",
    "lastChangedDateTime": "2022-12-23T14:43:26.7132",
    "name": "Барбершоп 'ЦирюльникЪ'",
    "description": "Крутые стрижки для крутых шишек" 
    }
"""

def test_parse_json():
    company = json.loads(company_json)
    assert company["id"] == 111

def test_parse_array():
    company_list = json.loads(company_json)
    assert company_list["name"] == "Барбершоп 'ЦирюльникЪ'"