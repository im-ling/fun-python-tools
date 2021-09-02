import pandas
import json
excel_path = "hphermes_pageId_config.xlsx"
json_path = "hphermes_pageId_config.json"

excel_data_df = pandas.read_excel(excel_path, sheet_name="7.5.26")
json_str = excel_data_df.to_json(orient='records')
data = json.loads(json_str)
for i in range(len(data)):
    pageId = data[i]["pageId"]
    if pageId.startswith("PX"):
        data[i]["pageId"] = pageId.replace("PX","PI")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

