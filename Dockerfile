FROM python:3.11-alpine
LABEL authors="taljo"
COPY Hezi_Exe.py /code/
ENV HASH_FOLDER=/data
RUN mkdir -p /data
ENTRYPOINT ["python", "/code/Hezi_Exe.py"]