from flask import Flask
from github import Github
import sys
import base64


app = Flask(__name__)

input = str(sys.argv[1]).rsplit("/")
userName = input[3]
repoName = input[4]

git = Github()

@app.route('/v1/<filename>')
def get_config(filename):
        if ('.yml' in filename or '.json' in filename):
            file_contents = git.get_user(userName).get_repo(repoName).get_file_contents(filename).content
            return base64.b64decode(file_contents)
        else:
            return "No such file found in repository"

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
