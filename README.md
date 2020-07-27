# nessusXml2Elastic

Script to convert XML to JSON &amp; Logstash Conf File to parse JSON file for Elasticstack also with Elastictemplate.

How to Use:

1. Export the report as XML file from Nessus VA.
2. Run the xml2json.py script and Enter the Input/Output JSON File Name.
3. Now import the JSON file in to your logstash. nessus_json_parser.conf

**Note: Use the nessus_vul_elastic_template.json (if you want to build the below graphs/views)

![](https://github.com/TejaRamachandran/nessusXml2Elastic/blob/master/_others/Nessus_View_1.gif)
![](https://github.com/TejaRamachandran/nessusXml2Elastic/blob/master/_others/graph.gif)

thanks [@savitha](https://github.com/CGSavitha) for contribution
