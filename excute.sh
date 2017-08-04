
#score_api website
for loop in 0 1 2 3
do
    nohup python manage.py runserver 0.0.0.0:800$loop >/dev/null 2>&1 &
    sleep 0.1s
done