# 📑📝 Scanned PDFs checker 📄👨‍💻 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
A minimalistic streamlit based webapp to detect and identify scanned/digitally created PDFs from a large corpus. Want to OCR the scanned docs? Don't worry we have that covered here as well :wink:

### Live Web-App can be found [here.](https://scanned-pdfs-checker.herokuapp.com/)

![demo](https://user-images.githubusercontent.com/29462447/184208229-e1641d8c-0a77-486e-9c5e-b42784b033e1.gif)


## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the necessary dependencies.

## Usage:
1. Simply run the command: 
```
streamlit run app.py
```
2. Navigate to http://localhost:8501 in your web-browser.
3. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading images, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```

------------
## Results 
------------

![1](https://user-images.githubusercontent.com/29462447/184023135-b8c5d056-b670-4c1b-9279-e5c685e5d197.png)
![2](https://user-images.githubusercontent.com/29462447/184023129-7a6c04a4-ebc4-490a-9bf7-2f8c084713d1.png)
![3](https://user-images.githubusercontent.com/29462447/184023132-9cc02e96-ed4c-4ec4-b6b4-96a410b66fd8.png)
![4](https://user-images.githubusercontent.com/29462447/184023133-ab9a02cc-2aa5-4f3f-90f2-a436f54d90f8.png)
![5](https://user-images.githubusercontent.com/29462447/184023373-b922eea6-e029-409d-b2d7-ac130d2ca385.png)

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
