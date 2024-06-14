class Band:
    def __init__(self, name, hometown):
        self._name = None  # Initialize _name attribute
        self.name = name  # Use property setter
        self._hometown = hometown  # No setter for immutability
        self._concerts = []
        self._venues = set()
        print(f"Initialized Band: {self.name}, {self.hometown}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def hometown(self):
        return self._hometown

    def concerts(self):
        return self._concerts

    def venues(self):
        return list(self._venues)

    def play_in_venue(self, venue, date):
        new_concert = Concert(date, self, venue)
        return new_concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]

    def __repr__(self):
        return f"Band(name={self.name}, hometown={self.hometown})"


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self._date = None  # Initialize _date attribute
        self._band = None  # Initialize _band attribute
        self._venue = None  # Initialize _venue attribute
        self.date = date  # Use property setter
        self.band = band  # Type check handled in property setter
        self.venue = venue  # Type check handled in property setter

        Concert.all.append(self)
        band._concerts.append(self)
        band._venues.add(venue)
        venue.add_concert(self)
        print(f"Initialized Concert: {self.date}, {self.band.name}, {self.venue.name}")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string.")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError("Band must be a Band instance.")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError("Venue must be a Venue instance.")

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def __repr__(self):
        return f"Concert(date={self.date}, band={self.band.name}, venue={self.venue.name})"


class Venue:
    def __init__(self, name, city):
        self._name = None  # Initialize _name attribute
        self._city = None  # Initialize _city attribute
        self.name = name  # Use property setter
        self.city = city  # Use property setter
        self._concerts = set()
        self._bands = set()
        print(f"Initialized Venue: {self.name}, {self.city}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string.")

    def concerts(self):
        return list(self._concerts)

    def bands(self):
        return list(self._bands)

    def add_concert(self, concert):
        if concert not in self._concerts:
            self._concerts.add(concert)
            self._bands.add(concert.band)

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None

    def __repr__(self):
        return f"Venue(name={self.name}, city={self.city})"
