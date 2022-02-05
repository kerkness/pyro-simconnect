##
## This script parses flightsimulator.com docs and gets simvars
## and saves them to a json file.
##
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

req = Request("https://docs.flightsimulator.com/html/Programming_Tools/SimVars/Simulation_Variables.htm")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

variables = []
match = "Variables.htm#"
for link in links:
    if match in link:
        hashpos = link.find("#")
        slashpos = link.rfind("/")
        variable = link[hashpos+1:]
        category = link[slashpos+1:hashpos-4]
        details = { 'category': category, 'variable': variable }
        
        variables.append(details)

# print(variables)
json_object = json.dumps(variables, indent = 4)
print(json_object)

with open('variables.json', 'w') as simvar_file:
    simvar_file.write(json_object)
