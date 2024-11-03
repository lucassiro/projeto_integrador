import httpx


class CamaraAPI:
    def __init__(self) -> None:
        self.base_url = "https://dadosabertos.camara.leg.br/api/v2"

    def request(self, endpoint: str) -> dict:
        response = httpx.get(f"{self.base_url}/{endpoint}")
        return response.json()

    def get_deputados(self) -> dict:
        return self.request("deputados")

    def get_despesas(self, id: int, year: int = 2022) -> dict:
        return self.request(f"deputados/{id}/despesas?ano={year}")
