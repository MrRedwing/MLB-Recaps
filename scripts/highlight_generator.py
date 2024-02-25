from mlbrecaps import Team, Date, DateRange, GameGenerator, Clips

def highlightGenerator(team: Team, dates: Date | DateRange, path: str):
    # get all games on that date
    games = GameGenerator(team, dates).get_games()

    # Iterate over every game found
    for index, game in enumerate(games):
        # Determine whether the team is home or away
        homeRoad = game.road_status(team)

        # Get the top ten plays of the game
        homeHighlights = game.get_highlights(10, homeRoad) 
        homeClips = Clips(homeHighlights, homeRoad) # Generate clips of the plays from the Twins broadcast

        # Download all highlight clips
        print(f"Game {index + 1}: {game}")
        homeClips.download(f"{path}{index}", True)

if __name__ == "__main__":
    # Get teams for the search
    team = Team("MIN")
    # dates = Date(7, 20, 2023)
    dates = Date(9, 17, 2023)

    highlightGenerator(team, dates, "/home/karsten/coding/python/recaps/videos/")