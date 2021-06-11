git config --global user.name "RSFfen"
git config --global user.email "rsf61.fen@gmail.com"
pip freeze > requirements.txt
git init
git status
git add -A
git commit -m "initial commit"

git remote add origin https://github.com/RSFfen/project2.git
git branch -M main
git push -u origin main
heroku login