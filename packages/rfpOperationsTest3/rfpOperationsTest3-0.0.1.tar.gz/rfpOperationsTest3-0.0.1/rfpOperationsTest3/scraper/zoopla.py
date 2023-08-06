from .base import Scraper


class ZooplaScraper(Scraper):

    BASE_URL = "https://www.zoopla.co.uk/"

    def __init__(self) -> None:
        super().__init__()

    def set_search_settings(self, city_name: str = None, max_price: int = None):
        super().set_search_settings(city_name=city_name, max_price=max_price)

    def __iter__(self):
        assert (
            "city_name" in self.search_settings
        ), "make sure to set `search_settings` first"
        assert (
            "max_price" in self.search_settings
        ), "make sure to set `search_settings` first"

        city_name = self.search_settings["city_name"]
        max_price = self.search_settings["max_price"]

        self.url = (
            self.BASE_URL
            + f"to-rent/property/{city_name}/?price_frequency=per_month&q={city_name}&results_sort=newest_listings&search_source=refine&price_max={max_price}&view_type=list"
        )
        print(self._url)
        pages = self.soup.find("div", attrs={"data-testid": "regular-listings"})

        for page in pages:
            # find a property's id

            try:
                id = [
                    str(el)
                    for el in str(page.find(href=True)["href"]).split("/")
                    if el.isdigit()
                ][0]

            except IndexError:  # premium
                print("ID could not found, searching for it...")
                id = [
                    i
                    for i in [
                        el["href"]
                        for el in page.find_all(href=True)
                        if "search_identifier" in el["href"]
                    ][0].split("/")
                    if i.isdigit()
                ][0]

            any_bed = any(
                [
                    el.text
                    for el in page.find("div").find_all("span")
                    if el.text == "Bedrooms"
                ]
            )
            any_bath = any(
                [
                    el.text
                    for el in page.find("div").find_all("span")
                    if el.text == "Bathrooms"
                ]
            )
            any_chair = any(
                [
                    el.text
                    for el in page.find("div").find_all("span")
                    if el.text == "Living rooms"
                ]
            )

            rooms = [el.text for el in page.find("div").find_all("span")]

            bed_num = int(rooms[rooms.index("Bedrooms") + 1]) if any_bed else 0
            bath_num = int(rooms[rooms.index("Bathrooms") + 1]) if any_bath else 0
            chair_num = int(rooms[rooms.index("Living rooms") + 1]) if any_chair else 0

            all_info_raw = page.find_all("p")
            all_info = [all_info_raw[i].text for i in range(len(all_info_raw))]

            # str contains 'pcm', is our price
            # strings contains just digit inside is rooms we are looking for

            # convert raw <str> price to <int>
            raw_price = [info for info in all_info if "pcm" in info][0]
            price = int(
                "".join(el for el in raw_price if el.isdigit())
            )  # unit: £, per: month

            address = page.find("h3").text

            p_info = {
                "id": int(id),
                "price": price,
                "num_beds": bed_num,
                "num_baths": bath_num,
                "num_liv_rooms": chair_num,
                "address": address,
            }

            yield p_info
