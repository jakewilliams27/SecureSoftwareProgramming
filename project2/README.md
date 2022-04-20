
# Assignment

The National Vulnerability Database (NVD) is administered by NIST. It reports lots of detailed information on software vulnerabilities, assigning each a unique identifier, while documenting the types of harms possible and which software is affected. You can learn about the program here: https://nvd.nist.gov/.


In this project, you will write a Python program to access the NVD through its API, which is documented here: https://nvd.nist.gov/developers/vulnerabilities.


Please sign up for an API key: https://nvd.nist.gov/developers/request-an-api-key. This ensures you can query the system more frequently (useful while you're debugging).


You have two primary tasks.


## Task 1
**Implement def getCVEs(year, month):**


In this method, you will write an API query that will request all vulnerabilities identified in the specified year and month. The results come back in JSON format, which contains more information than we need. You will need to extract relevant fields and write the results to a CSV file named cve-year-month.csv, where year and month are the arguments supplied to the function. Here are the fields you need to include (use CVSSv3 measures):

* cveid   
* month   
* year   
* publication date   
* modification date
* exploitabilityScore
* impactScore
* vectorString
* attackVector
* attackComplexity
* privilegesRequired
* userInteraction
* scope
* confidentialityImpact
* integrityImpact
* availabilityImpact
* baseScore
* baseSeverity
* description


The file format, including headers and example entries for 10 CVEs, is in the attached cve-2022-02-sample.csv. Please follow that formatting exactly (headers and fields).


## Task 2
**Make plots of the gathered data in the plotCVEs(year,month,topnum=40) method.**


You should make two plots. The first is a bar chart plot of the top 40 CVEs in terms of highest severity rating identified for the month specified in the method. You should use the CSV generated in Task 1 to make the plot. Plot them in descending order by severity, and include a description of the vulnerability in the text that appears when you hover over the bar.


The second is a scatter plot for each CVE identified that month comparing the overall severity score (CVSS v3) to the exploitability score.


Below I've included a screenshot of what both should look like.


Do not modify the code included in the if __name__=="__main__" block.


![](https://github.com/jtw7615/SecureSoftwareProgramming/blob/main/project2/bar.png?raw=true)
![](https://github.com/jtw7615/SecureSoftwareProgramming/blob/main/project2/scatter.png?raw=true)
