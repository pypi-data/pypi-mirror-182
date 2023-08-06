import platform

global winvers
global kind
osvers = []
kind = ""

def update_OS(nkind):
    if nkind == "Mac OS":
        nkind = "Darwin"
    global kind
    kind = nkind

def update_OS_versions(vers: str):
    global osvers
    osvers = vers

def os():
    beginning = osvers[0]
    endn = len(osvers) - 1
    end = osvers[endn]
    total = kind + " " + beginning + " - " + end
    return total

def osCheck():
    prob = 0
    if platform.system() == kind:
        prob = 1
        i = 0
        while i < len(osvers):
            if platform.release().startswith(osvers[i]):
                prob = 2
                break
            i += 1
    if prob == 2:
        del prob
        return True
    else:
        del prob
        return False
