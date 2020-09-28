# Automate-Github-with-python
An Automatic GitHub Project Initializer.

Every time creating a new project takes the following steps:
1. Login to GitHub
2. Create a New Repository
3. Name the Repository
4. Write the Description
5. Check the radio button for initilizing the README.md
6. copying the link of the newly created repository
7. opening the terminal and using git clone "repository-link"
8. creating a new file to write the code in
9. opening the file in the editor, in this applications case visual studio code.

The application will do all the steps according to user input:
1. In Create_Creds.py the user will input initial infor about username, password and path to the projects folder where the new repository should be cloned.
2. This information will be written to a creds.py file which will be used in accessing the GitHub account.
3. The Accessing_GitHub.py will ask the user for the name, description and the name of the file to be created after cloning the repository before the user can click on Initialize repository which will make the repository with name and description as provided.