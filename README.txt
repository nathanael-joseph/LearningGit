Using Git from the command line.

--- Adding User Info ---
First, lets add basic user information to Git.
    $ git config --global user.name "Nathanael Joseph"
Check the name has been set
    $ git config --get user.name
Set the user's email address:
    $ git config --global user.email "nathanaeljy@outlook.com"
Check the email has been set correctly:
    $ git config --get user.email

--- Initializing and cloning a repo ---
Create a new project using:
    $ git init "repository_name"
Clone an existing project from github or elswhere using:
    $ git clone repo_URL
// Then be sure to change your working directory to the git directory.


--- Modifying the project ---
Add changes to the snapshot (that will be included in next commit).
    $ git add [file]
Add all changes
    $ git add *
Make a local commit
    $ git commit -m [commit message]
// this will commit all staged changes. 
