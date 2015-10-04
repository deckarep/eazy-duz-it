import subprocess
from subprocess import Popen, PIPE, STDOUT

def pull_request(title):
	# merge master template with contributing template
	global_template = load_template("GLOBAL.md")
	cont_template = load_template("CONTRIBUTING.md")
	merged_template = title + "\n\n" + global_template + cont_template

	# generate a PR against the merged templates
	p = Popen(["hub", "pull-request", "-F", "-"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
	cmd_stdout = p.communicate(input=merged_template)[0]
	link = cmd_stdout.decode()

	# assign resultant link to clipboard
	setClipboardData(link)
	print "Created PR (added to clipboard) : " + link 

def load_template(name):
	with open(name, 'r') as f:
		lines = f.read()
		return lines

# Helper method for getting the clipboard's data
def getClipboardData():
	p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
	retcode = p.wait()
	data = p.stdout.read()
	return data

# Helper method for setting the clipboard with data
def setClipboardData(data):
	p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
	p.stdin.write(data)
	p.stdin.close()
	retcode = p.wait()

if __name__ == "__main__":
	pull_request("my awesome pr")
