export interface Boardgame {
    id:           number;
    title:        string;
    category:     string;
    description:  string;
    tags:         string;
    min_players:  number;
    max_players:  number;
    best_players: number;
    min_age:      number;
    avg_time:     number;
    played_count: number;
}
