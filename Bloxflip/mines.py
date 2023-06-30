import cloudscraper, json, time

scraper = cloudscraper.create_scraper()


class Mine:
    """A class for a Mines game"""

    def __init__(self, game: dict) -> None:
        if game["hasGame"]:

            info = game["game"]
            self.competed_levels = info["uncoveredLocations"]
            self.client_seed = info["clientSeed"]
            self.multiplier = game["multiplier"]
            self.exploded = info["exploded"]

            self.timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info["created"]))
            self.user_id = info["userId"]
            self.nonce = info["nonce"]
            self.uuid = info["uuid"]

            self.mines = info["minesAmount"]
            self.bet_amount = info["betAmount"]
            self.payout = info["payout"]

            self.active = True
        else:
            self.active = False


class Mines:
    def __init__(self, auth: str) -> None:
        self.auth = auth

    def create(self, betamount: float, mines: int) -> None:
        """Creates a mines game"""

        response = scraper.post("https://api.bloxflip.com/games/mines/create", headers={
                        "x-auth-token": self.auth
                    },
                    json={
                        "betAmount": betamount,
                        "mines": mines
                    }
                )

        

        

        

    def choose(self, choice: int) -> bool:
        """Chooses a tile to bet on"""

        response = scraper.post("https://api.bloxflip.com/games/mines/action", headers={
                            "x-auth-token": self.auth
                        },
                        json={
                            "cashout": False,
                            "mine": choice
                        }
                    )

        

       

    def cashout(self) -> bool:
        """Cashouts the winnings from the current Mines game"""

        response = scraper.post("https://api.bloxflip.com/games/mines/action", headers={
                            "x-auth-token": self.auth
                        },
                        json={
                            "cashout": True
                        }
                    )

       

    @property
    def current(self) -> Mine:
        request = scraper.get("https://api.bloxflip.com/games/towers", headers={
                        "x-auth-token": self.auth
                    }
                ).json()

        
           
        
