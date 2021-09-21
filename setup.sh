# Setup the virtual environment
#virtualenv -p $(which python3) .venv
#source .venv/bin/activate
#pip install - requirements.txt

# Download the MPEG7 dataset
curl -o MPEG7.zip https://dabi.temple.edu/external/shape/MPEG7/MPEG7dataset.zip
unzip MPEG7.zip && mv original MPEG7 && rm MPEG7.zip

# Create directory for generated images
mkdir Output_Images
