import json
def loadConfig(configPath, instName, trigger):
    if trigger == 'null':
        fileName = configPath + 'configuration.json'
    else:
        fileName = configPath + 'configuration_'+trigger+'.json'
    with open(fileName, 'r') as f:
        data = json.load(f)
        for x in range(0, len(data)):
            y = data[x]
            if y.get('name') == instName:
                insName = y.get('name')
                print(insName)
                url = y.get('url')
                print(url)
                user = y.get('username')
                print(user)
                pwd = y.get('password')
                print(pwd)
        return insName, url, user, pwd

import requests
import re
from requests.auth import HTTPBasicAuth
import os

def get_filename_from_cd(cd):
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]



def export_intg(config, SourceInstance, TargetInstance, trigger, intg_id, replace_flag, out_dir, log_enabled):
    logger = OICArtifactslog.get_logger('ExportsrcIntg', log_enabled)
    logger.info('Inside Export Integrations Module...')
    insName, sourceUrl, user, pwd = loadInsConfig.loadConfig(
        config, SourceInstance, trigger)
    sourceUrl = sourceUrl+'/integrations/'+intg_id
    # print(targetUrl)
    logger.info('Source url is: '+sourceUrl)
    logger.info('Exporting integration from Source Instance...')
    credentials = HTTPBasicAuth(user, pwd)
    try:
        res = requests.get(sourceUrl+'/archive',
                           verify=False, auth=credentials)
        filename = get_filename_from_cd(res.headers.get('content-disposition'))
        # print(filename)
        logger.info('Exporting Integration: '+filename)
        filepath = os.path.join(out_dir, filename)
        with open(filepath, 'wb') as export_file:
            export_file.write(res.content)
            #print('Succesfully Exported Integration:'+filename)
            logger.info('Succesfully Exported Integration: '+filename)
        #if export_file is not None:
            #print('Importing the Intgeration....')
            #logger.info(
                'Importing the exported Intgeration to Target Instance...')
            #logger.info('Calling the Import Intgeration Module...')
            #sts, sts_msg = ImporttgtIntg.import_intg(
                #config, replace_flag, TargetInstance, trigger, filepath, log_enabled)
            #logger.info('Import Integration Status: '+str(sts))
            #return filename, sts, sts_msg
