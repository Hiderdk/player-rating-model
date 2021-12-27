from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Tuple, Protocol, Union

from data_structures import RatingEntity, MatchRating, Rating, PerformancePredict, RatingTeam, MatchWithRatings, Match, \
    RatingMetric, RatingUpdate,DIFFERENCE


class StartRatingGenerator:

    def generate_rating(self, region_historical_match_ratings: List[MatchWithRatings],
                        entity_match_ratings: List[RatingEntity], rating_metric: RatingMetric) -> Rating:
        return Rating(value=1000.0, rating_metric=rating_metric)


class PerformancePredictGenerator:

    def calculate_performance(self, rating: Rating, ratings: List[Rating]) -> PerformancePredict:
        if rating.rating_metric.prediction == DIFFERENCE:

    def _calculate_rating_difference_from_opponent_team_average(self, rating: Rating, ratings: List[Rating]) -> float:


class RatingUpdateGenerator:

    def calculate_pre_match_rating(self, metrics: Tuple) -> RatingUpdate:
        return

    def calculate_post_match_rating(self, metrics: Tuple) -> RatingUpdate:
        return


class MatchRatingGenerator(Protocol):

    def generate_match_ratings(self, match: Match, player_ratings: Dict[int, RatingEntity],
                               team_ratings: Dict[int, RatingEntity]) -> List[
        List[MatchRating]
    ]:
        ""


class MatchPlayerRatingGenerator(MatchRatingGenerator):

    def __init__(self,
                 performance_predictor: PerformancePredictGenerator,
                 start_rating_generator: StartRatingGenerator,
                 rating_metrics: List[RatingMetric]
                 ):
        self._rating_metrics: List[RatingMetric] = rating_metrics
        self._start_rating_generator: StartRatingGenerator = start_rating_generator
        self._performance_predictor: PerformancePredictGenerator = performance_predictor

    def generate_match_ratings(self, match: Match, player_ratings: Dict[int, RatingEntity],
                               team_ratings: Dict[int, RatingEntity]) -> List[
        Dict[int, RatingEntity],
        Dict[int, RatingEntity],
        List[MatchRating]
    ]:

        for team_id, player_ids in match.team_to_player_ids.items():
            if len(player_ids) == 0:
                raise ValueError("no players for team")
            for player_id in player_ids:
                if player_id not in player_ratings:
                    ratings: Dict[str, Rating] = {}
                    for metric in self._rating_metrics:
                        rating = self._start_rating_generator.generate_rating([], [], rating_metric=metric)
                        ratings[metric.name] = rating
                    new_player_rating = RatingEntity(id=player_id, ratings=ratings)
                    player_ratings[player_id] = new_player_rating

                rating_player = player_ratings[player_id]

    def _generate_single_team_player_ratings(self) -> List[RatingEntity]:
        player_rating_entities: List[RatingEntity] = []
        return player_rating_entities


class RatingGenerator():

    def __init__(self,
                 match_rating_generator: MatchRatingGenerator,
                 ):
        self._match_rating_generator: MatchRatingGenerator = match_rating_generator

    def generate_ratings(self, matches: List[Match], team_ratings: Dict[int, RatingTeam] = None,
                         player_ratings: Dict[int, RatingEntity] = None):
        for match in matches:
            team_ratings, player_ratings, match_ratings = self._match_rating_generator.generate_ratings(match=match,
                                                                                                        player_ratings=player_ratings,
                                                                                                        team_ratings=team_ratings)
