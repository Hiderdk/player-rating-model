from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Tuple

from models import RatingEntity, MatchRating, Rating, Performance, RatingTeam, MatchWithRatings, Match


class StartRatingGenerator:

    def generate_rating(self, region_historical_match_ratings: List[MatchWithRatings],
                        entity_match_ratings: List[RatingEntity], metric_name: str) -> Rating:
        return Rating(value=1000.0, metric_name=metric_name)


class PerformancePredictor:

    def calculate_performance(self, rating_teams: List[RatingTeam], metric: str) -> Dict[int, Performance]:
        return


class MatchRatingGenerator:

    def calculate_pre_match_rating(self, metrics: Tuple) -> MatchRating:
        return

    def calculate_post_match_rating(self, metrics: Tuple) -> MatchRating:
        return


class RatingGenerator():

    def __init__(self, start_rating_generator: StartRatingGenerator, performance_predictor: PerformancePredictor,
                 match_rating_generator: MatchRatingGenerator,
                 rating_metrics: Tuple[str, str] = (("kpr", "dpr"), ("dpr", "kpr"))
                 ):
        self._rating_metrics: Tuple[str, str] = rating_metrics
        self._start_rating_generator: StartRatingGenerator = start_rating_generator
        self._performance_predictor: PerformancePredictor = performance_predictor
        self._match_rating_generator: MatchRatingGenerator = match_rating_generator

    def generate_ratings(self, matches: List[Match], team_ratings: Dict[int, RatingTeam] = None,
                         player_ratings: Dict[int, RatingEntity] = None):
        for match in matches:
            for team_id, player_ids in match.team_to_player_ids.items():
                if len(player_ids) == 0:
                    raise ValueError("no players for team")

                for player_id in player_ids:
                    if player_id not in player_ratings:
                        ratings: Dict[str, Rating] = {}
                        for metric in self._rating_metrics:
                            rating = self._start_rating_generator.generate_rating([], [], metric_name=metric)
                            ratings[metric] = rating
                        new_player_rating = RatingEntity(id=player_id, ratings=ratings)
                        player_ratings[player_id] = new_player_rating

                    rating_player = player_ratings[player_id]

    def _generate_single_team_player_ratings(self) -> List[RatingEntity]:
        player_rating_entities: List[RatingEntity] = []
        return player_rating_entities
