DROP TABLE IF EXISTS tweets
DROP TABLE IF EXISTS top_coins

CREATE TABLE tweets (
	tweet_id, 
	user_name, 
	text, 
	created_at, 
	url
);

CREATE TABLE top_coins(
	date_time,
	ranking, 
	name, 
	price, 
	day_change
);
