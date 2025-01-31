VENV_PATH="/Users/abuwork/ml_env"
source "$VENV_PATH/bin/activate"

PROBLEM_LINK="https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/"
AUTHOR="Abubakir Koshek. email: koshek[dot]a[at][phystech default mail]"

python src/scraper.py --link "$PROBLEM_LINK" --author "$AUTHOR"