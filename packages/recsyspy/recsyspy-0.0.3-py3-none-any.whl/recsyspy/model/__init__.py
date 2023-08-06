#### CONTENT ####
class BasicItemModel:
    id: int


#### EVIDENCE ####
class BasicEventModel:
    id: int  #
    user_id: str
    item_id: str
    type: int
    ts: object


class BasicSessionModel:
    id: int


#### REQUEST ####
class BasicRecommendationModel:
    """Provide information to get recommendations."""

    item_seed_id: int  # Optional
    item_seed_ids: list[int]  # Optional
    type: int
    user_uid: int  # Optional
    recommendations: list[BasicItemModel]


#### USER ####
class BasicUserModel:
    uid: int
    ids: list[str]
