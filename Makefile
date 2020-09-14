clean:
	rm -rf db.sqlite3
	rm -rf account/migrations
	rm -rf auth_token/migrations
	rm -rf data_source/migrations
	rm -rf converge/migrations
	rm -rf message/migrations
	rm -rf project/migrations
	rm -rf event/migrations
	rm -rf silence/migrations

make:
	python manage.py makemigrations account auth_token data_source converge project silence event
