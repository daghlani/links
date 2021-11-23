# links
A dynamic page to create a list of links that you want, only with edit your list :)

# Usage
_Normal:_
 - Just clone the repo and add your urls and groups to [config.yml](config/config.yml) file like samples:
   
   ```bash
       $ git clone git@github.com:daghlani/links.git
   ```
   
   ```yaml
    targets:
      - group: 'monitoring'
        color_tag: "#030c50"
        urls:
          - url:
            href: http://example.com
            title:  Example
          - url:
            href: http://example1.com
            title: Example1
        .
        .
        .
   ```
    *As you can see, you could add `color_tag` for every group of yourself to chang them color of columns in page. if 
    you don't set anything for that, default color will be take. (`#111`)*
    
    
 
 - create a virtualenv and install requirements: 
 
    ```shell script
        $ virtualenv -p /usr/bin/python3.8 venv
        $ source venv/bin/activate
        $ cd links
        $ pip install -r requirements.txt
    ```
    
 - Start app:
    
    ```shell script
        $ python app.py
    ```
 
 - Now if you don't change the `LINKS_HOST` and `LINKS_PORT` you can see your links page on http://127.0.0.1:5000/.


# Authentication:
 - There is a simple basic authentication ability that you can active it by set environment variable `LINKS_BASIC_AUTH` to on.
    Also you can set password for `admin` username or use default value (`LinksAdminPass`).
    
    if you wanna create some users, you can use this commands to create/update or delete your usernames:
    
    *create / update:*
    ```shell script
        python3 app.py htpasswd -u <username> <psasword>
   ```
    *delete:*
    ```shell script
        python3 app.py htpasswd -d <username>
   ```

 _Docker:_
    
    coming Soon...
 
