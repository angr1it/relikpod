# Clone the repository
git clone https://github.com/richardpaulhudson/coreferee

# Change to the repository directory
cd coreferee

# Modify the setup.cfg file
sed -i '39s/spacy>=3.0.0,<3.6.0/spacy>=3.0.0,<3.8.0/' setup.cfg
sed -i 's/to_version:             3.3.0/to_version:             3.8.0/g' coreferee/lang/en/config.cfg

# Verify the change
cat setup.cfg | grep spacy

# Install the package
pip install .

# Install dependencies from requirements.txt
pip install -r ../requirements.txt

python -m spacy download en_core_web_lg
python -m coreferee install en
