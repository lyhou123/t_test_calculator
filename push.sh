echo "enter commit message: "
read commit_message
git add .
git commit -m "$commit_message"
git push origin main
echo "Changes pushed to main branch."
echo "Done."