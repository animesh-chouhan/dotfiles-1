
import argparse
import sys

import i3

workspaces = i3.get_workspaces()[:-1]
workspaces.append(workspaces[0])
print(workspaces)
for i in range(len(workspaces)):
    if workspaces[i]["focused"] == True:
        i3.workspace(workspaces[i+1]["name"])
        sys.exit()

# i3.workspace(workspaces[1]["name"])
