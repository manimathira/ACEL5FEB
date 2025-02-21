from cvprac import cvp_client
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = "192.168.0.5"
cvp2 = ""
cvp3= ""
cvp_user= "arista"
cvp_pw = "aristar872"
client = cvp_client.CvpClient()
client.connect([cvp1],cvp_user,cvp_pw)
tasks=client.api.get_tasks_by_status('Pending')
for task in tasks:
    taskid = task['workOrderId']
    hostname= task['workOrderDetails']['netElementHostName']
    print (f"executing tasks on {hostname}")
    client.api.execute_task(taskid)






