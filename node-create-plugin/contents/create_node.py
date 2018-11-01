import os
import sys

# error method, same in all files
def exit_with_status(status, message):
    print message
    sys.exit(status)

# creates a <node name>.yml file from the passed in args
def create_node_file_from_args(args):

    # check if our file exists and inform the user if it can't be overwritten
    file_name_to_check = args.path + "/" + args.node_name + ".yml"
    if args.overwrite == "false" and check_if_file_exits(file_name_to_check) == True:
        exit_with_status(3, "File exists and has not been set to be overwritten.")

    # ensure tags have no spaces by replacing them with '_' characters
    args.tags = args.tags.replace(" ", "_")

    # replace the template file elements
    node_text = get_node_template()
    node_text = node_text.replace("@node_name@", args.node_name + ":", 1)
    node_text = node_text.replace("@node_name@", "nodename: \"" + args.node_name + "\"")
    node_text = node_text.replace("@description@", "description: \"" + args.description + "\"")
    node_text = node_text.replace("@hostname@", "hostname: \"" + args.hostname + "\"")
    node_text = node_text.replace("@username@", "username: \"" + args.username + "\"")
    node_text = node_text.replace("@tags@", "tags: \"" + args.tags + "\"")

    # open the node file or create it if it doesn't exist and write the content text to it
    f = open(file_name_to_check, "w+")
    f.write(node_text)
    f.close()
    # ensure the file exists and error out if it was not
    if check_if_file_exits(file_name_to_check):
        return True
    else:
        exit_with_status(4, "File could not be created, change user into rundeck and see if you can make it.")


# checks if a file exists
def check_if_file_exits(path):
    if os.path.isfile(path):
        return True
    else:
        return False

# get the content template that will be changed when creating a node file
def get_node_template():
    node_text = "---\n"
    node_text += "@node_name@\n"
    node_text += "  @description@\n"
    node_text += "  @hostname@\n"
    node_text += "  @node_name@\n"
    node_text += "  @tags@\n"
    node_text += "  @username@\n"
    return node_text
