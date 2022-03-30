import gitlab
import argparse

# token = input('your token').replace(" ", "")
# if not token:
#     token = "glpat-7zJjQs96eW2Wd5W_pWVA"
# print(token)


parser = argparse.ArgumentParser()
parser.add_argument("-cp", '--project_name', type=str,
                    help="add a new project using -p")
parser.add_argument("-c", '--collaborator', type=str,
                    help="add collaborator")
parser.add_argument("-sg", '--subgroup', type=str, help="create sub group")
parser.add_argument("-t", '--token', type=str, help="create token")


# project_name = input("Enter thr project name").strip()
# groupname = input("give group name where you want to add").strip()

# arr = ['-m', '-t', '-p', '-c']

# x = '-m' in arr
# print(x)
# group_id = int(gl.groups.list(search=groupname)[0].id)


class CreateProject:
    def __init__(self,  project_name, token, collaborator, subgroup):
        self.project_name = project_name
        self.token = token
        gl = gitlab.Gitlab(url='https://gitlab.com',
                           private_token=token)
        gl.auth()
        self.gl = gl
        self.collaborator = collaborator
        self.subgroup = subgroup

    def create_new_project(self):
        p_ar = self.gl.projects.create({"name": self.project_name})
        print("project created in My project")
        user = p_ar.id
        self.user = user

    # def show_data(self):
    #     projects = self.gl.projects.list()
    #     g = self.gl.groups.list()

    # def show_multipledata(self):
    #     id = int(input("Group id to be deleted").replace(" ", ""))
    #     group = self.gl.groups.get(id)
    #     for project in group.projects.list():
    #         print(project)

    # def attribute(self):
    #     id = int(input("project id to be checked").replace(" ", ""))
    #     project = self.gl.projects.get(id)
    #     print(project.attributes)

    # def delte(self):
    #     id = int(input("project id to be deleted").replace(" ", ""))
    #     self.gl.projects.delete(id)

    def add_project(self):
        name = input("name of project").replace(" ", "")
        user = self.gl.projects.create(
            {'name': name, 'namespace_id': self.user})
        self.user = user

    def sub_group(self):
        path_name = input("path")
        group = self.gl.groups.create(
            {'name': self.subgroup, 'path': path_name, 'parent_id': 51386043})
        user = group.id
        self.user = user

    def permission(self):

        project = self.gl.projects.get(self.user)
        # userid = int(
        #     input("Enter id whom you want to give collabration").replace(" ", ""))
        user = self.gl.users.get(self.collaborator).id

        member = project.members.create({'user_id': user,
                                         'access_level':  gitlab.GUEST_ACCESS})
        member.access_level = gitlab.DEVELOPER_ACCESS
        member.save()
        print("all dn")

    # def issuess(self):
    #     id = int(input("project id to be checked").replace(" ", ""))
    #     project = self.gl.projects.get(id)
    #     issues = project.issues.list()
    #     print(issues)


if __name__ == "__main__":
    args = parser.parse_args()
    project_name = args.project_name
    token = args.token
    collaborator = args.collaborator
    subgroup = args.subgroup
    projects = CreateProject(project_name, token, collaborator, subgroup)
    if(subgroup and collaborator):
        projects.sub_group()
        projects.add_project()
        projects.collaborator()
    elif(subgroup):
        projects.sub_group()
        projects.add_project()
    else:

        projects.create_new_project()
        projects.permission()

    # projects.create_new_project(get)

    # gl.groups.create({'name': 'Hello', 'path': 'Hello'})

    # try:
    #     projects.create_newproject()
    # except Exception as e:
    #     raise Exception("Project couldn't be created:" + e)
    # finally:
    #     process.exit(0)

    # add_project_groups.subgroup()
    # add_project_groups.group()

# create a new project
# name=input("enter project name to be enter")

# def create_newproject(name):
#        p_ar = gl.projects.create({'name':name})
#        print(p_ar)
# create_newproject(name)

# to get issues

#  to get Project

# To create a new group

######add group member####


""" not done """
#

# user_data = {'email': 'joshikirti926@gmail.com', 'username': 'joshikirti28', 'name': 'Kirti','password':'Kirti1@'}
# user = gl.users.create(user_data)
# print(user)
# project = gl.projects.get(34889466)
# print(project.attributes)
# urls='https://gitlab.com/projects/new?namespace_id=51325559'
# creates=gl.projects.create(urls)
# print(creates)
# for project in projects:
#     print(project)


# g_ars = group.accessrequests.list()


# Priyanka = gl.users.list(username='salalpriyanka672')[0]

# # user_project = Priyanka.projects.create({'name': 'cool'})
# user_projects = Priyanka.projects.list()
# print(user_projects)


# project.snippets_enabled = 120
# project.save()
# group_create = gl.groups.create({'name': "Hellooo"})

# group = gl.groups.get(51325559)
# print(group)


# to create sub group
# group = gl.groups.create(
#     {'name': 'create343', 'path': 'group/create343'})
