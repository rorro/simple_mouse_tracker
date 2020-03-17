def get_config(conf):
    print("track_data:",conf.track_data)


def create_file():
    self.DEFAULT_STATS = [
            "#total_coords=0",
            "#total_clicks=0",
            ]
    data_file = open("stats.dat", "a")
    data_file.write("hello")
