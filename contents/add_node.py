import sys
import xml.etree.ElementTree as ET

# error method, same in all files
def exit_with_status(status, message):
    print message
    sys.exit(status)

# adds an xml node to a resources.yml file
def xml_add(args):
    # replace the template file elements
    node_text = get_xml_template()
    node_text = node_text.replace("@node_name@", args.node_name)
    node_text = node_text.replace("@description@", args.description)
    node_text = node_text.replace("@hostname@", args.hostname)
    node_text = node_text.replace("@username@", args.username)
    node_text = node_text.replace("@tags@", args.tags)

    # get the xml form of all of the existing nodes
    tree = ET.parse(args.path)
    root = tree.getroot()
    # determine if the node exists and if it can be removed
    for child in root.findall("node"):
        if child.get("name") == args.node_name and args.overwrite == "false":
            exit_with_status(6, "The node you are adding already exists and overwrite is set to false.")
        elif child.get("name") == args.node_name and args.overwrite == "true":
            # if we can remove the node do it and write the remaning nodes to our yml file
            root.remove(child)
            tree.write(args.path)
            break
    tree = ''

    # get a string of text to be written to our yml file
    f = open(args.path, "r")
    node_file_text = ""
    for line in f:
        if line != "</project>":
            node_file_text += line
        else:
            # add our node as the last in the file
            node_file_text += node_text
            node_file_text += line
    f.close()
    # write the content to our file 
    f = open(args.path, "w")
    f.write(node_file_text)

# get the content template for an xml file
def get_xml_template():
    node_text = ""
    node_text += "<node name=\"@node_name@\" hostname=\"@hostname@\""
    node_text += " description=\"@description@\""
    node_text += " tags=\"@tags@\" username=\"@username@\"></node>\n"
    return node_text
