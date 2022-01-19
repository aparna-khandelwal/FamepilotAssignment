#1. Implement a group_by_owners function that:
#-- accepts a dict containing the file owner name for each file name.
#-- Returns a dict containig a list of file names for each owner name, in any order.
#For eg: {
#'Input.txt': 'Randy',
#'Code.py': 'Stan',
#'Output.txt': 'Randy'
#} 
#the group_by_owners function should return {“randy”: [“input.txt”, “output.txt”], “stan”: [“code.py”]}

def group_by_owners(files):
    result = {}
    for file, owner in files.items(): 
        result[owner] = result.get(owner, []) + [file]  
    return result

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(group_by_owners(files))
