import json
import requests
import csv

url = '' # paste shoppee or lazada review(get rating link address). limit to 50 and start offset to zero

data = requests.get(url)
html_text = data.text
json_data = json.loads(html_text)
comments_data = json_data['data']['ratings']

for item in comments_data:
	if len(item['comment']) > 20:
		with open(r'data.csv', 'a', newline='', encoding='utf-8') as csv_file:
			column_names = ['comment', 'rating_star', 'itemid']
			writer = csv.DictWriter(csv_file, fieldnames=column_names)
			writer.writerow({
				'comment': item['comment'],
				'rating_star': item['rating_star'],
				'itemid' : item ['itemid']
			})

print('Appended to CSV')