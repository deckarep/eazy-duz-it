import subprocess
from subprocess import Popen, PIPE, STDOUT
import argparse
import os.path

# TODO:
# * parse version from repo, perhaps by specifiying a file and line and regex of where to get the version
# * increment version automatically (optional)
# * provide json config in repo where all the details live
# * include the chef-data staging/production keys that should get updated
# * provide command: --pull-request (currently in progress)
# * provide command: --release (not started, but cuts a release)
# * provide command: --rollback (reverses process for speedy rollback)
# * provide command: --staging (automatically prompts to create a release if one doesn't exist)
# * provide command: --prod (fails if a staging was not yet updated and pre-release doesn't exist)
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
	if os.path.isfile(name):
		with open(name, 'r') as f:
			lines = f.read()
			return lines
	return ""

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
	parser = argparse.ArgumentParser(prog="eazy-duz-it")

	parser.add_argument("-pr", "--pull-request", dest="pr", help="generates a pull-request", action="store_true")
	parser.add_argument("-t", "--title", dest="title", help="title for your pull-request")

	# Parse that shit.
	args = parser.parse_args()
	print args.title
	print args.pr

	# Generate pr
	if args.pr:
		if not args.title:
			print "You need a title."
		pull_request(args.title)





