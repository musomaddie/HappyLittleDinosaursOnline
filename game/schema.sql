DROP TABLE IF EXISTS point_cards;
DROP TABLE IF EXISTS instant_cards;
DROP TABLE IF EXISTS disaster_cards;
DROP TABLE IF EXISTS room_ids;

CREATE TABLE point_cards(
	card_name TEXT PRIMARY KEY,
	quantity INTEGER NOT NULL,
	value INTEGER NOT NULL,
	special_effect BOOLEAN NOT NULL,
	special_effect_description TEXT
);

CREATE TABLE instant_cards(
	card_name TEXT PRIMARY KEY,
	quantity INTEGER NOT NULL,
	description TEXT NOT NULL
);

CREATE TABLE disaster_cards(
	card_name TEXT PRIMARY KEY,
	quantity INTEGER NOT NULL,
	disaster_type TEXT NOT NULL,
	description TEXT NOT NULL
);

CREATE TABLE room_ids(
    room_id TEXT PRIMARY KEY
);
