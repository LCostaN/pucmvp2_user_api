FROM python:3.9

ENV SECRET=PUCMVP22023
ENV SECRET2=$2y$16$vLR5d3IlBF/hNbXBHA4zQ.jgEaNVOfFtrUkiGNgbQjEgZPRck5jKG

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]