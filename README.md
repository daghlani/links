# links
A dynamic page to create a list of links that you want, only with edit your list :)

# Usage
### _Normal:_
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
    As you can see, you could add `color_tag` for every group of yourself to chang them color of columns in page. if 
    you don't set anything for that, default color will be take. (`#111`).
    
    also to change text color of any group of links, you could set the `text_color` variable as a color that you want. if 
    you don't set anything for that, default color will be take. (`#22f5ff`).
    
    
 
 - create a virtualenv and install requirements: 
 
    ```console
        $ virtualenv -p /usr/bin/python3.8 venv
        $ source venv/bin/activate
        $ cd links
        $ pip install -r requirements.txt
    ```
    
 - Start app:
    
    ```console
        $ python app.py
    ```
 
 - Now if you don't change the `LINKS_HOST` and `LINKS_PORT` you can see your links page on http://127.0.0.1:5000/.


### _Docker:_
 
 - in order to use docker version, just you need pull this docker image and run it like this:
    ```console
        $ docker run -p 80:80 --name LINKS daghlani/links:latest
    ```
 - also you can use this docker-compose sample:
 
     ```yaml
        version: '3.4'
        services:
          LINKS:
            container_name: ${LINKS_CON_NAME:-LINKS}
            image: links:${LINKS_V:-latest}
            ports:
              - "8040:80"
            #volumes:
            #  - $PWD/config:/app/config
            restart: unless-stopped
    ```
     before it, you must create a `config` directory and put `config.yml` in it. you can see this [config.yml](config/config.yml) sample and then:
     
     create a `.env` file like this:
    ```shell script
        LINKS_CON_NAME=LINKS
        LINKS_V=0.2
    ```
    
 - and run it:
     ```console
        $ docker-compose up -d
     ```
       

# Authentication:
 - There is a simple basic authentication ability that you can active it by set environment variable `LINKS_BASIC_AUTH` to on.
    Also you can set password for `admin` username or use default value (`LinksAdminPass`).
    
    if you wanna create some users, you can use this commands to create/update or delete your usernames:
    
    *create / update:*
   ```console
        $ python3 app.py htpasswd -u <username> <psasword>
   ```
    *delete:*
   ```console
        $ python3 app.py htpasswd -d <username>
   ```
