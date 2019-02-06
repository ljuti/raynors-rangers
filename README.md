# Raynor's Rangers SC2 Bot

[Join the official Discord server for the competition!](https://discord.gg/D9XEhWY)

Documentation for the `python-sc2`:
- [The BotAI-class](https://github.com/Dentosal/python-sc2/wiki/The-BotAI-class)
- [Units and actions](https://github.com/Dentosal/python-sc2/wiki/Units-and-actions)

## Tips

- The [Python SC2 Wiki](https://github.com/Dentosal/python-sc2/wiki) contains useful material to get you started
- The [Starcraft II AI Discord](https://discord.gg/D9XEhWY) gives you access to the community and support
- The code for your bot goes to [bot/main.py](bot/main.py): simple examples can be found at [python-sc2 examples](https://github.com/Dentosal/python-sc2/tree/master/examples)
  * Further, our server-side runner expects to find a class names `MyBot` in this file.
- On our servers, your code will be run on python 3.6. (currently, python 3.6.3)
- You can modify the `run_locally.py` starter script to your liking as you might want to increase the difficulty of the game-AI at some point
  * Map can be selected by using its file name in lowercase, for instance: `run_game(maps.get("(2)dreamcatcherle")`
- If you need to use any Python dependencies, just paste the libraries into your team repo
- Push code to Gitlab early and push it often, to see your progress and make sure your bot works correctly on our servers.
- Watch how your bot fares on the Ranking on the [Artificial Overmind Challenge site](https://artificial-overmind.reaktor.com/)  
