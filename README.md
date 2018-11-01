## Rundeck Node-Create Plugin

This is a plugin to be run on an existing instance or localhost Rundeck machine to create nodes in Rundeck to be accessed later.

## Install

You have a choice for which zip file to use, you can use the one I have provided called `node-create-plugin.zip`* or you can make your own version of the zip file by running the command `zip -r node-create-plugin.zip zip -r node-create-plugin.zip node-create-plugin/contents/ node-create-plugin/plugin.yaml` (assuming you have access to zip). The plugin should be put in your Rundeck instance's plugins directory which is by default located at `/var/lib/rundeck/libext/`. If you want an example of the plugin in action go to the bottom of the readme to the Example Job section.

\*I am only not including an md5sum because it changes every time I re-zip the file. Don't trust me, zip your own.

## Requirements

I did all of my testing for this plugin occurred in Rundeck version 3.0.7-20181008 (jalapeño popper deepskyblue flag). I have not tested it with any 2.X versions but may do so after development is complete.

There should not be any other dependencies apart from Rundeck.

It is important to note that this plugin will create, open and edit files. There may be some behaviors that occur from this that are unexpected so it would be best if when a job is called no other jobs are currently running that might use the node being created. That being said, maybe it will all be fine.

## Configuration

There are several required options and some optional options that have built in defaults.

There are a number of attributes that will be used in the creation of the node. It is important that none of these be left blank as this could cause issues with how the node is read.

The attributes include
  * **Node Name:** The name of your node as it appears in Rundeck. If you are making an individual node file then this the file name will be in the format `node_name.yml`.  
  * **Hostname:** The address used by Rundeck to login to this particular node. It can be either an ip address or a hostname.
  * **Login Username:** This shall be the username you intend to use to login to the node with. The format that rundeck will use to access a node is similar to `ssh <username>@<hostname/ip>`. This username should exist on the device, usually set to root or rundeck (if you make a rundeck user on the target node).
  * **File Path\*:** This will be assumed by the plugin as the default location of the node file or directory. You should change this if the default location is incorrect. By default it is `/var/rundeck/projects/<project name>/etc/resources(.xml)`. There will be a little more explanation of this later.
  * **Node Description:** (Optional) This can be whatever you would like but should not be blank. The plugin may add a basic description if none is included.
  * **Tags:** (Optional) This should be a comma separated list containing no spaces in between tags. The plugin may add a basic tag if none is included. Example input: `first,test,rundeck1`
  * **Overwrite:** If an existing node has the same Node Name as you have just entered should the existing node be overwritten with the new information?

\***Note on File Path**: I have encountered two common configurations when it comes to Rundeck Node setups. The most common is to have a single `resources.xml` file containing information on all nodes. The other is to have a folder called resources which contains a series of `<node name>.yml` files. My program checks to see if the File Path is to a file or a directory and acts accordingly. There is a less common configuration where you have both a `resources.xml` file as well as a resources folder. If you are using this just enter either the file or folder and the program will act accordingly. If you choose to name your `resources.xml` file something else that is fine just add its name instead of the default.

## Testing details

As stated previously, all development and testing for this plugin occurred in Rundeck version 3.0.7-20181008 (jalapeño popper deepskyblue flag). The machine used was for testing was the 'centos/7' vagrant box. Initial node.yml files were placed in the directory `/var/rundeck/projects/<project name>/etc/resources/`.

## Example Job

If you would like to see this job in action you are in luck. I have included the a file called hello.xml which is a job that uses this plugin to create a node.
- Move the plugin to the plugins folder (default: `/var/lib/rundeck/libext/`)
- Ensure it is there by going to the plugins list and looking under the Workflow Node Steps tab
- Under a Rundeck project select Upload Definition from Job Actions
- Navigate to and select the hello.xml file and select remove UUID as it will not be important here
- Run the job and fill in the fields as explained in the bullet points
