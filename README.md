# Product's Category API

The main objective of this API is categorizing products. It takes the title with the description and giving the product a category using a ANN model. The API is built using Flask framework.

## Running the project

- python 3.10 at minimum is required
- Clone the repository 

> git clone https://github.com/mouadlaayouni-youcan/product-category-api.git

- Install the requirements 

> pip install -r requirements.txt
- execute the project using 

      flask run
    
    or
    
      flask --debug run

on the first execution you will need to wait for the model to get downloaded
 - link ANN model : https://drive.google.com/file/d/1ay7UPkh4I_YjggdrqJtne0QWgk_f_zcv/view?usp=sharing
 - link TF-IDF    : https://store3.gofile.io/download/c9324af4-fb56-4a94-979f-250a8d64371f/TF-IDF.pkl

if the download doesn't work try downloading it manually using :
```
wget https://store3.gofile.io/download/c9324af4-fb56-4a94-979f-250a8d64371f/TF-IDF.pkl
```
```
wget https://store3.gofile.io/download/264d9274-48b1-4a16-8720-fc94f2c3af50/ANN-N.h5
```

### Documentation :

[Link to the documentation](https://nextmediama.atlassian.net/wiki/spaces/YOUC/pages/edit-v2/2577465345)
