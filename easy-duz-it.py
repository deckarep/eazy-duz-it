import subprocess
from subprocess import Popen, PIPE, STDOUT
import argparse
import os.path
import json

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
	cont_json = load_json("easy-duz-it.json")
	# generate exclusive repo contents
	tier = "- [ ] %s - Merge Checklist:\n" % cont_json["name"]
	# including checklist specific to this repo
	checklist = "\n".join(["\t- [ ] " + c for c in cont_json["contributing"]])
	merged_template = title + "\n\n" + global_template + tier + checklist

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

def load_json(name):
	d = load_template(name)
	j = byteify(json.loads(d))
	return j

# Keeps json in simple ascii format
def byteify(input):
	if isinstance(input, dict):
		return {byteify(key):byteify(value) for key,value in input.iteritems()}
	elif isinstance(input, list):
		return [byteify(element) for element in input]
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	else:
		return input

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
	#print args.title
	#print args.pr

	# Generate pr
	if args.pr:
		if not args.title:
			print "You need a title."
		pull_request(args.title)





