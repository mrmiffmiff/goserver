FROM debian:stable-slim
COPY main.py main.py
COPY books/ books/
RUN <<EOF
apt update
apt install -y python3 python3-pip
EOF
CMD ["python3", "main.py"]
