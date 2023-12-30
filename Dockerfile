# Use an official Python runtime as a parent image
FROM python:3.9

RUN apt update && \
    apt-get install -y bash-completion \
    sudo tmux r-base r-base-dev xterm nano python3-pip git vim python3-pip --no-install-recommends \
    && rm -rf /var/lib/apt/lists/

ENV USERNAME flask_user
ARG USER_ID=1000
ARG GROUP_ID=15214

RUN groupadd --gid $GROUP_ID $USERNAME && \
        useradd --gid $GROUP_ID -m $USERNAME && \
        echo "$USERNAME:$USERNAME" | chpasswd && \
        usermod --shell /bin/bash $USERNAME && \
        usermod -aG sudo $USERNAME && \
        usermod --uid $USER_ID $USERNAME && \
        echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/$USERNAME && \
        chmod 0440 /etc/sudoers.d/$USERNAME

RUN mkdir -p /home/$USERNAME/flask-app
RUN chown $USERNAME:$USERNAME --recursive /home/$USERNAME/

# Copy requirements.txt to the container
COPY requirements.txt /home/$USERNAME/

# Install Python dependencies
RUN pip install --no-cache-dir -r /home/$USERNAME/requirements.txt

# Set a personal library location for R
ENV R_LIBS_USER /usr/local/lib/R/site-library

# Install R packages
RUN R -e 'install.packages("randomForest", repos="https://cran.rstudio.com/")'

# Expose port 5000 for Flask
EXPOSE 5000

WORKDIR /home/$USERNAME/flask-app

USER $USERNAME
