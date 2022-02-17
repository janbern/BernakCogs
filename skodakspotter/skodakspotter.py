from redbot.core import commands


class SkodakSpotter(commands.Cog):
    """Je Stegomrd online?"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def skodak(self, ctx):

        import requests
        from bs4 import BeautifulSoup
        url = 'http://armory.twinstar.cz/character-feed.xml?r=Apollo&cn=Stegomrd'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'xml')
        timestamp = soup.find('character')
        if timestamp is not None:
            await ctx.send(timestamp['lastModified'])
        else:
            await ctx.send("Sorry, can't connect to Twinstar rn")
