# Simple Instagram Bot
* Uses Python 3.8  
* Use `pip install -r requirements.txt` to install packages.  

* Fill config.json with desired account username and password.  
* You can change additional files like populate hashtags.txt and comments.txt with required tags and comments.  
* You can also disable/enable some features by commenting on the code.  

* Requires mozilla Firefox installed on your system. Although this code wont run the GUI.  
* if you want GUI, Edit line
> client = InstaPy(username=userfile.read(), password=passfile.read(), headless_browser=True)  
>
to   
> client = InstaPy(username=userfile.read(), password=passfile.read())
>
