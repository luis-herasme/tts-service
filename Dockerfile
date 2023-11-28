FROM python:3.11

# Upgrade pip
RUN pip install --upgrade pip

# Install linux dependencies
RUN apt update
RUN apt install -y libgl1-mesa-glx

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Setup the working directory
WORKDIR /app

# Copy over the files needed for your application (adjust as needed)
COPY . .

EXPOSE 3001

ENV PORT 3001

# set hostname to localhost
ENV HOSTNAME "0.0.0.0"

# Run the flask server
CMD ["waitress-serve", "--host", "0.0.0.0", "--p", "3001", "--call", "app:create_app"]
