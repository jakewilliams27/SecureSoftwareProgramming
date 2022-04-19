
import requests

from plotly.graph_objs import Bar, Scatter
from plotly import offline

import urllib.parse
import os.path, hashlib

#store the results

import csv

days_in_month = {1 : 31,
                 2 : 28,
                 3: 31,
                 4: 30,
                 5: 31,
                 6: 30,
                 7: 31,
                 8: 31,
                 9: 30,
                 10: 31,
                 11: 30,
                 12: 31}

def getCVEs(year, month):

    #if not os.path.isfile(f"cve-{year}-{month:02d}.csv"):
    #    return True


    last_day = days_in_month[month]
    api_key = "393b820c-a6e4-42c1-a193-84d20e0825dc"
    
    URL = "https://services.nvd.nist.gov/rest/json/cves/1.0/"
    
    params = {
        "pubStartDate": f"{year}-{month:02d}-01T00:00:00:000 UTC-05:00",
        "pubEndDate": f"{year}-{month:02d}-{last_day}T23:59:00:000 UTC-00:00",
        "resultsPerPage": "2000",
        "apiKey": api_key
    }



    req = requests.get(URL, params=params)

    data = req.json()
    #print(data['result'])
    with open(f'cve-{year}-{month:02d}.csv', "w", newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['cveid','month','year','pubdate','moddate','exploitabilityScore','impactScore','vectorString','attackVector','attackComplexity','privilegesRequired','userInteraction','scope','confidentialityImpact','integrityImpact','availabilityImpact','baseScore','baseSeverity','description'])
        
        
        for row in data['result']['CVE_Items']:
            writer.writerow([
                            row['cve']['CVE_data_meta']['ID'], 
                            month, 
                            year, 
                            row['publishedDate'], 
                            row['lastModifiedDate'], 
                            row['impact']['baseMetricV3']['exploitabilityScore'],
                            row['impact']['baseMetricV3']['impactScore'], 
                            row['impact']['baseMetricV3']['cvssV3']['vectorString'], 
                            row['impact']['baseMetricV3']['cvssV3']['attackVector'], 
                            row['impact']['baseMetricV3']['cvssV3']['attackComplexity'], 
                            row['impact']['baseMetricV3']['cvssV3']['privilegesRequired'], 
                            row['impact']['baseMetricV3']['cvssV3']['userInteraction'], 
                            row['impact']['baseMetricV3']['cvssV3']['scope'], 
                            row['impact']['baseMetricV3']['cvssV3']['confidentialityImpact'], 
                            row['impact']['baseMetricV3']['cvssV3']['integrityImpact'], 
                            row['impact']['baseMetricV3']['cvssV3']['availabilityImpact'], 
                            row['impact']['baseMetricV3']['cvssV3']['baseScore'], 
                            row['impact']['baseMetricV3']['cvssV3']['baseSeverity'], 
                            row['cve']['description']['description_data'][0]['value']])
    
    return


def plotCVEs(year,month,topnum=40):

    names = []
    severities = []
    exploitabilities = []
    descriptions = []
    
    with open(f"cve-{year}-{month:02d}.csv", "r", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #csvfile.readline();
        for line in reader:
            names.append(line['cveid'])
            severities.append(float(line['baseScore']))
            exploitabilities.append(float(line['exploitabilityScore']))
            descriptions.append(line['description'])


        severities, names, exploitabilities, descriptions = list(zip(*sorted(zip(severities, names, exploitabilities, descriptions), reverse=True)))

        cropped_severities = severities[:topnum]
        cropped_names = names[:topnum]

        offline.plot({
                'data': [
                    Bar(x=cropped_names, y=cropped_severities, hovertext=descriptions)
                ], 
                'layout': {
                    'xaxis': {
                        'title': 'CVE'
                    }, 
                    'yaxis': {
                        'title': 'Severity Score'
                    }, 
                    'title': f"Highest-severity CVES for {year}-{month}"
                }
            }, 
            filename="bar.html"
        )

        offline.plot({
                'data': [
                    Scatter(x=severities, y=exploitabilities, hovertext=descriptions, mode='markers')
                ], 
                'layout' : {
                    'xaxis': {
                        'title': 'Severity Score'
                    },
                    'yaxis': {
                        'title': 'Exploitability Score'
                    },
                    'title': f"CVE severity vs. exploitability for {year}-{month}"
                }
            }, 
            filename="scatter.html"
        )
        return


    return


if __name__ =="__main__":
    getCVEs(2022,2)
    plotCVEs(2022,2)
    h = hashlib.new('sha1')
    h.update(open("cve-2022-02.csv").read().encode("utf-8"))
    print(h.hexdigest())
