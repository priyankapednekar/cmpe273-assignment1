from flask import Flask
import sys
from github import Github
import yaml
import simplejson as json


app = Flask(__name__)

file_path=sys.argv[1]

BASE_URL="https://api.github.com"

@app.route("/v1/<string:file_name>")
def hello(file_name):
	
	user_name=file_path[19:24]
	repo_name=file_path[25:]
	file_type= file_name.split(".")
	
	g=Github(login_or_token="c33593dad5481122105464469ca45ee566bdaa4e",base_url=BASE_URL)
	#g=Github(base_url=BASE_URL)
	git=g.get_user(user_name)
	repo = git.get_repo(repo_name)
	
	
	try:
		if (file_type[1]=='yml'):
			con_yml= repo.get_contents(file_name)
			return con_yml.decoded_content
		
     
		elif (file_type[1]=='json'):
			f=file_type[0]+'.yml'
			con_json= repo.get_contents(f)
			raw= con_json.decoded_content 
			return json.dumps(yaml.load(raw))

	except:
			return "File not found!!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
