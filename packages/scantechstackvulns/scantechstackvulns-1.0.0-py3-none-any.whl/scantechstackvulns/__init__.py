__version__ = '1.0.0'

import sys
import warnings
import requests
from bs4 import BeautifulSoup
from simplexl import CreateExcel


class TechStack:
    
    def __init__(self, techstack, output_file, proxyname=None, proxyport=None, proxyusername=None, proxypassword=None):
        warnings.filterwarnings('ignore')
        self.techstack = techstack
        self.output_file = output_file
        self.proxyname = proxyname
        self.proxyport = proxyport
        self.proxyusername = proxyusername
        self.proxypassword = proxypassword
        self.noOfIssuesCount = None
        self.countFrom = None
        self.countThrough = None
        self.startIndex = 0
        self.vulnSearchUrl = "https://nvd.nist.gov/vuln/search/results?adv_search=true&isCpeNameSearch=true&query="
        self.cpeSearchUrl = "https://services.nvd.nist.gov/rest/json/cpes/2.0?keywordSearch={}&resultsPerPage=10000"
          

    @property
    def cpeMatchStrings(self):
        with requests.Session() as request:
            request.verify = False
            cpeMatchStrings = {}
            for each in self.techstack:
                response = request.get(url=self.cpeSearchUrl.format(each))
                if response.status_code == 200:
                    result = response.json()
                    for product in result.get("products"):
                        match_string = product.get("cpe", {}).get("cpeName")
                        if all(x in match_string for x in each.split(" ")):
                            cpeMatchStrings[str(each)] = str(match_string)
        return cpeMatchStrings

    
    def getDataFromWeb(self, url):
        try:
            with requests.Session() as request:
                proxies = {
                    'http':"http://"+str(self.proxyname)+":"+str(self.proxyport),
                    'https':"https://"+str(self.proxyname)+":"+str(self.proxyport)
                }
                if self.proxyusername and self.proxypassword:
                    auth = HTTPProxyAuth(self.proxyusername, self.proxypassword)
                    request.proxies = proxies
                    request.auth = auth

                request.verify = False
                data = request.get(url=url)

        except Exception as e:
            data = None
            print("Unable fetch data from nvd database please try after sometime........")
            sys.exit(e)

        return data
    

    def scrapeTechStackData(self, cpe, startIndex=0):
        try:
            vulnSearchUrl = f"{self.vulnSearchUrl}{cpe}&startIndex={startIndex}"
            data = self.getDataFromWeb(url=vulnSearchUrl)
            parsed_data = BeautifulSoup(data.text, 'lxml')
            self.noOfIssuesCount = int(parsed_data.select_one('strong[data-testid=vuln-matching-records-count]').text)
            self.countFrom = int(parsed_data.select_one('strong[data-testid=vuln-displaying-count-from]').text)
            self.countThrough = int(parsed_data.select_one('strong[data-testid=vuln-displaying-count-through]').text)
            TechStackData = parsed_data.select_one('table[data-testid=vuln-results-table]')
        except Exception as e:
            TechStackData = None
            print("Unable fetch data from nvd database please try after sometime........")
            sys.exit(e)
        return TechStackData
    

    def techStackDataToList(self):
        try:
            print()
            print("Analysis Started. It Takes Time to Complete, Please Wait Patiently")
            productname, cve, severity, description, status = [[] for i in range(5)]
            for product, cpe in self.cpeMatchStrings.items():
                print()
                data = self.scrapeTechStackData(cpe=cpe)
                if self.noOfIssuesCount == 0:
                    productname.append(product.strip())
                    cve.append("No vulnerability")
                    severity.append("No vulnerability")
                    description.append("No vulnerability")
                    status.append("Closed")
                    print(productname[-1]+ " : " + cve[-1] + " : " + severity[-1])
                elif self.noOfIssuesCount <= 20:
                    issues_table = self.scrapeTechStackData(cpe=cpe)
                    non_dispute_issues_count=0
                    for i in range(self.noOfIssuesCount):
                        description_data = issues_table.select_one(f'tr[data-testid=vuln-row-{i}] td p[data-testid=vuln-summary-{i}]').text.strip()
                        if "unspecified vulnerability" in description_data.lower() or "disputed" in description_data.lower():
                            continue
                        else:
                            productname.append(product.strip())
                            cve.append(issues_table.select_one(f'tr[data-testid=vuln-row-{i}] th strong a[href]').text.strip())
                            description.append(description_data)
                            cvss3 = issues_table.select_one(f'tr[data-testid=vuln-row-{i}] td[nowrap=nowrap] span[id=cvss3-link]')
                            
                            if cvss3:
                                cvss3_score_severity = cvss3.text.split(":")[-1]
                                cvss3_severity = cvss3_score_severity.split(" ")[-1]
                                severity.append(cvss3_severity.strip())
                            else:
                                cvss2 = issues_table.select_one(f'tr[data-testid=vuln-row-{i}] td[nowrap=nowrap] span[id=cvss2-link{i}]').text
                                cvss2_score_severity = cvss2.split(":")[-1]
                                cvss2_severity = cvss2_score_severity.split(" ")[-1]
                                severity.append(cvss2_severity.strip())
                            status.append("Open")
                            non_dispute_issues_count+=1
                        print(productname[-1]+ " : " + cve[-1] + " : " + severity[-1])
                    else:
                        if non_dispute_issues_count == 0:
                            productname.append(product)
                            cve.append("No vulnerability")
                            severity.append("No vulnerability")
                            description.append("No vulnerability")
                            status.append("Closed")
                            print(productname[-1]+ " : " + cve[-1] + " : " + severity[-1])
                elif self.noOfIssuesCount > 20:
                    count_while = 0
                    while self.noOfIssuesCount - self.startIndex >= 0 :
                        issues_table = self.scrapeTechStackData(cpe=cpe, startIndex=self.startIndex)
                        for i in range(self.countThrough+1 - self.countFrom):
                            description_data = issues_table.select_one(f'tr[data-testid=vuln-row-{i}] td p[data-testid=vuln-summary-{i}]').text.strip()
                            if "unspecified vulnerability" in description_data.lower() or "disputed" in description_data.lower():
                                continue
                            else:
                                productname.append(product.strip())
                                cve.append(issues_table.select_one(f'tr[data-testid=vuln-row-{i}] th strong a[href]').text.strip())
                                description.append(description_data)
                                cvss3 = issues_table.select_one(f'tr[data-testid=vuln-row-{i}] td[nowrap=nowrap] span[id=cvss3-link]')
                                if cvss3:
                                    cvss3_score_severity = cvss3.text.split(":")[-1]
                                    cvss3_severity = cvss3_score_severity.split(" ")[-1]
                                    severity.append(cvss3_severity.strip())
                                else:
                                    cvss2 = issues_table.select_one(f'tr[data-testid=vuln-row-{i}] td[nowrap=nowrap] span[id=cvss2-link{i}]').text
                                    cvss2_score_severity = cvss2.split(":")[-1]
                                    cvss2_severity = cvss2_score_severity.split(" ")[-1]
                                    severity.append(cvss2_severity.strip())
                                status.append("Open")
                                count_while+=1
                            print(productname[-1]+ " : " + cve[-1] + " : " + severity[-1])
                        self.startIndex+=20
                    else:
                        if count_while == 0:
                            productname.append(product)
                            cve.append("No vulnerability")
                            severity.append("No vulnerability")
                            description.append("No vulnerability")
                            status.append("Closed")
                            print(productname[-1]+ " : " + cve[-1] + " : " + severity[-1])
                else:
                    sys.exit("some thing went wrong pls re run the script")
            tech_stack_data = zip(productname, description, cve, severity, status)

        except Exception as e:
            df_tech_stack = None
            print("Unable fetch data from nvd database please try after sometime........")
            sys.exit(e)

        return tech_stack_data
    

    def makeXL(self):
        try:
            tech_stack_data = self.techStackDataToList()
            
            tech_stack_sheet_columns = [
                "DependencyName",
                "Description",
                "CVE",
                "Severity",
                "Status"
            ]

            xl = CreateExcel()
            xl.create_sheet(
                col_data=tech_stack_sheet_columns,
                row_data=list(tech_stack_data)
            )
            xl.save(self.output_file)   
            print()
            print('execl created successfully....')
            print()
            return
        except Exception as e:
            print("Unable to create xls....")
            sys.exit(e)
    

    @classmethod
    def scan(cls, techstack, output_file, proxyname=None, proxyport=None, proxyusername=None, proxypassword=None):
        obj = cls(techstack, output_file, proxyname=None, proxyport=None, proxyusername=None, proxypassword=None)
        return obj.makeXL()

