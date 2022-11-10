# To DO ?

## API 

- [X] Install 
    - [X] Django 
    - [X] restframwork
    - [X] jwt 
    - [X] CORS

- [X] Auth
    - [X] login with username and password 
    - [X] Token refresh
    - [X] Testing 
        - [X] test_get_access_token
        - [X] test_refreash_access_token
        - [X] test_login_with_invalid_payload


- [X] Items 
    - [X] Create model `items` {name, expired_at, image, created_at }
    - [X] Create `model view set` {create, update, delete, read [ pagination ] }
    - [X] filter `items` by { name, expired_at }
    - [X] Testing 
        - [X] test_create_new_items
        - [X] test_get_items
        - [X] test_paginate
        - [X] test_update_item
        - [X] test_delete_item


## Dashboard 

- [ ] Install   
    - [ ] Vue3 use vite 
    - [ ] piniaJS
    - [ ] tailwindcss 
    - [ ] axios.js

- [ ] Login page 
- [ ] Profile {update, read} + logout
- [ ] Items page 
    - [ ] Table view items 
    - [ ] Form 
        - [ ] Create
        - [ ] update  
    - [ ] filter input { name, expired_at }
