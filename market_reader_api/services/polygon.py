from datetime import date
from polygon import RESTClient
from polygon.rest.models import Agg


class Polygon:
    def __init__(self) -> None:
        self.client: RESTClient = RESTClient()

    def fetch_aggregates(
            self,
            ticker: str,
            start: date,
            end: date,
            timespan: str = "day",
            multiplier: int = 1
    ) -> list[Agg]:
        return self.client.get_aggs(
            ticker,
            multiplier,
            timespan,
            start.isoformat(),
            end.isoformat(),
        )
