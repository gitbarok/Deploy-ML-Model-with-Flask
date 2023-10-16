FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["q6_flask_app.py", "./"]

EXPOSE 9696

ENTRYPOINT [ "python" ]

CMD [ "q6_flask_app.py" ]