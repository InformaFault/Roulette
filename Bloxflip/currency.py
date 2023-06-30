import cloudscraper


scraper = cloudscraper.create_scraper()


class Currency:
    def __init__(self) -> None:
        pass

    @staticmethod
    def balance(auth: str) -> int:
        """Get user's balance from their auth token"""

        request = scraper.get("https://api.bloxflip.com/user", headers={
            "x-auth-token": auth
        }).json()
        

        return request["user"]["wallet"]

    @staticmethod
    def affiliate(auth: str) -> int:
        """Get the amount of currency available on their affiliate"""

        request = scraper.get("https://api.bloxflip.com/user/affiliates", headers={
            "x-auth-token": auth
        }).json()
        
            

        return request["affiliateMoneyAvailable"]

    @staticmethod
    def claimAfiliate(auth: str, amount: int) -> dict:
        """Claim the currency insied the user's affiliate balance"""

        response = scraper.post("https://api.bloxflip.com/user/affiliates/claim",
                    headers={
                        "x-auth-token": auth
                    }, json={
                        "amount": str(amount)
                    }
                )

        if response.status_code == 200:
            return response.json()

        

    @staticmethod
    def withdraw(auth: str, amount: int) -> dict:
        """Withdraw Bloxflip currency into Roblox"""

        response = scraper.post("https://api.bloxflip.com/user/withdrawTarget", headers={
                    "x-auth-token": auth
                }, json={
                    "amount": str(int(amount))
                }
            )

        

        return response.json()
