export GITHUB_USER=USER
export GITHUB_TOKEN=TOKEN
git add .
git commit -m "Update."
git push https://$GITHUB_USER:$GITHUB_TOKEN@github.com/lucasjsch/limud-resources.git gh-pages
git pull origin gh-pages