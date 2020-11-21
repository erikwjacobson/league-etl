-- Generate verification table
CREATE TABLE verification
(
    verification_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (verification_id),
    match_id varchar(255) NOT NULL,
);

-- Generate primary data warehousing database
CREATE TABLE player (
    player_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (player_id),
    player_name varchar(255) NOT NULL
);

CREATE TABLE league (
    league_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (league_id),
    league_name varchar(255) NOT NULL
);

CREATE TABLE team (
    team_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (team_id),
    league_id int NOT NULL FOREIGN KEY REFERENCES league(league_id), --FK
    team_name varchar(255) NOT NULL,
);

CREATE TABLE roster (
    roster_id int IDENTITY NOT NULL,
    CONSTRAINT PK_roster_roster_id PRIMARY KEY (roster_id),
    team_id int NOT NULL FOREIGN KEY REFERENCES team(team_id), --FK
    top_player_id int NOT NULL FOREIGN KEY REFERENCES player(player_id), --FK
    jg_player_id int NOT NULL FOREIGN KEY REFERENCES player(player_id), --FK
    mid_player_id int NOT NULL FOREIGN KEY REFERENCES player(player_id), --FK
    bot_player_id int NOT NULL FOREIGN KEY REFERENCES player(player_id), --FK
    sup_player_id int NOT NULL FOREIGN KEY REFERENCES player(player_id), --FK
);

CREATE TABLE patch (
    patch_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (patch_id),
    patch_no varchar(255) NOT NULL,
    start_date date,
    end_date date,
);

CREATE TABLE split
(
    split_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (split_id),
    split_name varchar(255),
);

CREATE TABLE game
(
    game_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (game_id),
    blue_roster_id int NOT NULL FOREIGN KEY REFERENCES team(team_id), --FK
    red_roster_id int NOT NULL FOREIGN KEY REFERENCES team(team_id), --FK
    league_id int NOT NULL FOREIGN KEY REFERENCES league(league_id), --FK
    patch_id int NOT NULL FOREIGN KEY REFERENCES patch(patch_id), --FK
    split_id int FOREIGN KEY REFERENCES team(team_id), --FK
    game_date date NOT NULL
);

CREATE TABLE stat_type
(
    stat_type_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (stat_type_id),
    stat_name varchar(255) NOT NULL,
    description text,
);

CREATE TABLE game_player_stat
(
    game_player_stat_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (game_player_stat_id),
    stat_type_id int NOT NULL FOREIGN KEY REFERENCES stat_type(stat_type_id), --FK
    player_id int NOT NULL FOREIGN KEY REFERENCES player(player_id), --FK
    game_id int NOT NULL FOREIGN KEY REFERENCES game(game_id), --FK
    stat_value varchar(255) not null
);

CREATE TABLE game_roster_stat
(
    game_roster_stat_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (game_roster_stat_id),
    stat_type_id int NOT NULL FOREIGN KEY REFERENCES stat_type(stat_type_id), --FK
    roster_id int NOT NULL FOREIGN KEY REFERENCES roster(roster_id), --FK
    game_id int NOT NULL FOREIGN KEY REFERENCES game(game_id), --FK
    stat_value varchar(255) NOT NULL
);

CREATE TABLE champion
(
    champion_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (champion_id),
    champion_name varchar(255) NOT NULL
);

CREATE TABLE game_pick
(
    game_pick_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (game_pick_id),
    champion_id int NOT NULL FOREIGN KEY REFERENCES champion(champion_id), --FK
    stat_type_id int NOT NULL FOREIGN KEY REFERENCES player(player_id), --FK
    pick_position varchar(10) NOT NULL CHECK (pick_position IN('top', 'jungle', 'mid', 'bot', 'support')),
    pick_side varchar(10) NOT NULL CHECK (pick_side IN('blue', 'red'))

);

CREATE TABLE game_ban
(
    game_ban_id int IDENTITY (1,1) NOT NULL,
    PRIMARY KEY (game_ban_id),
    champion_id int NOT NULL FOREIGN KEY REFERENCES champion(champion_id), --FK
    ban_side varchar(10) NOT NULL CHECK (ban_side IN('blue', 'red')),
    ban_order varchar(255) NOT NULL
);