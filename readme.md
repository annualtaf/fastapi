to run application in local

python -m venv env
env\Scripts\activate <!-- env is name of the environment -->

pip install -r requirements.txt <!-- next install dependencies -->

<!-- main = filename -->

uvicorn main:app --reload

always lower case your text and validate if there is no case sensitive validation

in python add \ to continue code in next line

for a post or get request if data is coming from the user need to validate it at both ends
