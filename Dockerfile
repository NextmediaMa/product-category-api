FROM XXXXXX #dockerrhub (pythonReq + pipReq)
COPY . /src/
EXPOSE 5000
ENTRYPOINT ['Flask  --debug run']