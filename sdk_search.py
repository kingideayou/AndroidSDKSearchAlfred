# encoding: utf-8
 # -*- coding: utf-8 -*-

import sys
import argparse
import json
from pprint import pprint
from workflow import Workflow, ICON_WEB, web

ICON_ANDROID = 'icon.png'

def main(wf):
        
    refDatas = json.load(open('androidRefData.json'))
    xmlDatas = json.load(open('androidXmlData.json'))

    # Loop through the returned posts and add an item for each to
    # the list of results for Alfred
    
    for xmlData in xmlDatas:
        index = xmlData['label'].lower().find(wf.args[0].lower())
        if index >= 0:
            wf.add_item(title=xmlData['label'],
                     valid=True,
                     arg=xmlData['link'],
                     subtitle=xmlData['link'],
                     icon=ICON_ANDROID)
                     
    for refData in refDatas:
        index = refData['label'].lower().find(wf.args[0].lower())
        if index >= 0:
            wf.add_item(title=refData['label'],
                     valid=True,
                     arg=refData['link'],
                     subtitle=refData['link'],
                     icon=ICON_ANDROID)
                     
    

    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
   wf = Workflow()
   sys.exit(wf.run(main))
