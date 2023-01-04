class Player:
    def __init__(self, _player_num: int):
        self.player_num: int = _player_num
        self.roll_num: int = 0
        # Dictionary containing pairs of combo name and if the combo has already been used
        self.combo_dict: dict[str, bool] = {}
        self.has_yahtzee: bool = False
        self.has_bonus: bool = False
        self.can_click = True
        self.upper_points: int = 0
        self.lower_points: int = 0
        self.total_points: int = 0
        self.points_items_list: list[PointsItem] = []

    def clear_point_items(self):
        for x in range(len(self.points_items_list)):
            if self.points_items_list[x].status == "potential":
                self.points_items_list[x].change_status("hidden")


# This is the dumbest fix I have ever done
from PointsItem import PointsItem