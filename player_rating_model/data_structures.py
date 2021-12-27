from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Literal

DIFFERENCE = "difference"


@dataclass
class RatingMetric:
    name: str
    against: str = None
    prediction: Literal["difference", "sum"] = "difference"


@dataclass
class Rating:
    entity_id: int
    team_id: int
    rating_metric: RatingMetric
    value: float
    rating_context: Dict[str, float] = None


@dataclass
class RatingEntity:
    id: int
    ratings: Dict[str, Rating] = 0


@dataclass
class RatingTeam:
    id: int
    players: List[RatingEntity] = None


@dataclass
class PerformancePredict:
    pre_match_ratings: Dict[str, Rating]
    pre_match_average_opponent_ratings: Dict[str, Rating]
    predicted_performance: float
    performance: float


@dataclass
class RatingUpdate:
    performance: PerformancePredict


@dataclass
class MatchRating:
    entity_id: int
    opponent_team_id: int

    opponent_player_ids: List[int] = None
    pre_match_team_ratings: List[Dict[str, Rating]] = None
    pre_match_opponent_ratings: List[Dict[str, Rating]] = None
    post_match_ratings: Dict[str, Rating] = None
    series_id: int = None
    game_id: int = None


@dataclass
class MatchEntity:
    entity_id: int
    team_id: int
    start_date_time: datetime
    performances: Dict[str, float]
    series_id: int = None
    game_id: int = None


@dataclass
class Match:
    team_ids: List[int]
    team_to_player_ids: Dict[int, List[int]] = None
    series_id: int = None
    game_id: int = None


@dataclass
class MatchWithRatings:
    match: Match
    entity_match_ratings: Dict[int, MatchRating]
    series_id: int = None
    game_id: int = None


@dataclass
class Tournament:
    name: str
    id: int
    matches_with_ratings: List[MatchWithRatings]
    region: str = None
    country: str = None
    prize_pool: str = None
    location: str = None


@dataclass
class League:
    name: str
    tournaments: List[Tournament]
    match_with_ratings: List[MatchWithRatings]
    region: str = None
    country: str = None
    prize_pool: str = None
    location: str = None


@dataclass
class Region:
    name: str
    leagues: List[League]
    match_with_ratings: List[MatchWithRatings]
