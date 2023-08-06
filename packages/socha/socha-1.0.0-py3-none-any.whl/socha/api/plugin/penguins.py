"""
This is the plugin for this year's game `Penguins`.
"""
import logging
import math
from typing import List, Union, Optional
from warnings import warn

_hexagonTemplate = [
    "  _______  \xA0",
    " /       \\ \xA0",
    "/XXXXXXXXX\\\xA0",
    "\\YYYYYYYYY/\xA0",
    " \\_______/ \xA0"
]

_emptyHexagonPlaceholder = "\xA0\xA0\xA0\xA0\xA0\xA0"


class Vector:
    """
    Represents a vector in the hexagonal grid. It can calculate various vector operations.
    """

    def __init__(self, d_x: int = 0, d_y: int = 0):
        """
        Constructor for the Vector class.

        :param d_x: The x-coordinate of the vector.
        :param d_y: The y-coordinate of the vector.
        """
        self.d_x = d_x
        self.d_y = d_y

    def magnitude(self) -> float:
        """
        Calculates the length of the vector.

        :return: The length of the vector.
        """
        return (self.d_x ** 2 + self.d_y ** 2) ** 0.5

    def dot_product(self, other: 'Vector'):
        """
        Calculates the dot product of two vectors.

        :param other: The other vector to calculate the dot product with.
        :return: The dot product of the two vectors.
        """
        return self.d_x * other.d_x + self.d_y * other.d_y

    def cross_product(self, other: 'Vector'):
        """
        Calculates the cross product of two vectors.

        :param other: The other vector to calculate the cross product with.
        :return: The cross product of the two vectors.
        """
        return self.d_x * other.d_y - self.d_y * other.d_x

    def scalar_product(self, scalar: int):
        """
        Extends the vector by a scalar.

        :param scalar: The scalar to extend the vector by.
        :return: The extended vector.
        """
        return Vector(self.d_x * scalar, self.d_y * scalar)

    def addition(self, other: 'Vector'):
        """
        Adds two vectors.

        :param other: The other vector to add.
        :return: The sum of the two vectors as a new vector object.
        """
        return Vector(self.d_x + other.d_x, self.d_y + other.d_y)

    def subtraction(self, other: 'Vector'):
        """
        Subtracts two vectors.

        :param other: The other vector to subtract.
        :return: The difference of the two vectors as a new vector object.
        """
        return Vector(self.d_x - other.d_x, self.d_y - other.d_y)

    def get_arc_tangent(self) -> float:
        """
        Calculates the arc tangent of the vector.

        :return: A radiant in float.
        """
        return math.degrees(math.atan2(self.d_y, self.d_x))

    def are_identically(self, other: 'Vector'):
        """
        Compares two vectors.

        :param other: The other vector to compare to.
        :return: True if the vectors are equal, false otherwise.
        """
        return self.d_x == other.d_x and self.d_y == other.d_y

    def are_equal(self, other: 'Vector'):
        """
        Checks if two vectors have the same magnitude and direction.

        :param other: The other vector to compare to.
        :return: True if the vectors are equal, false otherwise.
        """
        return self.magnitude() == other.magnitude() and self.get_arc_tangent() == other.get_arc_tangent()

    @property
    def directions(self) -> List['Vector']:
        """
        Gets the six neighbors of the vector.

        :return: A list of the six neighbors of the vector.
        """
        return [
            Vector(1, -1),  # UP RIGHT
            Vector(-2, 0),  # LEFT
            Vector(1, 1),  # DOWN RIGHT
            Vector(-1, 1),  # DOWN LEFT
            Vector(2, 0),  # Right
            Vector(-1, -1)  # UP LEFT
        ]

    def is_one_hex_move(self):
        """
        Checks if the vector points to a hexagonal field that is a direct neighbor.

        :return: True if the vector is a one hex move, false otherwise.
        """
        return abs(self.d_x) == abs(self.d_y) or (self.d_x % 2 == 0 and self.d_y == 0)

    def __str__(self) -> str:
        """
        Returns the string representation of the vector.

        :return: The string representation of the vector.
        """
        return f"Vector({self.d_x}, {self.d_x})"


class CartesianCoordinate:
    """
    Represents a coordinate in a normal cartesian coordinate system, that has been taught in school.
    This class is used to translate and represent a hexagonal coordinate in a cartesian and with that a 2D-Array.
    """

    def __init__(self, x: int, y: int):
        """
        Constructor for the CartesianCoordinate class.

        :param x: The x-coordinate on a cartesian coordinate system.
        :param y: The y-coordinate on a cartesian coordinate system.
        """
        self.x = x
        self.y = y

    def to_vector(self):
        """
        Converts the cartesian coordinate to a vector.
        """
        return Vector(d_x=self.x, d_y=self.y)

    def add_vector(self, vector: Vector) -> 'CartesianCoordinate':
        """
        Adds a vector to the cartesian coordinate.

        :param vector: The vector to add.
        :return: The new cartesian coordinate.
        """
        vector: Vector = self.to_vector().addition(vector)
        return CartesianCoordinate(x=vector.d_x, y=vector.d_y)

    def subtract_vector(self, vector: Vector) -> 'CartesianCoordinate':
        """
        Subtracts a vector from the cartesian coordinate.

        :param vector: The vector to subtract.
        :return: The new cartesian coordinate.
        """
        vector: Vector = self.to_vector().subtraction(vector)
        return CartesianCoordinate(x=vector.d_x, y=vector.d_y)

    def distance(self, other: 'CartesianCoordinate') -> float:
        """
        Calculates the distance between two cartesian coordinates.

        :param other: The other cartesian coordinate to calculate the distance to.
        :return: The distance between the two cartesian coordinates.
        """
        return self.to_vector().subtraction(other.to_vector()).magnitude()

    def to_hex(self) -> 'HexCoordinate':
        """
        Converts the cartesian coordinate to a hex coordinate.

        :return: The hex coordinate.
        """
        return HexCoordinate(x=self.x * 2 + (1 if self.y % 2 == 1 else 0), y=self.y)

    def to_index(self) -> Optional[int]:
        """
        Converts the cartesian coordinate to an index.

        :return: The index or None if the coordinate is not valid.
        """
        if 0 <= self.x <= 7 and 0 <= self.y <= 7:
            return self.y * 8 + self.x
        return None

    @staticmethod
    def from_index(index: int) -> Optional['CartesianCoordinate']:
        """
        Converts an index to a cartesian coordinate.

        :param index: The index to convert.
        :return: The cartesian coordinate.
        """
        if 0 <= index <= 63:
            return CartesianCoordinate(x=index % 8, y=int(index / 8))
        raise IndexError("Index out of range.")

    def __repr__(self) -> str:
        return f"CartesianCoordinate({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, CartesianCoordinate) and self.x == other.x and self.y == other.y


class HexCoordinate:
    """
    Represents a coordinate in a hexagonal coordinate system, that differs from the normal cartesian one.
    This class is used to represent the hexagonal game board.
    """

    def __init__(self, x: int, y: int):
        """
        Constructor for the HexCoordinate class.

        :param x: The x-coordinate on a hexagonal coordinate system.
        :param y: The y-coordinate on a hexagonal coordinate system.
        """
        self.x = x
        self.y = y

    def to_cartesian(self) -> CartesianCoordinate:
        """
        Converts the hex coordinate to a cartesian coordinate.

        :return: The cartesian coordinate.
        """
        return CartesianCoordinate(x=math.floor((self.x / 2 - (1 if self.y % 2 == 1 else 0)) + 0.5), y=self.y)

    def to_vector(self) -> Vector:
        """
        Converts the hex coordinate to a vector.

        :return: The vector.
        """
        return Vector(d_x=self.x, d_y=self.y)

    def add_vector(self, vector: Vector) -> 'HexCoordinate':
        """
        Adds a vector to the hex coordinate.

        :param vector: The vector to add.
        :return: The new hex coordinate.
        """
        vector: Vector = self.to_vector().addition(vector)
        return HexCoordinate(x=vector.d_x, y=vector.d_y)

    def subtract_vector(self, vector: Vector) -> 'HexCoordinate':
        """
        Subtracts a vector from the hex coordinate.

        :param vector: The vector to subtract.
        :return: The new hex coordinate.
        """
        vector: Vector = self.to_vector().subtraction(vector)
        return HexCoordinate(x=vector.d_x, y=vector.d_y)

    def get_neighbors(self) -> List['HexCoordinate']:
        """
        Returns a list of all neighbors of the hex coordinate.

        :return: The list of neighbors.
        """
        return [self.add_vector(vector) for vector in self.to_vector().directions]

    def distance(self, other: 'HexCoordinate') -> float:
        """
        Calculates the distance between two hex coordinates.

        :param other: The other hex coordinate to calculate the distance to.
        :return: The distance between the two hex coordinates.
        """
        return self.to_vector().subtraction(other.to_vector()).magnitude()

    def __repr__(self) -> str:
        return f"HexCoordinate({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, HexCoordinate) and self.x == other.x and self.y == other.y


class Move:
    """
    Represents a move in the game.
    """

    def __init__(self, to_value: HexCoordinate, from_value: HexCoordinate = None):
        """
        :param to_value: The destination of the move.
        :param from_value: The origin of the move.
        """
        self.from_value = from_value
        self.to_value = to_value

    def get_delta(self):
        """
        Gets the distance between the origin and the destination.

        :return: The delta of the move as a Vector object.
        """
        return self.to_value.distance(self.from_value)

    def reversed(self):
        """
        Reverses the move.

        :return: The reversed move.
        """
        return Move(from_value=self.to_value, to_value=self.from_value)

    def __str__(self) -> str:
        return "Move(from = {}, to = {})".format(self.from_value, self.to_value)

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Move) and self.to_value == __o.to_value and \
               (self.from_value is None or self.from_value == __o.from_value)


class Team:
    """
    Represents a team in the game.
    """

    def __init__(self, color: str):
        """
        A Team can be either yourself or your opponent.
        
        :param color: The color of the team. Can be either 'ONE' or 'TWO'.
        """
        self.one = {
            'opponent': 'TWO',
            'name': 'ONE',
            'letter': 'R',
            'color': 'Rot'
        }
        self.two = {
            'opponent': 'ONE',
            'name': 'TWO',
            'letter': 'B',
            'color': 'Blau'
        }
        self.team_enum = None
        if color == "ONE":
            self.team_enum = self.one
        elif color == "TWO":
            self.team_enum = self.two
        else:
            raise Exception(f"Invalid : {color}")

    def team(self) -> 'Team':
        """
        :return: The team object.
        """
        return self

    def color(self) -> str:
        """
        :return: The color of this team.
        """
        return self.team_enum['name']

    def opponent(self) -> 'Team':
        """
        :return: The opponent of this team.
        """
        return Team(self.team_enum['opponent'])

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Team) and self.team_enum['name'] == __o.team_enum['name']

    def __str__(self) -> str:
        return self.team_enum['name']


class Field:
    """
    Represents a field in the game.
    """

    def __init__(self, coordinate: HexCoordinate, field: Union[int, str, Team]):
        """
        The Field represents a field on the game board.
        It says what state itself it has and where it is on the board.

        :param coordinate: The coordinate of the field.
        :param field: The state of the field. Can be either the number of fishes, or a Team.
        """
        self.coordinate = coordinate
        self.field: Union[int, str, Team]
        if isinstance(field, int):
            self.field = field
        elif field.isalpha():
            self.field = Team(field)
        else:
            raise TypeError(f"The field's input is wrong: {field}")

    def is_empty(self) -> bool:
        """
        :return: True if the field is has no fishes, False otherwise.
        """
        return self.field == 0

    def is_occupied(self) -> bool:
        """
        :return: True if the field is occupied by a penguin, False otherwise.
        """
        return isinstance(self.field, Team)

    def get_fish(self) -> Union[None, int]:
        """
        :return: The amount of fish on the field, None if the field is occupied.
        """
        return None if self.is_occupied() else self.field

    def get_team(self) -> Union[Team, None]:
        """
        :return: The team of the field if it is occupied by penguin, None otherwise.
        """
        return self.field if isinstance(self.field, Team) else None

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Field) and self.field == __o.field
    
    def __repr__(self):
        if isinstance(self.field, int):
            return f"Field({self.coordinate}, Fish({self.field}))"
        else:
            return f"Field({self.coordinate}, {self.field})"


class Board:
    """
    Class which represents a game board. Consisting of a two-dimensional array of fields.
    """

    def __init__(self, game_field: List[List[Field]]):
        """
        The Board shows the state where each field is, how many fish and which team is on each field.

        :param game_field: The game field as a two-dimensional array of fields.
        """
        self._game_field = game_field

    def get_empty_fields(self) -> List[Field]:
        """
        :return: A list of all empty fields.
        """
        fields: List[Field] = []
        for row in self._game_field:
            for field in row:
                if field.is_empty():
                    fields.append(field)
        return fields

    def is_occupied(self, coordinates: HexCoordinate) -> bool:
        """
        :param coordinates: The coordinates of the field.
        :return: True if the field is occupied, false otherwise.
        """
        return self.get_field(coordinates).is_occupied()

    def is_valid(self, coordinates: HexCoordinate) -> bool:
        """
        Checks if the coordinates are in the boundaries of the board.

        :param coordinates: The coordinates of the field.
        :return: True if the field is valid, false otherwise.
        """
        arrayCoordinates = coordinates.to_cartesian()
        return 0 <= arrayCoordinates.x < self.width() and 0 <= arrayCoordinates.y < self.height()

    def width(self) -> int:
        """
        :return: The width of the board.
        """
        return len(self._game_field)

    def height(self) -> int:
        """
        :return: The height of the board.
        """
        return len(self._game_field[0])

    def _get_field(self, x: int, y: int) -> Field:
        """
        Gets the field at the given coordinates.
        *Used only internally*

        :param x: The x-coordinate of the field.
        :param y: The y-coordinate of the field.
        :return: The field at the given coordinates.
        """
        return self._game_field[y][x]

    def get_field(self, position: HexCoordinate) -> Field:
        """
        Gets the field at the given position.

        :param position: The position of the field.
        :return: The field at the given position.
        :raise IndexError: If the position is not valid.
        """
        cartesian = position.to_cartesian()
        if self.is_valid(position):
            return self._get_field(cartesian.x, cartesian.y)

        raise IndexError(f"Index out of range: [x={cartesian.x}, y={cartesian.y}]")

    def get_field_or_none(self, position: HexCoordinate) -> Union[Field, None]:
        """
        Gets the field at the given position no matter if it is valid or not.

        :param position: The position of the field.
        :return: The field at the given position, or None if the position is not valid.
        """
        cartesian = position.to_cartesian()
        if self.is_valid(position):
            return self._get_field(cartesian.x, cartesian.y)
        return None

    def get_field_by_index(self, index: int) -> Field:
        """
        Gets the field at the given index. The index is the position of the field in the board.
        The field of the board is calculated as follows:

        - `x = index / width`
        - `y = index % width`
        - The index is 0-based. The index is calculated from the top left corner of the board.

        :param index: The index of the field.
        :return: The field at the given index.
        """
        return self.get_field(CartesianCoordinate.from_index(index).to_hex())

    def get_all_fields(self) -> List[Field]:
        """
        Gets all Fields of the board.

        :return: All Fields of the board.
        """
        return [self.get_field_by_index(i) for i in range(self.width() * self.height())]

    def compare_to(self, other: 'Board') -> List[Field]:
        """
        Compares two boards and returns a list of the Fields that are different.

        :param other: The other board to compare to.
        :return: A list of Fields that are different or a empty list if the boards are equal.
        """
        fields = []
        for x in range(len(self._game_field)):
            for y in range(len(self._game_field[0])):
                if self._game_field[x][y] != other._game_field[x][y]:
                    fields.append(self._game_field[x][y])
        return fields

    def contains(self, field: Field) -> bool:
        """
        Checks if the board contains the given field.

        :param field: The field to check for.
        :return: True if the board contains the field, False otherwise.
        """
        for row in self._game_field:
            if field in row:
                return True
        return False

    def contains_all(self, fields: List[Field]) -> bool:
        """
        Checks if the board contains all the given fields.

        :param fields: The fields to check for.
        :return: True if the board contains all the given fields, False otherwise.
        """
        for field in fields:
            if not self.contains(field):
                return False
        return True

    def get_moves_in_direction(self, origin: HexCoordinate, direction: Vector) -> List[Move]:
        """
        Gets all moves in the given direction from the given origin.

        :param origin: The origin of the move.
        :param direction: The direction of the move.
        :return: A list with all moves that fulfill the criteria.
        """
        moves = []
        for i in range(1, self.width()):
            destination = origin.add_vector(direction.scalar_product(i))
            if self._is_destination_valid(destination):
                moves.append(Move(from_value=origin, to_value=destination))
            else:
                break
        return moves

    def _is_destination_valid(self, field: HexCoordinate) -> bool:
        return self.is_valid(field) and not self.is_occupied(field) and not \
            self.get_field(field).is_empty()

    def possible_moves_from(self, position: HexCoordinate) -> List[Move]:
        """
        Returns a list of all possible moves from the given position. That are all moves in all hexagonal directions.

        :param position: The position to start from.
        :return: A list of all possible moves from the given position.
        :raise: IndexError if the position is not valid.
        """
        if not self.is_valid(position):
            raise IndexError(f"Index out of range: [x={position.x}, y={position.y}]")
        moves = []
        for direction in Vector().directions:
            moves.extend(self.get_moves_in_direction(position, direction))
        return moves

    def get_penguins(self) -> List[Field]:
        """
        Searches the board for all penguins.

        :return: A list of all Fields that are occupied by a penguin.
        """
        return [field for field in self.get_all_fields() if field.is_occupied()]

    def get_teams_penguins(self, team: Team) -> List[HexCoordinate]:
        """
        Searches the board for all penguins of the given team.

        :param team: The team to search for.
        :return: A list of all coordinates that are occupied by a penguin of the given team.
        """
        teams_penguins = []
        for x in range(self.width()):
            for y in range(self.height()):
                current_field = self.get_field(CartesianCoordinate(x, y).to_hex())
                if current_field.is_occupied() and current_field.get_team().team() == team:
                    coordinates = CartesianCoordinate(x, y).to_hex()
                    teams_penguins.append(coordinates)
        return teams_penguins

    def get_most_fish(self) -> List[Field]:
        """
        Returns a list of all fields with the most fish.

        :return: A list of Fields.
        """

        fields = list(filter(lambda field_x: not field_x.is_occupied(), self.get_all_fields()))
        fields.sort(key=lambda field_x: field_x.get_fish(), reverse=True)
        for i, field in enumerate(fields):
            if field.get_fish() < fields[0].get_fish():
                fields = fields[:i]
        return fields

    def get_board_intersection(self, other: 'Board') -> List[Field]:
        """
        Returns a list of all fields that are in both boards.

        :param other: The other board to compare to.
        :return: A list of Fields.
        """
        return [field for field in self.get_all_fields() if field in other.get_all_fields()]

    def get_fields_intersection(self, other: List[Field]) -> List[Field]:
        """
        Returns a list of all fields that are in both list of Fields.

        :param other: The other list of Fields to compare to.
        :return: A list of Fields.
        """
        return [field for field in self.get_all_fields() if field in other]

    def _move(self, move: Move) -> 'Board':
        """
        Moves the penguin from the origin to the destination.

        :param move: The move to execute.
        :return: The new board with the moved penguin.
        """
        new_board = Board(self._game_field)
        to_field = new_board.get_field(move.to_value)
        to_field_coo = move.to_value.to_cartesian()
        new_board._game_field[to_field_coo.x][to_field_coo.y] = Field(coordinate=move.to_value, field=to_field.field)
        if move.from_value:
            from_field_coo = move.from_value.to_cartesian()
            new_board._game_field[from_field_coo.x][from_field_coo.y] = Field(coordinate=move.from_value, field=0)
        return new_board

    @staticmethod
    def _fillUpString(placeholder: str, string: str) -> str:
        len_placeholder = len(placeholder)
        len_string = len(string)
        difference = len_placeholder - len_string
        rest = difference - int(difference / 2) * 2
        return "\xA0" * int(difference / 2) + string + "\xA0" * int(difference / 2) + "\xA0" * rest

    def pretty_print(self):
        """
        Prints the board in a pretty way.
        """
        result = ""
        for i, column in enumerate(self._game_field):
            for row in _hexagonTemplate:
                result += _emptyHexagonPlaceholder if i % 2 != 0 else ""
                for field in column:
                    if field.is_empty():
                        hexagon = " " * len(row)
                    elif "XXXXXXXXX" in row:
                        hexagon = row.replace("XXXXXXXXX", self._fillUpString("XXXXXXXXX", str(field.coordinate)))
                    else:
                        hexagon = row.replace("YYYYYYYYY", self._fillUpString("YYYYYYYYY", str(field.field)))
                    result += hexagon
                result += "\n"
        print(result)

    def __eq__(self, __o: 'Board'):
        return self._game_field == __o._game_field


class Fishes:
    """
    Represents the amount of fish each player has.
    """

    def __init__(self, fishes_one: int, fishes_two: int):
        self.fishes_one = fishes_one
        self.fishes_two = fishes_two

    def get_fish_by_team(self, team: Team):
        """
        Looks up the amount of fish a team has.

        :param team: A team object, that represents the team to get the fish amount of.
        :return: The amount of fish of the given team.
        """
        return self.fishes_one if team.team_enum == Team("ONE").team_enum else self.fishes_two


class GameState:
    """
       A `GameState` contains all information, that describes the game state at a given time, that is, between two game
       moves.

       This includes:
            - the board
            - a consecutive turn number (round & turn) and who's turn it is
            - the team that has started the game
            - the number of fishes each player has
            - the last move made

       The `GameState` is thus the central object through which all essential information of the current game can be
       accessed.

       Therefore, for easier handling, it offers further aids, such as:
            - a method to calculate available moves
            - a method to perform a move for simulating future game states

       The game server sends a new copy of the `GameState` to both participating players after each completed move,
       describing the then current state.
       """

    def __init__(self, board: Board, turn: int, start_team: Team, fishes: Fishes, last_move: Move = None):
        """
        Creates a new `GameState` with the given parameters.

        :param board: The board of the game.
        :param turn: The turn number of the game.
        :param start_team: The team that has the first turn.
        :param fishes: The number of fishes each team has.
        :param last_move: The last move made.
        """
        self.start_team = start_team
        self.board = board
        self.turn = turn
        self.round = int((self.turn + 1) / 2)
        self.current_team = self.current_team_from_turn()
        self.other_team = self.current_team_from_turn().opponent()
        self.last_move = last_move
        self.fishes = fishes
        self.current_pieces = self.board.get_teams_penguins(self.current_team)
        self.possible_moves = self._get_possible_moves(self.current_team)

    def _get_possible_moves(self, current_team: Team = None) -> List[Move]:
        """
        Gets all possible moves for the current team.
        That includes all possible moves from all Fields that are not occupied by a penguin from that team.

        :param current_team: The team to get the possible moves for.
        :return: A list of all possible moves from the current player's turn.
        """
        current_team = current_team or self.current_team
        moves = []
        if len(self.board.get_teams_penguins(current_team)) < 4:
            for x in range(self.board.width()):
                for y in range(self.board.height()):
                    field = self.board.get_field(CartesianCoordinate(x, y).to_hex())
                    if not field.is_occupied() and field.get_fish() == 1:
                        moves.append(Move(from_value=None, to_value=CartesianCoordinate(x, y).to_hex()))
        else:
            for piece in self.board.get_teams_penguins(current_team):
                moves.extend(self.board.possible_moves_from(piece))
        return moves

    def current_team_from_turn(self) -> Team:
        """
        Calculates the current team from the turn number.

        :return: The team that has the current turn.
        """
        current_team_by_turn = self.start_team if self.turn % 2 == 0 else self.start_team.opponent()
        if not self._get_possible_moves(current_team_by_turn):
            return current_team_by_turn.opponent()
        return current_team_by_turn

    def perform_move(self, move: Move) -> 'GameState':
        """
        Performs the given move on the current game state.

        :param move: The move to perform.
        :return: The new game state after the move has been performed.
        """
        if self.is_valid_move(move):
            new_board = self.board._move(move)
            adding_fish = new_board.get_field(move.to_value).get_fish()
            new_fishes_one = self.fishes.fishes_one + adding_fish if self.current_team == Team("ONE") else \
                self.fishes.fishes_one
            new_fishes_two = self.fishes.fishes_two + adding_fish if self.current_team == Team("TWO") else \
                self.fishes.fishes_two
            new_fishes = Fishes(new_fishes_one, new_fishes_two)
            return GameState(board=new_board, turn=self.turn + 1, start_team=self.start_team, fishes=new_fishes,
                             last_move=move)
        logging.error(f"Performed invalid move while simulating: {move}")
        raise Exception(f"Invalid move: {move}")

    def is_valid_move(self, move: Move) -> bool:
        """
        Checks if the given move is valid.
        
        :param move: The move to check.
        :return: True if the move is valid, False otherwise.
        """
        for possible_move in self.possible_moves:
            if possible_move == move:
                return True
        return False
