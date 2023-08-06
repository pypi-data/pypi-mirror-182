import uuid
import requests
from pyvis.network import Network


class SynapseGraphError(Exception):
    text: str

    def __init__(self, text: str = 'Unknown Error'):
        self.text = text

    def __str__(self):
        return self.text


class SynapseGraph:
    rooms: dict
    users: dict
    graph_name: str

    HEADERS: dict
    MATRIX_HOMESERVER: str

    graph: Network

    user_node_color: str
    ext_user_node_color: str
    room_node_color: str

    min_room_d: int = 10
    max_room_d: int = 60

    hide_usernames: bool
    u2u_relation: bool

    def __init__(self, name: str, headers: dict, matrix_homeserver: str,
                 user_node_color: str = '#326051', room_node_color: str = '#99a9af',
                 ext_user_node_color: str = '#B4976D', hide_usernames: bool = True,
                 u2u_relation: bool = True):
        self.graph_name = name
        self.HEADERS = headers
        self.MATRIX_HOMESERVER = matrix_homeserver
        self.graph = Network(height='600px', width='100%', cdn_resources='in_line')
        self.user_node_color = user_node_color
        self.room_node_color = room_node_color
        self.ext_user_node_color = ext_user_node_color
        self.hide_usernames = hide_usernames
        self.u2u_relation = u2u_relation

        self.users = {}
        self.rooms = {}
        self.__load()
        self.__make_nodes_in_graph()
        self.__calculate_edges()

    def __str__(self):
        return self.graph_name

    @property
    def json(self) -> str:
        return self.graph.to_json(max_depth=2048)

    def show(self, file_name: str = 'nx') -> None:
        """Render and open graph to html"""

        self.graph.options = {
            "physics": {
                "barnesHut": {
                    "theta": 0.6,
                    "gravitationalConstant": -22200,
                    "centralGravity": 0.15,
                    "springLength": 170
                },
                "minVelocity": 1.4,
                "timestep": 0.49
            }
        }

        self.graph.show(f'{file_name}.html')

    @property
    def html(self) -> str:
        return self.graph.generate_html()

    def refresh(self) -> None:
        """Just refresh all data"""

        self.clear()
        self.__load()
        self.__make_nodes_in_graph()
        self.__calculate_edges()

    def clear(self) -> None:
        """Clear all collected data"""

        self.rooms.clear()
        self.users.clear()
        self.graph = Network(height='600px', width='100%')

    def __calculate_edges(self) -> None:
        """
        Makes edges between users and rooms, users and users

        u2u_relation: Edges between users aka DM
        """

        for user in self.users.values():
            for room_id in user.joined_rooms:
                room: SynapseGraph.Room = self.rooms[room_id]

                if not room.public:
                    continue

                self.graph.add_edge(user.user_uuid, room.room_id)

        if self.u2u_relation:
            for user in self.users.values():
                user: SynapseGraph.User

                for second_user in self.users.values():
                    second_user: SynapseGraph.User

                    if user == second_user:
                        continue

                    for room_id in user.joined_rooms:
                        if self.rooms[room_id].public:
                            continue

                        if room_id in second_user.joined_rooms:
                            self.graph.add_edge(user.user_uuid, second_user.user_uuid)

    def save_html(self, path_with_name: str):
        self.graph.write_html(path_with_name)

    def __make_nodes_in_graph(self) -> None:
        """Just draw nodes in graph"""

        # Users
        for user in self.users.values():
            user: SynapseGraph.User

            self.graph.add_node(
                n_id=user.user_uuid,
                color=self.user_node_color,
                label='user' if self.hide_usernames else user.display_name,
                size=5
            )

        # Rooms
        # Calculate adaptive size for room node
        min_joined_users: int
        max_joined_users: int

        first: bool = True
        for room in self.rooms.values():
            room: SynapseGraph.Room

            if first:
                min_joined_users = max_joined_users = room.joined_members
                first = False
            else:
                if room.joined_members < min_joined_users:
                    min_joined_users = room.joined_members

                if room.joined_members > max_joined_users:
                    max_joined_users = room.joined_members

        for room in self.rooms.values():
            room: SynapseGraph.Room

            # Skipping DM
            if not room.public:
                continue

            if room.joined_members != min_joined_users:
                node_size: float = ((self.max_room_d - self.min_room_d) / (100 / (
                        (room.joined_members / (max_joined_users - min_joined_users)) * 100))) + self.min_room_d
            else:
                node_size = room.joined_members + self.min_room_d

            self.graph.add_node(n_id=room.room_id, label=str(room), color=self.room_node_color, size=node_size)

    def __load(self) -> None:
        # Load users first
        response = requests.get(f'https://{self.MATRIX_HOMESERVER}/_synapse/admin/v2/users?dir=f&from=0&guests=false',
                                headers=self.HEADERS)

        if not response.ok:
            raise SynapseGraphError(response.json()['error'])

        for user in response.json()['users']:
            user_obj = self.User(
                name=user['name'],
                display_name=user['displayname'],
                avatar_url=user['avatar_url']
            )
            self.users[user_obj.name] = user_obj

            # Then load joined rooms
            response = requests.get(f'https://{self.MATRIX_HOMESERVER}/_synapse/admin/v1/users/'
                                    f'{user["name"]}/joined_rooms?dir=b&from=0&order_by=id', headers=self.HEADERS)

            if response.ok:
                user_obj.joined_rooms = response.json()['joined_rooms']

        # Make main list of rooms
        rooms = []
        for user in self.users.values():
            rooms += user.joined_rooms

        rooms = list(dict.fromkeys(rooms))  # Delete duplicates

        # Parse additional information about every room
        for room_id in rooms:
            response = requests.get(
                f'https://{self.MATRIX_HOMESERVER}/_synapse/admin/v1/rooms/{room_id}',
                headers=self.HEADERS
            )

            if not response.ok:
                continue

            room = response.json()

            if room['join_rules'] is None:
                continue

            self.rooms[room_id] = self.Room(
                name=room['name'],
                avatar_url=room['avatar'],
                canonical_alias=room['canonical_alias'],
                joined_members=room['joined_members'],
                room_id=room['room_id'],
                public=room['join_rules'] in ('restricted', 'public')
            )

    class Room:
        name: str | None
        canonical_alias: str | None
        joined_members: int
        room_id: str
        public: bool
        avatar_url: str | None

        def __init__(
                self,
                name: str | None,
                canonical_alias: str | None,
                joined_members: int,
                room_id: str,
                public: bool,
                avatar_url: str | None
        ):
            self.name = name
            self.canonical_alias = canonical_alias
            self.joined_members = joined_members
            self.room_id = room_id
            self.public = public
            self.avatar_url = avatar_url

        def __str__(self):
            if self.canonical_alias is None:
                return self.room_id
            else:
                return self.canonical_alias

    class User:
        name: str
        display_name: str
        avatar_url: str | None
        joined_rooms: tuple
        user_uuid: str

        def __str__(self):
            return self.name

        def __init__(self, name: str, display_name: str, avatar_url: None | str):
            self.name = name
            self.display_name = display_name
            self.avatar_url = avatar_url

            # Uniq id need to hide usernames
            self.user_uuid = uuid.uuid4().hex
